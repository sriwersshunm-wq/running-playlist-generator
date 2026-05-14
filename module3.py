from module1 import get_tracks
from module2 import RUN_ARCS, CIRCLE_OF_FIFTHS

ALL_KEYS = [0,1,2,3,4,5,6,7,8,9,10,11]

def build_playlist(run_type='5k_race', start_key=0):
    arc = RUN_ARCS[run_type]
    playlist = []
    current_key = start_key

    for phase in arc:
        mins_needed = phase['mins']
        tracks_needed = int(mins_needed / 3.5) + 1

        # Try circle of fifths keys first
        allowed_keys = CIRCLE_OF_FIFTHS[current_key]
        tracks = get_tracks(
            bpm_min=phase['bpm'][0],
            bpm_max=phase['bpm'][1],
            mode=phase['mode'],
            key_list=allowed_keys,
            energy_min=phase['energy'][0],
            energy_max=phase['energy'][1],
            n=tracks_needed
        )

        # Fallback: widen to all keys if not enough tracks to fill the phase
        if len(tracks) < tracks_needed:
            tracks = get_tracks(
                bpm_min=phase['bpm'][0],
                bpm_max=phase['bpm'][1],
                mode=phase['mode'],
                key_list=ALL_KEYS,
                energy_min=phase['energy'][0],
                energy_max=phase['energy'][1],
                n=tracks_needed
            )

        filled = []
        total = 0
        for t in tracks:
            if total >= mins_needed:
                break
            filled.append(t)
            current_key = t['key']
            total += 3.5

        playlist.append({'phase': phase['phase'], 'tracks': filled})
        print(f"[{phase['phase']:10}] {len(filled)} tracks | last key={current_key}")

    return playlist

if __name__ == "__main__":
    print("Building 5K race playlist...\n")
    playlist = build_playlist('5k_race', start_key=0)
    print("\n--- FULL PLAYLIST ---")
    for phase in playlist:
        print(f"\n{phase['phase'].upper()}")
        for t in phase['tracks']:
            print(f"  {t['bpm']} BPM | {'Major' if t['mode']==1 else 'Minor'} | {t['name']} — {t['artist']}")
            