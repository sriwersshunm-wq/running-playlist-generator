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

The 5K arc has five phases: warmup (130–140 BPM, major), build (145–158 BPM, major), grind (155–167 BPM, minor), kick (168–186 BPM, major), cooldown (110–125 BPM, major).

The switch to minor during the grind is intentional — minor mode increases effort tolerance during the hardest segment. The return to major at maximum BPM for the kick creates a psychological release. Each phase picks songs in keys adjacent to the previous phase's ending key so the transitions stay smooth.

---

## Song database

81 songs in `songs.csv`, all manually verified for BPM, key, and mode. Genre is mostly pop/hip-hop/R&B — The Weeknd, Drake, Travis Scott, Kendrick Lamar, Post Malone, Imagine Dragons, Eminem, Harry Styles, and others.

---

## Validation

I ran three sessions comparing theory-aware playlists against BPM-only control sessions, logging pace, heart rate, RPE (1–10), and flow score (1–10) after each run. Run 1 (easy, theory-aware) gave a flow score of 8 and RPE of 3.0 — the kick phase caused a spontaneous pace increase despite low perceived effort, which was the first sign the harmonic structure was doing something.

Results from all three runs are in `validation_data.csv`.

---

## Project structure

```
running-playlist-generator/
├── main.py              # CLI entry point
├── module1.py           # Song database + filter engine
├── module2.py           # Music theory rules + run arc definitions
├── module3.py           # Playlist builder
├── module4.py           # Exporter + session logger
├── songs.csv            # 81-track song database
└── validation_data.csv  # Logged run sessions
```

---

## Requirements

```
pip install pandas
```
