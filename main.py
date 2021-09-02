import numpy
from service.utils import get_ping, get_server_time
from service.statistics import get_candle_stick
import time
from utils.market.klines import get_stat_by_minute, format_stats
from service.order import buy_market_order, sell_market_order
import json


def main():
    bought = False
    bought_price = 0
    quantity_bought = 0

    while True:
        close, b_val = get_stat_by_minute()
        quantity = int(round(20 / float(b_val), 3))
        stats = format_stats(close)
        f = open("log.txt", "a")

        if stats["rsi"] < 30 and (stats["diff"] > stats["macd"]) and bought == False:
            print("Compra -->" + b_val)
            bought = True
            f.writelines([f"Comprado em --> {b_val}\n"])
            quantity_bought = quantity
            bought_price = b_val
            print(quantity)
            t = get_server_time()
            tm = json.load(t)["serverTime"]
            print(
                json.load(
                    buy_market_order(
                        timestamp=tm,
                        api_key="",
                        secret="",
                        quantity=quantity,
                    )
                )
            )

        if stats["rsi"] > 70 and bought == True and b_val > bought_price:
            print("Vende -->" + b_val)
            bought = False
            f.writelines([f"Vendido em --> {b_val}\n"])
            f.writelines(["---------------------\n"])
            print(quantity_bought)
            t = get_server_time()
            tm = json.load(t)["serverTime"]
            print(
                json.load(
                    sell_market_order(
                        timestamp=tm,
                        api_key="",
                        secret="",
                        quantity=quantity_bought,
                    )
                )
            )

        time.sleep(1)


main()
