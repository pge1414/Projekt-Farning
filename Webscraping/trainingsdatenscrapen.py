import yfinance as yf, tqdm, json

wörter = []


def get_performance(ticker_symbol, start_date, end_date):
    # Daten herunterladen
    ticker = yf.Ticker(ticker_symbol)
    df = ticker.history(start=start_date, end=end_date)
    
    if df.empty:
        return "Keine Daten für diesen Zeitraum gefunden."

    # Ersten und letzten Schlusskurs ermitteln
    start_price = df['Close'].iloc[0]
    end_price = df['Close'].iloc[-1]
    
    # Prozentualen Anstieg berechnen
    performance = ((end_price / start_price) - 1) * 100
    
    return performance

with open("indexe.json", "r") as f:
    for i in json.loads(f).values():
            wörter.append(str(i))


for w in tqdm.tqdm(wörter, desc="Verarbeitung läuft"):
    for i in range(20):
        for j in range(12):
            for k in range(3):    
                symbol = w
                start = f"{i}-{j}-{k*7}"
                end = f"{i}-{j}-{k*7+ 7}"

                pct_change = get_performance(symbol, start, end)
                print(f"Die Performance von {symbol} zwischen {start} und {end} betrug: {pct_change:.2f}%")

            
# Beispiel: Apple (AAPL) im Jahr 2023
# symbol = "AAPL"
# start = "2023-01-01"
# end = "2023-12-31"

pct_change = get_performance(symbol, start, end)
print(f"Die Performance von {symbol} zwischen {start} und {end} betrug: {pct_change:.2f}%")