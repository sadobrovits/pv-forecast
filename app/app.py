import joblib, numpy as np, pandas as pd
from fastapi import FastAPI
from datetime import datetime, timezone
from pydantic import BaseModel

ART = joblib.load("pv_gbr.pkl")
MODEL  = ART["model"]
FEATS  = ART["features"]

app = FastAPI(title="PV-Forecast API")

class ForecastOut(BaseModel):
    datetime_utc: datetime
    pv_kw: float

@app.get("/forecast", response_model=ForecastOut)
def forecast(date: datetime):
    idx = pd.Timestamp(date, tz="UTC").tz_convert(None)

    X = pd.DataFrame(index=[idx])
    X["lag_96"]  = MODEL[0].mean_[0]
    X["lag_192"] = MODEL[0].mean_[0]
    X["sin_hour"] = np.sin(2*np.pi*idx.hour/24)
    X["cos_hour"] = np.cos(2*np.pi*idx.hour/24)
    doy = idx.dayofyear
    X["sin_doy"]  = np.sin(2*np.pi*doy/365.25)
    X["cos_doy"]  = np.cos(2*np.pi*doy/365.25)
    X = X[FEATS]

    pv_kw = float(max(MODEL.predict(X)[0], 0))
    return ForecastOut(datetime_utc=idx, pv_kw=round(pv_kw, 3))
