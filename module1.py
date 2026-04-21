import pandas as pd

df = pd.read_csv('songs.csv')

def get_tracks(bpm_min, bpm_max, mode, key_list,
               energy_min, energy_max, valence_min=0.2, n=20):
    """Filter tracks from local dataset matching phase requirements."""
    filtered = df[
        (df['bpm'] >= bpm_min) & (df['bpm'] <= bpm_max) &
        (df['mode'] == mode) &
        (df['key'].isin(key_list)) &
        (df['energy'] >= energy_min) & (df['energy'] <= energy_max) &
        (df['valence'] >= valence_min)
    ]
    return filtered.head(n).to_dict('records')

if __name__ == "__main__":
    test_tracks = get_tracks(
        bpm_min=120, bpm_max=150,
        mode=1,
        key_list=[0,1,2,3,4,5,6,7,8,9,10,11],
        energy_min=0.4, energy_max=0.8
    )
    print(f"Found {len(test_tracks)} tracks")
    for t in test_tracks:
        print(f"{t['bpm']} BPM | {'Major' if t['mode']==1 else 'Minor'} | key={t['key']} | {t['name']} — {t['artist']}")