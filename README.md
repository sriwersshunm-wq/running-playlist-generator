# Music Theory-Aware Running Playlist Generator

Every running playlist app matches songs by BPM and nothing else. This tool does more — it uses music theory to build playlists the way a composer structures a piece, with an intentional harmonic arc from start to finish.

The three things it adds on top of BPM matching:
- **Mode** — minor keys during the hardest effort phases, major keys during warmup and kick, based on how mode affects arousal and perceived effort
- **Key consistency** — song transitions are restricted to adjacent keys on the circle of fifths so there are no jarring key changes mid-run that break flow state
- **Energy arc** — harmonic tension builds toward the final kilometer instead of songs being shuffled randomly

I built this after getting frustrated that Spotify's running mixes felt musically random even when the tempos were right.

---

## How to use it

```bash
python main.py --type 5k_race --key 0 --label A1
python main.py --type easy --key 7 --label B1
python main.py --type tempo --key 5 --no-export
python main.py --help
```

Run types: `easy`, `tempo`, `5k_race`

Key is a number 0–11 (0=C, 1=C#, 2=D, 3=Eb, 4=E, 5=F, 6=F#, 7=G, 8=Ab, 9=A, 10=Bb, 11=B)

It outputs two files — a readable breakdown of the playlist by phase, and a Spotify URI list you can paste into [spotifyplaylist.net](https://www.spotifyplaylist.net/) to build the actual playlist.

---

## How the arc works (5K race example)

The 5K arc has five phases: warmup (130–140 BPM, major), build (145–158 BPM, major), grind (150–175 BPM, minor), kick (168–186 BPM, major), cooldown (110–125 BPM, major).

The switch to minor during the grind is intentional — minor mode increases effort tolerance during the hardest segment. The return to major at maximum BPM for the kick creates a psychological release. Each phase picks songs in keys adjacent to the previous phase's ending key so the transitions stay smooth.

---

## Song database

85 songs in `songs.csv`, all manually verified for BPM, key, and mode on Tunebat. Genre is mostly pop/hip-hop/R&B — The Weeknd, Drake, Travis Scott, Kendrick Lamar, Post Malone, Imagine Dragons, Eminem, Harry Styles, and others.

---

## Validation

I ran three sessions comparing theory-aware playlists against a random playlist control, logging pace, heart rate, RPE (1–10), and flow score (1–10) after each run.

| Condition | Avg Pace | Avg HR | Avg RPE | Avg Flow |
|-----------|----------|--------|---------|----------|
| Theory-aware (n=2) | 7:52/mi | 165 BPM | 4.5 | 8.0 |
| Control (n=1) | 8:38/mi | 164 BPM | 3.0 | 6.0 |

HR was nearly identical across all three runs, meaning the physiological load was the same. Theory-aware runs were 46 seconds per mile faster on average, and flow score was 2 points higher. Results from all sessions are in `validation_data.csv` and can be reproduced by running `python analysis.py`.

---

## Limitations and next steps

This is a small self-experiment — 3 runs, 1 subject — so the results are interesting but not statistically conclusive. The control run was also longer than the theory-aware runs, so pace is used as the main comparison metric rather than total distance. A proper follow-up would test multiple subjects over more sessions, and add a third condition that matches BPM but randomizes key and mode, to isolate the music theory effect specifically.

The Spotify API is also currently restricted for new apps, so playlists are exported as URI lists for manual import rather than created automatically.

---

## Project structure

```
running-playlist-generator/
├── main.py              # CLI entry point
├── module1.py           # Song database + filter engine
├── module2.py           # Music theory rules + run arc definitions
├── module3.py           # Playlist builder
├── module4.py           # Exporter + session logger
├── analysis.py          # Validation data analysis
├── songs.csv            # 85-track song database
└── validation_data.csv  # Logged run sessions
```

---

## Requirements

```
pip install pandas
```
