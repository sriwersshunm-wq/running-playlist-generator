# Music Theory-Aware Running Playlist Generator

A Python tool that generates personalized running playlists using harmonic arc design, circle-of-fifths key consistency, and mode-based arousal theory — validated against BPM-only control sessions in a self-experiment.

Most existing running playlist tools (Spotify, RockMyRun) match songs by tempo alone. This project introduces three additional music theory variables:

- **Harmonic mode** — minor keys during high-effort grind phases, major keys during warmup and kick phases, based on the established link between mode and emotional arousal
- **Energy arc** — songs ordered so harmonic tension builds toward the final kilometer, the way a composer constructs a symphony
- **Key consistency** — transitions restricted to adjacent keys on the circle of fifths, avoiding jarring modulations that research suggests break flow state

---

## How It Works

The tool is built across four modules:

**module1.py** — Song database interface. Filters the local CSV dataset by BPM range, key, mode, energy, and valence to return candidate tracks for each phase.

**module2.py** — Music theory rules engine. Defines the circle-of-fifths adjacency map and the run arc templates (easy, tempo, 5K race). Each arc is a sequence of phases with target BPM ranges, modes, and energy windows.

**module3.py** — Playlist builder. Walks through each phase of the arc, queries the song database with circle-of-fifths key constraints, fills the phase duration, and updates the current key for the next phase.

**module4.py** — Export and logging. Outputs a human-readable playlist breakdown and a Spotify URI list for importing. Logs validation run data (pace, HR, RPE, flow score) to CSV for statistical analysis.

---

## Run Arc Design

### 5K Race Arc
| Phase    | BPM Range | Mode  | Duration |
|----------|-----------|-------|----------|
| Warmup   | 130–140   | Major | 5 min    |
| Build    | 145–158   | Major | 7 min    |
| Grind    | 155–167   | Minor | 6 min    |
| Kick     | 168–186   | Major | 3 min    |
| Cooldown | 110–125   | Major | 9 min    |

The shift from major → minor → major across the grind and kick phases is intentional: minor mode increases perceived effort tolerance during the hardest segment, while the return to major at maximum BPM during the kick creates a psychological release that research associates with sprint performance.

### Easy Run Arc
| Phase | BPM Range | Mode  | Duration |
|-------|-----------|-------|----------|
| Main  | 125–145   | Major | 40 min   |

### Tempo Run Arc
| Phase    | BPM Range | Mode  | Duration |
|----------|-----------|-------|----------|
| Warmup   | 130–140   | Major | 10 min   |
| Grind    | 155–168   | Minor | 25 min   |
| Cooldown | 110–125   | Major | 10 min   |

---

## Usage

```bash
# Full 5K race playlist starting in C
python main.py --type 5k_race --key 0 --label A2

# Easy run starting in G
python main.py --type easy --key 7 --label B1

# Tempo run, print only (no file export)
python main.py --type tempo --key 5 --no-export

# Show all options
python main.py --help
```

**Key reference:** 0=C, 1=C#, 2=D, 3=Eb, 4=E, 5=F, 6=F#, 7=G, 8=Ab, 9=A, 10=Bb, 11=B

The tool exports two files per run:
- `playlist_[type]_[label]_[timestamp]_readable.txt` — phase-by-phase breakdown with BPM, key, mode, and energy for each track
- `playlist_[type]_[label]_[timestamp]_spotify_uris.txt` — paste into [spotifyplaylist.net](https://www.spotifyplaylist.net/) to build the Spotify playlist instantly

---

## Song Database

The dataset (`songs.csv`) contains 81 tracks sourced manually and verified against Tunebat for BPM, key, and mode accuracy. Each track includes:

| Column     | Description                          |
|------------|--------------------------------------|
| name       | Track title                          |
| artist     | Artist name                          |
| spotify_id | Spotify track ID                     |
| bpm        | Tempo in beats per minute            |
| key        | Pitch class (0–11, Spotify standard) |
| mode       | 1 = Major, 0 = Minor                 |
| energy     | Perceived energy (0.0–1.0)           |
| valence    | Musical positivity (0.0–1.0)         |

Genre: pop, hip-hop, R&B (The Weeknd, Drake, Travis Scott, Kendrick Lamar, Post Malone, Imagine Dragons, Eminem, Harry Styles, and others).

---

## Validation

The tool was validated in a self-experiment comparing theory-aware playlists against BPM-only control sessions across three runs. Metrics logged per session:

- Total time and final mile pace
- Mean heart rate per mile
- Mean RPE (Rate of Perceived Exertion, Borg 1–10 scale)
- Flow score (self-reported 1–10)

Data is logged automatically via `log_session()` in module4.py to `validation_data.csv`.

**Preliminary result (Run 1):** Theory-aware playlist produced a flow score of 8/10 with RPE of 3.0 on an easy run. The kick phase caused a spontaneous pace increase despite low perceived effort, suggesting the major-key BPM spike has measurable behavioral effect even at easy intensity.

---

## Research Angle

This project sits at the intersection of computer engineering, music theory, and sports science — three domains that are rarely combined in applied software. The core hypothesis is that harmonic structure, not just tempo, influences running performance through psychological arousal and flow state maintenance.

The music theory backbone (circle of fifths, mode-arousal theory, harmonic tension arcs) was encoded manually from Grade 5 music theory knowledge, then operationalized as a filtering and sequencing algorithm. The validation loop treats each run as an experimental trial, making this a software engineering project with a self-experiment research design.

---

## Project Structure

```
running-playlist-generator/
├── main.py              # CLI entry point
├── module1.py           # Song database interface
├── module2.py           # Music theory rules engine
├── module3.py           # Playlist builder
├── module4.py           # Export and session logger
├── songs.csv            # 81-track verified song database
└── validation_data.csv  # Logged run sessions
```

---

## Requirements

```
pandas
```

Install with:
```bash
pip install pandas
```
