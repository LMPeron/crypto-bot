import http.client


def get_candle_stick(symbol, interval, start_time):
      conn = http.client.HTTPSConnection("api.binance.com")
      payload = ''
      headers = {}

      interval = f"&interval={interval}" if interval is not None else ""
      symbol = f"&symbol={symbol}" if symbol is not None else ""
      start_time = f"&startTime={start_time}" if start_time is not None else ""
      conn.request("GET", f"/api/v3/klines?{interval}{symbol}", payload, headers)
      return conn.getresponse()