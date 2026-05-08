import argparse
from module3 import build_playlist
from module4 import export_playlist

KEY_NAMES = {
    0: 'C', 1: 'C#', 2: 'D', 3: 'Eb', 4: 'E',
    5: 'F', 6: 'F#', 7: 'G', 8: 'Ab', 9: 'A',
    10: 'Bb', 11: 'B'
}

RUN_TYPE_DESCRIPTIONS = {
    'easy':     'Easy run — steady major key, moderate BPM throughout',
    'tempo':    'Tempo run — warmup → minor grind → major cooldown',
    '5k_race':  '5K race — full harmonic arc: warmup → build → grind → kick → cooldown',
}

def print_banner():
    print("\n" + "=" * 60)
    print("  MUSIC THEORY-AWARE RUNNING PLAYLIST GENERATOR")
    print("  ASDRP Research Project — github.com/sriwersshunm-wq")
    print("=" * 60 + "\n")

def print_playlist(playlist):
    print("\n--- PLAYLIST BREAKDOWN ---\n")
    total = 0
    for phase in playlist:
        print(f"  [{phase['phase'].upper()}]")
        for t in phase['tracks']:
            mode = 'Major' if t['mode'] == 1 else 'Minor'
            print(f"    {t['bpm']:3} BPM | {mode:5} | key={KEY_NAMES[t['key']]:2} | {t['name']} — {t['artist']}")
        print()
        total += len(phase['tracks'])
    print(f"  Total tracks: {total}\n")

def main():
    parser = argparse.ArgumentParser(
        description='Generate a music-theory-aware running playlist.',
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        '--type', '-t',
        choices=['easy', 'tempo', '5k_race'],
        default='5k_race',
        help=(
            "Run type:\n"
            "  easy     — Easy run, steady pace\n"
            "  tempo    — Tempo run, minor grind phase\n"
            "  5k_race  — Full 5K race arc (default)\n"
        )
    )

    parser.add_argument(
        '--key', '-k',
        type=int,
        choices=range(12),
        default=0,
        metavar='KEY (0-11)',
        help=(
            "Starting musical key (0=C, 1=C#, 2=D, 3=Eb, 4=E,\n"
            "  5=F, 6=F#, 7=G, 8=Ab, 9=A, 10=Bb, 11=B)\n"
            "  Default: 0 (C)\n"
        )
    )

    parser.add_argument(
        '--label', '-l',
        type=str,
        default='A1',
        help="Run label for export filename, e.g. A1, B2 (default: A1)"
    )

    parser.add_argument(
        '--no-export',
        action='store_true',
        help="Print playlist to terminal only, skip file export"
    )

    args = parser.parse_args()

    print_banner()
    print(f"  Run type : {args.type}  —  {RUN_TYPE_DESCRIPTIONS[args.type]}")
    print(f"  Start key: {KEY_NAMES[args.key]} ({args.key})")
    print(f"  Label    : {args.label}\n")

    print("Building playlist...\n")
    playlist = build_playlist(args.type, start_key=args.key)

    print_playlist(playlist)

    if not args.no_export:
        print("--- EXPORTING ---")
        export_playlist(playlist, run_type=args.type, run_label=args.label)

if __name__ == '__main__':
    main()
    