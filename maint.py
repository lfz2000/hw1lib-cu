from hw1lib import AUDUSD_return
from hw1lib import GBPEUR_return
from hw1lib import USDCAD_return
from hw1lib import USDJPY_return
from hw1lib import USDMXN_return
from hw1lib import EURUSD_return
from hw1lib import USDCNY_return
from hw1lib import USDCZK_return
from hw1lib import USDPLN_return
from hw1lib import USDINR_return


ts1 = AUDUSD_return(1,10)
ts2 = GBPEUR_return(1,10)
ts3 = USDCAD_return(1,10)
ts4 = USDJPY_return(1,10)
ts5 = USDMXN_return(1,10)
ts6 = EURUSD_return(1,10)
ts7 = USDCNY_return(1,10)
ts8 = USDCZK_return(1,10)
ts9 = USDPLN_return(1,10)
ts10 = USDINR_return(1,10)





print(ts1.last_price)
print(ts2.last_price)
print(ts3.last_price)
print(ts4.last_price)
print(ts5.last_price)
print(ts6.last_price)
print(ts7.last_price)
print(ts8.last_price)
print(ts9.last_price)
print(ts10.last_price)