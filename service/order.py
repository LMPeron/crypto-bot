import http.client
import hmac
import hashlib

def buy_market_order(timestamp, api_key, secret, quantity):
    conn = http.client.HTTPSConnection("api.binance.com")
    payload = ""
    headers = {"Content-Type": "application/json", "X-MBX-APIKEY": api_key}
    query_string = f'symbol=BTTBUSD&side=BUY&quantity={quantity}&type=MARKET&timestamp={timestamp}'
    signature = hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    conn.request(
        "POST",
        '/api/v3/order?' + query_string + f'&signature={signature}',
        payload,
        headers,
    )
    res = conn.getresponse()
    return res


def sell_market_order(timestamp, api_key, secret, quantity):
    conn = http.client.HTTPSConnection("api.binance.com")
    payload = ""
    headers = {"Content-Type": "application/json", "X-MBX-APIKEY": api_key}
    query_string = f'symbol=BTTBUSD&side=SELL&quantity={quantity}&type=MARKET&timestamp={timestamp}'
    signature = hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    conn.request(
        "POST",
        '/api/v3/order?' + query_string + f'&signature={signature}',
        payload,
        headers,
    )
    res = conn.getresponse()
    return res


def buy_limit_order(timestamp, api_key, secret, quantity, price):
    conn = http.client.HTTPSConnection("api.binance.com")
    payload = ""
    headers = {"Content-Type": "application/json", "X-MBX-APIKEY": api_key}
    query_string = f'symbol=BTTBUSD&side=BUY&quantity={quantity}&timeInForce=IOC&price={price}&type=LIMIT&timestamp={timestamp}'
    signature = hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    conn.request(
        "POST",
        '/api/v3/order?' + query_string + f'&signature={signature}',
        payload,
        headers,
    )
    res = conn.getresponse()
    return res


def sell_limit_order(timestamp, api_key, secret, quantity, price):
    conn = http.client.HTTPSConnection("api.binance.com")
    payload = ""
    headers = {"Content-Type": "application/json", "X-MBX-APIKEY": api_key}
    query_string = f'symbol=BTTBUSD&side=SELL&quantity={quantity}&timeInForce=IOC&price={price}&type=LIMIT&timestamp={timestamp}'
    signature = hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    conn.request(
        "POST",
        '/api/v3/order/test?' + query_string + f'&signature={signature}',
        payload,
        headers,
    )
    res = conn.getresponse()
    return res


