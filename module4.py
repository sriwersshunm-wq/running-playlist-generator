import csv
import datetime
import os
from module1 import get_tracks
from module2 import RUN_ARCS
from module3 import build_playlist

def export_playlist_to_text(playlist, run_type='5k_race'):
    """Print the playlist in a clean format for manual Spotify queue."""
    print(f"\n=== {run_type.upper()} PLAYLIST ===")
    print("Add these songs to your Spotify queue in order:\n")
    for phase in playlist:
        print(f"--- {phase['phase'].upper()} ---")
        for t in phase['tracks']:
            print(f"  {t['name']} — {t['artist']} ({t['bpm']} BPM, {'Major' if t['mode']==1 else 'Minor'})")
    print("\n")

def log_session(condition, km_splits, avg_hr_per_km, rpe_per_km, flow_score, notes=""):
    """Log validation run data to CSV for statistical analysis."""
    filename = 'validation_data.csv'
    file_exists = os.path.isfile(filename)
    row = {
        'date': datetime.date.today().isoformat(),
        'condition': condition,
        'total_time': sum(km_splits),
        'final_km_pace': km_splits[-1],
        'mean_hr': round(sum(avg_hr_per_km)/len(avg_hr_per_km), 1),
        'mean_rpe': round(sum(rpe_per_km)/len(rpe_per_km), 1),
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
    export_playlist_to_text(playlist, '5k_race')