import http.client

def get_ping():
      conn = http.client.HTTPSConnection("api.binance.com")
      payload = ''
      headers = {}
      conn.request("GET", "/api/v3/ping", payload, headers)
      res = conn.getresponse()
      data = res.read()
      return data


def get_server_time():
      conn = http.client.HTTPSConnection("api.binance.com")
      payload = ''
      headers = {}
      conn.request("GET", "/api/v3/time", payload, headers)
      res = conn.getresponse()
      
      return res




