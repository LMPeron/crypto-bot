from service.statistics import get_candle_stick
from datetime import datetime, timedelta
import json
import numpy
import talib


def get_stat_by_minute():
    try:
        #   date = datetime.now() + timedelta(minutes=-10)
        #   date_format = f"{datetime.timestamp(date)}".split(".")
        #   date_str = (
        #       date_format[0]
        #       + f"{date_format[1][0]}{date_format[1][1]}{date_format[1][2]}"
        #   )
        res = get_candle_stick("XECBUSD", "1m", "1628202599999")
        close_list = []
        if res:
            l = json.load(res)
            l_value = l[len(l) - 1][4]
            for i in l:
                close_list.append(float(i[4]))

            num_arr = numpy.array(close_list)

            return num_arr, l_value

        return [], -1
    except:
        raise Exception("Não foi possível obter Estatísiticas por minuto.")


def format_stats(close):
    rsi = talib.RSI(close, timeperiod=6)
    macd, macdsignal, macdhist = talib.MACD(
        close, fastperiod=12, slowperiod=26, signalperiod=9
    )

    r_rsi = rsi[len(rsi) - 1]
    r_dea = "%.8f" % (macd[len(macd) - 1])
    r_diff = "%.08f" % (macdsignal[len(macdsignal) - 1])
    r_macd = "%.08f" % (macdhist[len(macdhist) - 1])

    res = {"rsi": r_rsi, "dea": r_dea, "diff": r_diff, "macd": r_macd}
    return res
