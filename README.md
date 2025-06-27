
# PV Forecast – Data Science Challenge (neoom, 2025)

This repository contains a small end-to-end solution to forecast photovoltaic production for a given timestamp using a scikit-learn model, served via FastAPI.

## Features

- Gradient Boosting model (703 kB `.pkl`)
- API with `/forecast?date=...` endpoint
- Docker-ready
- [CI only in repo with `-ci` suffix]

## Quickstart (with Docker)

```bash
docker build -t pv-forecast .
docker run --rm -p 5000:5000 pv-forecast
# → http://localhost:5000/docs
```

## Project structure

- `app/` – FastAPI app
- `model/` – pretrained scikit-learn model
- `notebooks/` – development & EDA notebook
- `tests/` – basic pytest for CI

## License

MIT – use freely for learning and demonstration.
