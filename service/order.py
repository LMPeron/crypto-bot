import http.client
import hmac
import hashlib

def buy_market_order(timestamp, api_key, secret, quantity):
    conn = http.client.HTTPSConnection("api.binance.com")
    payload = ""
    headers = {"Content-Type": "application/json", "X-MBX-APIKEY": api_key}
    query_string = f'symbol=XECBUSD&side=BUY&quantity={quantity}&type=MARKET&timestamp={timestamp}'
    signature = hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    conn.request(
        "POST",
        '/api/v3/order/test?' + query_string + f'&signature={signature}',
        payload,
        headers,
    )
    res = conn.getresponse()
    return res


def sell_market_order(timestamp, api_key, secret, quantity):
    conn = http.client.HTTPSConnection("api.binance.com")
    payload = ""
    headers = {"Content-Type": "application/json", "X-MBX-APIKEY": api_key}
    query_string = f'symbol=XECBUSD&side=SELL&quantity={quantity}&type=MARKET&timestamp={timestamp}'
    signature = hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    conn.request(
        "POST",
        '/api/v3/order/test?' + query_string + f'&signature={signature}',
        payload,
        headers,
    )
    res = conn.getresponse()
    return res



def send_signed_request(http_method, url_path, payload={}):
    query_string = urlencode(payload, True)
    if query_string:
        query_string = "{}&timestamp={}".format(query_string, get_timestamp())
    else:
        query_string = 'timestamp={}'.format(get_timestamp())

    url = BASE_URL + url_path + '?' + query_string + '&signature=' + hashing(query_string)
    print("{} {}".format(http_method, url))
    params = {'url': url, 'params': {}}
    response = dispatch_request(http_method)(**params)
    return response.json()