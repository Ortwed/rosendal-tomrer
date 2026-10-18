# Rosendal Tømrer – website

Statisk website for Rosendal Tømrer Entreprise ApS (rosendal-tomrer.dk).

- `docs/` – det færdige site (serveres af GitHub Pages)
- `src/` – Python-scripts der bygger sitet (`python3 src/build.py`) og tjekker det (`python3 src/verificer.py`)
- `FAKTATJEK.md` – det der skal bekræftes med Sebastian før go-live

**Demo-status:** `DEMO = True` i `src/site_shared.py` sætter noindex på alle sider. Sæt den til `False`, og udfyld `FORMSPREE_ID` og `GA_ID` ved go-live.

## Struktur (oktober 2026)
Hver side ligger som `/<slug>/index.html`. `python3 src/build.py` bygger testsiden i `docs/`, `python3 src/build.py --live` bygger `live/` og `rosendal-tomrer-live.zip` til Simply.com. Kør `python3 src/verificer.py` (`--live`) og `python3 src/skaermtest.py` før levering. Projekter (`PROJEKTER` i `build.py`) har status `pending` og vises først, når billeder og tekster er klar.
