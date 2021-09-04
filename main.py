from service.utils import get_server_time
import time
from utils.market.klines import get_stat_by_minute, format_stats
from service.order import buy_market_order, sell_market_order
import json
from datetime import date, datetime

def main():
    bought = False
    bought_price = 0
    quantity_bought = 0
    start(bought=bought, bought_price=bought_price, quantity_bought=quantity_bought)


def start(bought, bought_price, quantity_bought):
    while True:
        try:
            close, b_val = get_stat_by_minute()
            quantity = int(round(14 / float(b_val), 3))
            stats = format_stats(close)
            f = open("log.txt", "a")

            # and (stats["diff"] > stats["macd"])
            if stats["rsi"] < 30 and bought == False:
                print("Compra -->" + b_val)
                bought = True
                f.writelines([f"Comprado em --> {b_val}"])
                f.writelines([f" || as --> {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}\n"])
                quantity_bought = quantity
                bought_price = b_val
                print(quantity)
                t = get_server_time()
                tm = json.load(t)["serverTime"]
                print(
                    json.load(
                        buy_market_order(
                            timestamp=tm,
                            api_key="5oGo1UeJhwe2wuZqhrsNPF75RtE0mvfhnC8nT9qzcmJiyq7OsBYXmeRqbeg3aa79",
                            secret="9eGhTaIMRE70jLnaBb118j1N1WNCfafmV3V5OV8BeqEM0XZ9KDTBaTh9YelFB5oB",
                            quantity=quantity,
                            price=b_val
                        )
                    )
                )

            if stats["rsi"] > 70 and bought == True and b_val > bought_price:
                print("Vende -->" + b_val)
                bought = False
                f.writelines([f"Vendido  em --> {b_val}"])
                f.writelines([f" || as --> {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}\n"])
                f.writelines(["---------------------\n\n"])
                print(quantity_bought)
                t = get_server_time()
                tm = json.load(t)["serverTime"]
                print(
                    json.load(
                        sell_market_order(
                            timestamp=tm,
                            api_key="5oGo1UeJhwe2wuZqhrsNPF75RtE0mvfhnC8nT9qzcmJiyq7OsBYXmeRqbeg3aa79",
                            secret="9eGhTaIMRE70jLnaBb118j1N1WNCfafmV3V5OV8BeqEM0XZ9KDTBaTh9YelFB5oB",
                            quantity=quantity_bought,
                            price=b_val
                        )
                    )
                )


            print("Conectado.")
            time.sleep(2)
        except:
            print("Desconectado.")
            time.sleep(2)
            start(bought, bought_price, quantity_bought)

main()
