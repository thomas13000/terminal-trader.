from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import asyncio

app = FastAPI(title="Terminal Trader Pro — Hub Central")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

# Exemple d'API endpoint pour centraliser Finviz / Bloomberg plus tard
@app.get("/api/market-feed")
async def get_market_feed():
    return {
        "status": "online",
        "tickers": {
            "BTCUSDT": {"price": 96840.50, "change": 3.64},
            "US100": {"price": 21240.10, "change": 1.12},
            "XAUUSD": {"price": 2688.30, "change": 0.84}
        },
        "news": [
            {"source": "BLOOMBERG", "title": "Fed Signals Rate Pause Amid Inflation Data", "time": "14:32"},
            {"source": "FINVIZ", "title": "Tech Sector Leads Midday Rally", "time": "14:15"}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
