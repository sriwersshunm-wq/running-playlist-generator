# Module 2 — Music theory rules engine

CIRCLE_OF_FIFTHS = {
    0:[0,7,5],   # C → G, F
    1:[1,8,6],   # C# → G#, F#
    2:[2,9,7],   # D → A, G
    3:[3,10,8],  # Eb → Bb, Ab
    4:[4,11,9],  # E → B, A
    5:[5,0,10],  # F → C, Bb
    6:[6,1,11],  # F# → C#, B
    7:[7,2,0],   # G → D, C
    8:[8,3,1],   # Ab → Eb, C#
    9:[9,4,2],   # A → E, D
    10:[10,5,3], # Bb → F, Eb
    11:[11,6,4], # B → F#, E
}

RUN_ARCS = {
    'easy': [
        {'phase':'main','bpm':(125,145),'mode':1,'energy':(0.45,0.65),'mins':40},
    ],
    'tempo': [
        {'phase':'warmup','bpm':(130,140),'mode':1,'energy':(0.55,0.65),'mins':10},
        {'phase':'grind','bpm':(155,168),'mode':0,'energy':(0.40,0.90),'mins':25},
        {'phase':'cooldown','bpm':(110,125),'mode':1,'energy':(0.35,0.65),'mins':10},
    ],
    '5k_race': [
        {'phase':'warmup','bpm':(130,140),'mode':1,'energy':(0.55,0.65),'mins':5},
        {'phase':'build','bpm':(145,158),'mode':1,'energy':(0.65,0.75),'mins':7},
        {'phase':'grind','bpm':(155,167),'mode':0,'energy':(0.40,0.90),'mins':6},
        {'phase':'kick','bpm':(168,186),'mode':1,'energy':(0.40,0.90),'mins':3},
        {'phase':'cooldown','bpm':(110,125),'mode':1,'energy':(0.35,0.70),'mins':9},
    ],
}

if __name__ == "__main__":
    print("RUN ARCS loaded:")
    for arc_name, phases in RUN_ARCS.items():
        print(f"\n{arc_name}:")
        for p in phases:
            print(f"  {p['phase']:10} | BPM {p['bpm'][0]}-{p['bpm'][1]} | {'Major' if p['mode']==1 else 'Minor'} | {p['mins']} min")
    print("\nCIRCLE OF FIFTHS loaded — adjacent keys for C (0):", CIRCLE_OF_FIFTHS[0])