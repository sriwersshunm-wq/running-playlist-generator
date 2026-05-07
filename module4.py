import csv
import datetime
import os
from module1 import get_tracks
from module2 import RUN_ARCS
from module3 import build_playlist


def export_playlist(playlist, run_type='5k_race', run_label='A1'):
    """
    Export the generated playlist to:
      1. A readable .txt file (phase breakdown, song info)
      2. A .txt file of Spotify URIs — paste into open.spotify.com/playlist-import
         or any third-party importer (e.g. https://www.spotifyplaylist.net/)
    """
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M')
    base_name = f"playlist_{run_type}_{run_label}_{timestamp}"

    # ── 1. Human-readable breakdown ──────────────────────────────────────────
    readable_path = f"{base_name}_readable.txt"
    with open(readable_path, 'w') as f:
        f.write(f"Theory-Aware Playlist — {run_type.upper()} | Run {run_label}\n")
        f.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write("=" * 60 + "\n\n")

        total_tracks = 0
        for phase in playlist:
            phase_name = phase['phase'].upper()
            tracks = phase['tracks']
            f.write(f"[{phase_name}] — {len(tracks)} tracks\n")
            f.write("-" * 40 + "\n")
            for t in tracks:
                mode_str = 'Major' if t['mode'] == 1 else 'Minor'
                f.write(
                    f"  {t['bpm']:3} BPM | {mode_str:5} | key={t['key']:2} | "
                    f"energy={t['energy']:.2f} | {t['name']} — {t['artist']}\n"
                )
            f.write("\n")
            total_tracks += len(tracks)

        f.write(f"Total tracks: {total_tracks}\n")

    print(f"Readable playlist saved → {readable_path}")

    # ── 2. Spotify URI list ───────────────────────────────────────────────────
    uri_path = f"{base_name}_spotify_uris.txt"
    with open(uri_path, 'w') as f:
        f.write("# Paste these URIs into https://www.spotifyplaylist.net/\n")
        f.write("# or open Spotify desktop → New Playlist → drag-import\n\n")
        for phase in playlist:
            f.write(f"# --- {phase['phase'].upper()} ---\n")
            for t in phase['tracks']:
                f.write(f"spotify:track:{t['spotify_id']}\n")

    print(f"Spotify URI list saved  → {uri_path}")
    print(f"\nTo add to Spotify: go to https://www.spotifyplaylist.net/, paste the URI file contents.")

    return readable_path, uri_path


def log_session(condition, mile_splits, avg_hr_per_mile, rpe_per_mile, flow_score, notes=""):
    """Log validation run data to CSV for statistical analysis."""
    filename = 'validation_data.csv'
    file_exists = os.path.isfile(filename)
    row = {
        'date': datetime.date.today().isoformat(),
        'condition': condition,
        'total_time': round(sum(mile_splits), 2),
        'final_mile_pace': mile_splits[-1],
        'mean_hr': round(sum(avg_hr_per_mile) / len(avg_hr_per_mile), 1),
        'mean_rpe': round(sum(rpe_per_mile) / len(rpe_per_mile), 1),
        'flow_score': flow_score,
        'notes': notes,
    }
    with open(filename, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)
    print(f"Session logged: {condition} on {row['date']}")


if __name__ == "__main__":
    print("Generating theory-aware 5K playlist...\n")
    playlist = build_playlist('5k_race', start_key=0)

    print("\n--- EXPORTING ---")
    export_playlist(playlist, run_type='5k_race', run_label='A2')
    