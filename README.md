# Music Theory-Aware Running Playlist Generator

A Python tool that generates personalized running playlists using harmonic arc, 
circle-of-fifths key consistency, and arousal theory — validated against a 
BPM-only control in a self-experiment.

## How it works
Unlike existing apps (Spotify, RockMyRun) that match songs by BPM only, this tool 
uses music theory variables:
- Harmonic mode (major for effort phases, minor for grind phases)
- Circle-of-fifths key consistency (avoiding jarring key changes)
- Energy arc (songs ordered so tension builds toward the final kilometer)

## Modules
- module1.py — Song fetcher and filter engine
- module2.py — Music theory rules and run arc definitions
- module3.py — Playlist builder with key-consistency enforcement
- module4.py — Session logger and playlist exporter

## Run types supported
- Easy run
- Tempo run
- 5K race
