from module1 import get_tracks
from module2 import RUN_ARCS, CIRCLE_OF_FIFTHS

arc = RUN_ARCS['5k_race']
for phase in arc:
    tracks = get_tracks(
        bpm_min=phase['bpm'][0],
        bpm_max=phase['bpm'][1],
        mode=phase['mode'],
        key_list=[0,1,2,3,4,5,6,7,8,9,10,11],
        energy_min=phase['energy'][0],
        energy_max=phase['energy'][1]
    )
    print(f"{phase['phase']:10} — {len(tracks)} tracks found")