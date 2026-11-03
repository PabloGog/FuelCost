# Fuel Cost Calculator

Work out the fuel cost of a car trip and split it between passengers.

There are two versions:

| Version | Files | How to run |
|---|---|---|
| Web app (installable on a phone) | `index.html`, `service-worker.js`, `manifest.webmanifest`, `fuel-icon.svg` | Open `index.html` in a browser, or host the folder (e.g. GitHub Pages) and choose "Add to Home Screen" |
| Desktop app (Windows) | `fuel_cost.py`, `fuel_cost.bat` | Double-click `fuel_cost.bat` |

The web app remembers the last values on the device, picks a default currency from the device region, and has a Share button. Offline use and phone install need it served over HTTPS; opened as a local file it still calculates.

## Desktop setup

Needs Python 3.10+ with tkinter (included in the python.org Windows installer).

```bat
git clone https://github.com/PabloGog/FuelCost.git
cd FuelCost
setup_venv.bat
fuel_cost.bat
```

`setup_venv.bat` creates `.venv` and installs `requirements.txt` (currently empty: the app uses only the standard library). `fuel_cost.bat` uses `.venv` if it exists, otherwise the system Python.

## Releasing a web-app change

Bump `CACHE_NAME` in `service-worker.js` (e.g. `fuel-cost-v8` to `fuel-cost-v9`) so installed copies pick up the new files.
