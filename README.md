# Rosendal Tømrer – website

Statisk website for Rosendal Tømrer Entreprise ApS (rosendal-tomrer.dk).

- `docs/` – det færdige site (serveres af GitHub Pages)
- `src/` – Python-scripts der bygger sitet (`python3 src/build.py`) og tjekker det (`python3 src/verificer.py`)
- `FAKTATJEK.md` – det der skal bekræftes med Sebastian før go-live

**Demo-status:** `DEMO = True` i `src/site_shared.py` sætter noindex på alle sider. Sæt den til `False`, og udfyld `FORMSPREE_ID` og `GA_ID` ved go-live.
