from service.utils import get_server_time
import time
from utils.market.klines import get_stat_by_minute, format_stats
from service.order import buy_market_order, sell_market_order
import json
from datetime import date, datetime

def main():
    start(bought=False, bought_price=0, quantity_bought=0)


def start(bought, bought_price, quantity_bought):
    while True:
        try:
            close, b_val = get_stat_by_minute()
            quantity = int(round(20 / float(b_val), 3))
            stats = format_stats(close)
            # f = open("log.txt", "a")

            # and (stats["diff"] > stats["macd"])
            if stats["rsi"] < 60 and bought == False:
                print("Compra -->" + b_val)
                bought = True
                # f.writelines([f"Comprado em --> {b_val}"])
                # f.writelines([f" || as --> {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}\n"])
                quantity_bought = quantity
                bought_price = b_val
                print(quantity)

                # formatted_price = "{:.6f}".format(float(b_val))
                # print(formatted_price)

                t = get_server_time()
                tm = json.load(t)["serverTime"]
                print(
                    json.load(
                        buy_market_order(
                            timestamp=tm,
                            api_key="DAePl6JzIE2K92vHGHucJcC0ZiwDLPlefxVDwr1QW91NpB9mpQAgExTNijHCNR6s",
                            secret="euqAsojeNQOTTBZigHp1H4SloIFKVc0A9IZ9KtibSn7Slv77ChBK5a4WEliGhObD",
                            quantity=quantity,
                            # price=formatted_price
                        )
                    )
                )

            if stats["rsi"] > 60 and bought == True: #and b_val > bought_price:
                print("Vende -->" + b_val)
                bought = False
                # f.writelines([f"Vendido  em --> {b_val}"])
                # f.writelines([f" || as --> {datetime.now().strftime('%m/%d/%Y, %H:%M:%S')}\n"])
                # f.writelines(["---------------------\n\n"])


                quantity_bought = int(quantity_bought - quantity_bought * 0.01) + 1


                # formatted_price = "{:.6f}".format(float(b_val))
                # print(formatted_price)

                print(
                    json.load(
                        sell_market_order(
                            timestamp=tm,
                            api_key="DAePl6JzIE2K92vHGHucJcC0ZiwDLPlefxVDwr1QW91NpB9mpQAgExTNijHCNR6s",
                            secret="euqAsojeNQOTTBZigHp1H4SloIFKVc0A9IZ9KtibSn7Slv77ChBK5a4WEliGhObD",
                            quantity=quantity_bought,
                            # price=formatted_price
                        )
                    )
                )


            print("Conectado.")
            time.sleep(2)
        except Exception as e:
            print(e)
            time.sleep(2)
            break
    start(bought=bought, bought_price=bought_price, quantity_bought=quantity_bought)

main()
