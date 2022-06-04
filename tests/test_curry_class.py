from cmath import sqrt
import sys
sys.path.append("..")
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
import unittest
from math import sqrt

#Test Case, just for the simulation.
class CurrencyTestCase1(unittest.TestCase):
    def setUp(self):
        self.curry1 = AUDUSD_return(1,10)
        self.curry2 = AUDUSD_return(2,20)
        self.curry3 = AUDUSD_return(3,30)
        self.curry4 = AUDUSD_return(4,40)
        self.curry5 = AUDUSD_return(5,50)
        self.curry6 = AUDUSD_return(6,60)

    def test_num(self):
        self.assertEqual(5,AUDUSD_return.num)
        AUDUSD_return.num=0
        AUDUSD_return.run_sum=0
        AUDUSD_return.run_squared_sum=0
        AUDUSD_return.run_sum_of_std=0
        AUDUSD_return.last_price=-1
    
    def test_run_sum(self):
        self.assertEqual(1+1/2+1/3+1/4+1/5,AUDUSD_return.run_sum)
        AUDUSD_return.num=0
        AUDUSD_return.run_sum=0
        AUDUSD_return.run_squared_sum=0
        AUDUSD_return.run_sum_of_std=0
        AUDUSD_return.last_price=-1

    def test_run_squared_sum(self):
        self.assertEqual(0,AUDUSD_return.run_squared_sum)
        AUDUSD_return.num=0
        AUDUSD_return.run_sum=0
        AUDUSD_return.run_squared_sum=0
        AUDUSD_return.run_sum_of_std=0
        AUDUSD_return.last_price=-1

    def test_run_sum_of_std(self):
        self.assertEqual(0,AUDUSD_return.run_sum_of_std)
        AUDUSD_return.num=0
        AUDUSD_return.run_sum=0
        AUDUSD_return.run_squared_sum=0
        AUDUSD_return.run_sum_of_std=0
        AUDUSD_return.last_price=-1

    def test_last_price(self):
        x = self.curry6.last_price
        self.assertEqual(x,AUDUSD_return.last_price)
        AUDUSD_return.num=0
        AUDUSD_return.run_sum=0
        AUDUSD_return.run_squared_sum=0
        AUDUSD_return.run_sum_of_std=0
        AUDUSD_return.last_price=-1
   
    def test_get_avg(self):
        x = self.curry6.get_avg(0.5)
        self.assertEqual(1+1/2+1/3+1/4+1/5-1/2,AUDUSD_return.run_sum)
        self.assertEqual(x,AUDUSD_return.run_sum/(AUDUSD_return.num))
        AUDUSD_return.num=0
        AUDUSD_return.run_sum=0
        AUDUSD_return.run_squared_sum=0
        AUDUSD_return.run_sum_of_std=0
        AUDUSD_return.last_price=-1

    def test_add_to_running_squared_sum(self):
        self.curry6.add_to_running_squared_sum(0.1)
        self.assertEqual(AUDUSD_return.run_squared_sum,(0.2-0.1)**2)
        AUDUSD_return.num=0
        AUDUSD_return.run_sum=0
        AUDUSD_return.run_squared_sum=0
        AUDUSD_return.run_sum_of_std=0
        AUDUSD_return.last_price=-1

    def test_get_std(self):
        self.curry6.add_to_running_squared_sum(0.1)
        x = self.curry6.get_std()
        self.assertEqual(x,sqrt(((0.2-0.1)**2)/5))
        AUDUSD_return.num=0
        AUDUSD_return.run_sum=0
        AUDUSD_return.run_squared_sum=0
        AUDUSD_return.run_sum_of_std=0
        AUDUSD_return.last_price=-1

    def test_get_avg_std(self):
        x = self.curry6.get_avg_std(10)
        self.assertEqual(x,-2.0)
        AUDUSD_return.num=0
        AUDUSD_return.run_sum=0
        AUDUSD_return.run_squared_sum=0
        AUDUSD_return.run_sum_of_std=0
        AUDUSD_return.last_price=-1

class CurrencyTestCase2(unittest.TestCase):
    def setUp(self):
        self.curry1 = GBPEUR_return(1,10)
        self.curry2 = GBPEUR_return(2,20)
        self.curry3 = GBPEUR_return(3,30)
        self.curry4 = GBPEUR_return(4,40)
        self.curry5 = GBPEUR_return(5,50)
        self.curry6 = GBPEUR_return(6,60)

    def test_num(self):
        self.assertEqual(5,GBPEUR_return.num)
        GBPEUR_return.num=0
        GBPEUR_return.run_sum=0
        GBPEUR_return.run_squared_sum=0
        GBPEUR_return.run_sum_of_std=0
        GBPEUR_return.last_price=-1
    
    def test_run_sum(self):
        self.assertEqual(1+1/2+1/3+1/4+1/5,GBPEUR_return.run_sum)
        GBPEUR_return.num=0
        GBPEUR_return.run_sum=0
        GBPEUR_return.run_squared_sum=0
        GBPEUR_return.run_sum_of_std=0
        GBPEUR_return.last_price=-1

    def test_run_squared_sum(self):
        self.assertEqual(0,GBPEUR_return.run_squared_sum)
        GBPEUR_return.num=0
        GBPEUR_return.run_sum=0
        GBPEUR_return.run_squared_sum=0
        GBPEUR_return.run_sum_of_std=0
        GBPEUR_return.last_price=-1

    def test_run_sum_of_std(self):
        self.assertEqual(0,GBPEUR_return.run_sum_of_std)
        GBPEUR_return.num=0
        GBPEUR_return.run_sum=0
        GBPEUR_return.run_squared_sum=0
        GBPEUR_return.run_sum_of_std=0
        GBPEUR_return.last_price=-1

    def test_last_price(self):
        x = self.curry6.last_price
        self.assertEqual(x,GBPEUR_return.last_price)
        GBPEUR_return.num=0
        GBPEUR_return.run_sum=0
        GBPEUR_return.run_squared_sum=0
        GBPEUR_return.run_sum_of_std=0
        GBPEUR_return.last_price=-1
   
    def test_get_avg(self):
        x = self.curry6.get_avg(0.5)
        self.assertEqual(1+1/2+1/3+1/4+1/5-1/2,GBPEUR_return.run_sum)
        self.assertEqual(x,GBPEUR_return.run_sum/(GBPEUR_return.num))
        GBPEUR_return.num=0
        GBPEUR_return.run_sum=0
        GBPEUR_return.run_squared_sum=0
        GBPEUR_return.run_sum_of_std=0
        GBPEUR_return.last_price=-1

    def test_add_to_running_squared_sum(self):
        self.curry6.add_to_running_squared_sum(0.1)
        self.assertEqual(GBPEUR_return.run_squared_sum,(0.2-0.1)**2)
        GBPEUR_return.num=0
        GBPEUR_return.run_sum=0
        GBPEUR_return.run_squared_sum=0
        GBPEUR_return.run_sum_of_std=0
        GBPEUR_return.last_price=-1

    def test_get_std(self):
        self.curry6.add_to_running_squared_sum(0.1)
        x = self.curry6.get_std()
        self.assertEqual(x,sqrt(((0.2-0.1)**2)/5))
        GBPEUR_return.num=0
        GBPEUR_return.run_sum=0
        GBPEUR_return.run_squared_sum=0
        GBPEUR_return.run_sum_of_std=0
        GBPEUR_return.last_price=-1

    def test_get_avg_std(self):
        x = self.curry6.get_avg_std(10)
        self.assertEqual(x,-2.0)
        GBPEUR_return.num=0
        GBPEUR_return.run_sum=0
        GBPEUR_return.run_squared_sum=0
        GBPEUR_return.run_sum_of_std=0
        GBPEUR_return.last_price=-1

class CurrencyTestCase3(unittest.TestCase):
    def setUp(self):
        self.curry1 = USDCAD_return(1,10)
        self.curry2 = USDCAD_return(2,20)
        self.curry3 = USDCAD_return(3,30)
        self.curry4 = USDCAD_return(4,40)
        self.curry5 = USDCAD_return(5,50)
        self.curry6 = USDCAD_return(6,60)

    def test_num(self):
        self.assertEqual(5,USDCAD_return.num)
        USDCAD_return.num=0
        USDCAD_return.run_sum=0
        USDCAD_return.run_squared_sum=0
        USDCAD_return.run_sum_of_std=0
        USDCAD_return.last_price=-1
    
    def test_run_sum(self):
        self.assertEqual(1+1/2+1/3+1/4+1/5,USDCAD_return.run_sum)
        USDCAD_return.num=0
        USDCAD_return.run_sum=0
        USDCAD_return.run_squared_sum=0
        USDCAD_return.run_sum_of_std=0
        USDCAD_return.last_price=-1

    def test_run_squared_sum(self):
        self.assertEqual(0,USDCAD_return.run_squared_sum)
        USDCAD_return.num=0
        USDCAD_return.run_sum=0
        USDCAD_return.run_squared_sum=0
        USDCAD_return.run_sum_of_std=0
        USDCAD_return.last_price=-1

    def test_run_sum_of_std(self):
        self.assertEqual(0,USDCAD_return.run_sum_of_std)
        USDCAD_return.num=0
        USDCAD_return.run_sum=0
        USDCAD_return.run_squared_sum=0
        USDCAD_return.run_sum_of_std=0
        USDCAD_return.last_price=-1

    def test_last_price(self):
        x = self.curry6.last_price
        self.assertEqual(x,USDCAD_return.last_price)
        USDCAD_return.num=0
        USDCAD_return.run_sum=0
        USDCAD_return.run_squared_sum=0
        USDCAD_return.run_sum_of_std=0
        USDCAD_return.last_price=-1
   
    def test_get_avg(self):
        x = self.curry6.get_avg(0.5)
        self.assertEqual(1+1/2+1/3+1/4+1/5-1/2,USDCAD_return.run_sum)
        self.assertEqual(x,USDCAD_return.run_sum/(USDCAD_return.num))
        USDCAD_return.num=0
        USDCAD_return.run_sum=0
        USDCAD_return.run_squared_sum=0
        USDCAD_return.run_sum_of_std=0
        USDCAD_return.last_price=-1

    def test_add_to_running_squared_sum(self):
        self.curry6.add_to_running_squared_sum(0.1)
        self.assertEqual(USDCAD_return.run_squared_sum,(0.2-0.1)**2)
        USDCAD_return.num=0
        USDCAD_return.run_sum=0
        USDCAD_return.run_squared_sum=0
        USDCAD_return.run_sum_of_std=0
        USDCAD_return.last_price=-1

    def test_get_std(self):
        self.curry6.add_to_running_squared_sum(0.1)
        x = self.curry6.get_std()
        self.assertEqual(x,sqrt(((0.2-0.1)**2)/5))
        USDCAD_return.num=0
        USDCAD_return.run_sum=0
        USDCAD_return.run_squared_sum=0
        USDCAD_return.run_sum_of_std=0
        USDCAD_return.last_price=-1

    def test_get_avg_std(self):
        x = self.curry6.get_avg_std(10)
        self.assertEqual(x,-2.0)
        USDCAD_return.num=0
        USDCAD_return.run_sum=0
        USDCAD_return.run_squared_sum=0
        USDCAD_return.run_sum_of_std=0
        USDCAD_return.last_price=-1

class CurrencyTestCase4(unittest.TestCase):
    def setUp(self):
        self.curry1 = USDJPY_return(1,10)
        self.curry2 = USDJPY_return(2,20)
        self.curry3 = USDJPY_return(3,30)
        self.curry4 = USDJPY_return(4,40)
        self.curry5 = USDJPY_return(5,50)
        self.curry6 = USDJPY_return(6,60)

    def test_num(self):
        self.assertEqual(5,USDJPY_return.num)
        USDJPY_return.num=0
        USDJPY_return.run_sum=0
        USDJPY_return.run_squared_sum=0
        USDJPY_return.run_sum_of_std=0
        USDJPY_return.last_price=-1
    
    def test_run_sum(self):
        self.assertEqual(1+1/2+1/3+1/4+1/5,USDJPY_return.run_sum)
        USDJPY_return.num=0
        USDJPY_return.run_sum=0
        USDJPY_return.run_squared_sum=0
        USDJPY_return.run_sum_of_std=0
        USDJPY_return.last_price=-1

    def test_run_squared_sum(self):
        self.assertEqual(0,USDJPY_return.run_squared_sum)
        USDJPY_return.num=0
        USDJPY_return.run_sum=0
        USDJPY_return.run_squared_sum=0
        USDJPY_return.run_sum_of_std=0
        USDJPY_return.last_price=-1

    def test_run_sum_of_std(self):
        self.assertEqual(0,USDJPY_return.run_sum_of_std)
        USDJPY_return.num=0
        USDJPY_return.run_sum=0
        USDJPY_return.run_squared_sum=0
        USDJPY_return.run_sum_of_std=0
        USDJPY_return.last_price=-1

    def test_last_price(self):
        x = self.curry6.last_price
        self.assertEqual(x,USDJPY_return.last_price)
        USDJPY_return.num=0
        USDJPY_return.run_sum=0
        USDJPY_return.run_squared_sum=0
        USDJPY_return.run_sum_of_std=0
        USDJPY_return.last_price=-1
   
    def test_get_avg(self):
        x = self.curry6.get_avg(0.5)
        self.assertEqual(1+1/2+1/3+1/4+1/5-1/2,USDJPY_return.run_sum)
        self.assertEqual(x,USDJPY_return.run_sum/(USDJPY_return.num))
        USDJPY_return.num=0
        USDJPY_return.run_sum=0
        USDJPY_return.run_squared_sum=0
        USDJPY_return.run_sum_of_std=0
        USDJPY_return.last_price=-1

    def test_add_to_running_squared_sum(self):
        self.curry6.add_to_running_squared_sum(0.1)
        self.assertEqual(USDJPY_return.run_squared_sum,(0.2-0.1)**2)
        USDJPY_return.num=0
        USDJPY_return.run_sum=0
        USDJPY_return.run_squared_sum=0
        USDJPY_return.run_sum_of_std=0
        USDJPY_return.last_price=-1

    def test_get_std(self):
        self.curry6.add_to_running_squared_sum(0.1)
        x = self.curry6.get_std()
        self.assertEqual(x,sqrt(((0.2-0.1)**2)/5))
        USDJPY_return.num=0
        USDJPY_return.run_sum=0
        USDJPY_return.run_squared_sum=0
        USDJPY_return.run_sum_of_std=0
        USDJPY_return.last_price=-1

    def test_get_avg_std(self):
        x = self.curry6.get_avg_std(10)
        self.assertEqual(x,-2.0)
        USDJPY_return.num=0
        USDJPY_return.run_sum=0
        USDJPY_return.run_squared_sum=0
        USDJPY_return.run_sum_of_std=0
        USDJPY_return.last_price=-1

class CurrencyTestCase5(unittest.TestCase):
    def setUp(self):
        self.curry1 = USDMXN_return(1,10)
        self.curry2 = USDMXN_return(2,20)
        self.curry3 = USDMXN_return(3,30)
        self.curry4 = USDMXN_return(4,40)
        self.curry5 = USDMXN_return(5,50)
        self.curry6 = USDMXN_return(6,60)

    def test_num(self):
        self.assertEqual(5,USDMXN_return.num)
        USDMXN_return.num=0
        USDMXN_return.run_sum=0
        USDMXN_return.run_squared_sum=0
        USDMXN_return.run_sum_of_std=0
        USDMXN_return.last_price=-1
    
    def test_run_sum(self):
        self.assertEqual(1+1/2+1/3+1/4+1/5,USDMXN_return.run_sum)
        USDMXN_return.num=0
        USDMXN_return.run_sum=0
        USDMXN_return.run_squared_sum=0
        USDMXN_return.run_sum_of_std=0
        USDMXN_return.last_price=-1

    def test_run_squared_sum(self):
        self.assertEqual(0,USDMXN_return.run_squared_sum)
        USDMXN_return.num=0
        USDMXN_return.run_sum=0
        USDMXN_return.run_squared_sum=0
        USDMXN_return.run_sum_of_std=0
        USDMXN_return.last_price=-1

    def test_run_sum_of_std(self):
        self.assertEqual(0,USDMXN_return.run_sum_of_std)
        USDMXN_return.num=0
        USDMXN_return.run_sum=0
        USDMXN_return.run_squared_sum=0
        USDMXN_return.run_sum_of_std=0
        USDMXN_return.last_price=-1

    def test_last_price(self):
        x = self.curry6.last_price
        self.assertEqual(x,USDMXN_return.last_price)
        USDMXN_return.num=0
        USDMXN_return.run_sum=0
        USDMXN_return.run_squared_sum=0
        USDMXN_return.run_sum_of_std=0
        USDMXN_return.last_price=-1
   
    def test_get_avg(self):
        x = self.curry6.get_avg(0.5)
        self.assertEqual(1+1/2+1/3+1/4+1/5-1/2,USDMXN_return.run_sum)
        self.assertEqual(x,USDMXN_return.run_sum/(USDMXN_return.num))
        USDMXN_return.num=0
        USDMXN_return.run_sum=0
        USDMXN_return.run_squared_sum=0
        USDMXN_return.run_sum_of_std=0
        USDMXN_return.last_price=-1

    def test_add_to_running_squared_sum(self):
        self.curry6.add_to_running_squared_sum(0.1)
        self.assertEqual(USDMXN_return.run_squared_sum,(0.2-0.1)**2)
        USDMXN_return.num=0
        USDMXN_return.run_sum=0
        USDMXN_return.run_squared_sum=0
        USDMXN_return.run_sum_of_std=0
        USDMXN_return.last_price=-1

    def test_get_std(self):
        self.curry6.add_to_running_squared_sum(0.1)
        x = self.curry6.get_std()
        self.assertEqual(x,sqrt(((0.2-0.1)**2)/5))
        USDMXN_return.num=0
        USDMXN_return.run_sum=0
        USDMXN_return.run_squared_sum=0
        USDMXN_return.run_sum_of_std=0
        USDMXN_return.last_price=-1

    def test_get_avg_std(self):
        x = self.curry6.get_avg_std(10)
        self.assertEqual(x,-2.0)
        USDMXN_return.num=0
        USDMXN_return.run_sum=0
        USDMXN_return.run_squared_sum=0
        USDMXN_return.run_sum_of_std=0
        USDMXN_return.last_price=-1

class CurrencyTestCase6(unittest.TestCase):
    def setUp(self):
        self.curry1 = EURUSD_return(1,10)
        self.curry2 = EURUSD_return(2,20)
        self.curry3 = EURUSD_return(3,30)
        self.curry4 = EURUSD_return(4,40)
        self.curry5 = EURUSD_return(5,50)
        self.curry6 = EURUSD_return(6,60)

    def test_num(self):
        self.assertEqual(5,EURUSD_return.num)
        EURUSD_return.num=0
        EURUSD_return.run_sum=0
        EURUSD_return.run_squared_sum=0
        EURUSD_return.run_sum_of_std=0
        EURUSD_return.last_price=-1
    
    def test_run_sum(self):
        self.assertEqual(1+1/2+1/3+1/4+1/5,EURUSD_return.run_sum)
        EURUSD_return.num=0
        EURUSD_return.run_sum=0
        EURUSD_return.run_squared_sum=0
        EURUSD_return.run_sum_of_std=0
        EURUSD_return.last_price=-1

    def test_run_squared_sum(self):
        self.assertEqual(0,EURUSD_return.run_squared_sum)
        EURUSD_return.num=0
        EURUSD_return.run_sum=0
        EURUSD_return.run_squared_sum=0
        EURUSD_return.run_sum_of_std=0
        EURUSD_return.last_price=-1

    def test_run_sum_of_std(self):
        self.assertEqual(0,EURUSD_return.run_sum_of_std)
        EURUSD_return.num=0
        EURUSD_return.run_sum=0
        EURUSD_return.run_squared_sum=0
        EURUSD_return.run_sum_of_std=0
        EURUSD_return.last_price=-1

    def test_last_price(self):
        x = self.curry6.last_price
        self.assertEqual(x,EURUSD_return.last_price)
        EURUSD_return.num=0
        EURUSD_return.run_sum=0
        EURUSD_return.run_squared_sum=0
        EURUSD_return.run_sum_of_std=0
        EURUSD_return.last_price=-1
   
    def test_get_avg(self):
        x = self.curry6.get_avg(0.5)
        self.assertEqual(1+1/2+1/3+1/4+1/5-1/2,EURUSD_return.run_sum)
        self.assertEqual(x,EURUSD_return.run_sum/(EURUSD_return.num))
        EURUSD_return.num=0
        EURUSD_return.run_sum=0
        EURUSD_return.run_squared_sum=0
        EURUSD_return.run_sum_of_std=0
        EURUSD_return.last_price=-1

    def test_add_to_running_squared_sum(self):
        self.curry6.add_to_running_squared_sum(0.1)
        self.assertEqual(EURUSD_return.run_squared_sum,(0.2-0.1)**2)
        EURUSD_return.num=0
        EURUSD_return.run_sum=0
        EURUSD_return.run_squared_sum=0
        EURUSD_return.run_sum_of_std=0
        EURUSD_return.last_price=-1

    def test_get_std(self):
        self.curry6.add_to_running_squared_sum(0.1)
        x = self.curry6.get_std()
        self.assertEqual(x,sqrt(((0.2-0.1)**2)/5))
        EURUSD_return.num=0
        EURUSD_return.run_sum=0
        EURUSD_return.run_squared_sum=0
        EURUSD_return.run_sum_of_std=0
        EURUSD_return.last_price=-1

    def test_get_avg_std(self):
        x = self.curry6.get_avg_std(10)
        self.assertEqual(x,-2.0)
        EURUSD_return.num=0
        EURUSD_return.run_sum=0
        EURUSD_return.run_squared_sum=0
        EURUSD_return.run_sum_of_std=0
        EURUSD_return.last_price=-1

class CurrencyTestCase7(unittest.TestCase):
    def setUp(self):
        self.curry1 = USDCNY_return(1,10)
        self.curry2 = USDCNY_return(2,20)
        self.curry3 = USDCNY_return(3,30)
        self.curry4 = USDCNY_return(4,40)
        self.curry5 = USDCNY_return(5,50)
        self.curry6 = USDCNY_return(6,60)

    def test_num(self):
        self.assertEqual(5,USDCNY_return.num)
        USDCNY_return.num=0
        USDCNY_return.run_sum=0
        USDCNY_return.run_squared_sum=0
        USDCNY_return.run_sum_of_std=0
        USDCNY_return.last_price=-1
    
    def test_run_sum(self):
        self.assertEqual(1+1/2+1/3+1/4+1/5,USDCNY_return.run_sum)
        USDCNY_return.num=0
        USDCNY_return.run_sum=0
        USDCNY_return.run_squared_sum=0
        USDCNY_return.run_sum_of_std=0
        USDCNY_return.last_price=-1

    def test_run_squared_sum(self):
        self.assertEqual(0,USDCNY_return.run_squared_sum)
        USDCNY_return.num=0
        USDCNY_return.run_sum=0
        USDCNY_return.run_squared_sum=0
        USDCNY_return.run_sum_of_std=0
        USDCNY_return.last_price=-1

    def test_run_sum_of_std(self):
        self.assertEqual(0,USDCNY_return.run_sum_of_std)
        USDCNY_return.num=0
        USDCNY_return.run_sum=0
        USDCNY_return.run_squared_sum=0
        USDCNY_return.run_sum_of_std=0
        USDCNY_return.last_price=-1

    def test_last_price(self):
        x = self.curry6.last_price
        self.assertEqual(x,USDCNY_return.last_price)
        USDCNY_return.num=0
        USDCNY_return.run_sum=0
        USDCNY_return.run_squared_sum=0
        USDCNY_return.run_sum_of_std=0
        USDCNY_return.last_price=-1
   
    def test_get_avg(self):
        x = self.curry6.get_avg(0.5)
        self.assertEqual(1+1/2+1/3+1/4+1/5-1/2,USDCNY_return.run_sum)
        self.assertEqual(x,USDCNY_return.run_sum/(USDCNY_return.num))
        USDCNY_return.num=0
        USDCNY_return.run_sum=0
        USDCNY_return.run_squared_sum=0
        USDCNY_return.run_sum_of_std=0
        USDCNY_return.last_price=-1

    def test_add_to_running_squared_sum(self):
        self.curry6.add_to_running_squared_sum(0.1)
        self.assertEqual(USDCNY_return.run_squared_sum,(0.2-0.1)**2)
        USDCNY_return.num=0
        USDCNY_return.run_sum=0
        USDCNY_return.run_squared_sum=0
        USDCNY_return.run_sum_of_std=0
        USDCNY_return.last_price=-1

    def test_get_std(self):
        self.curry6.add_to_running_squared_sum(0.1)
        x = self.curry6.get_std()
        self.assertEqual(x,sqrt(((0.2-0.1)**2)/5))
        USDCNY_return.num=0
        USDCNY_return.run_sum=0
        USDCNY_return.run_squared_sum=0
        USDCNY_return.run_sum_of_std=0
        USDCNY_return.last_price=-1

    def test_get_avg_std(self):
        x = self.curry6.get_avg_std(10)
        self.assertEqual(x,-2.0)
        USDCNY_return.num=0
        USDCNY_return.run_sum=0
        USDCNY_return.run_squared_sum=0
        USDCNY_return.run_sum_of_std=0
        USDCNY_return.last_price=-1

class CurrencyTestCase8(unittest.TestCase):
    def setUp(self):
        self.curry1 = USDCZK_return(1,10)
        self.curry2 = USDCZK_return(2,20)
        self.curry3 = USDCZK_return(3,30)
        self.curry4 = USDCZK_return(4,40)
        self.curry5 = USDCZK_return(5,50)
        self.curry6 = USDCZK_return(6,60)

    def test_num(self):
        self.assertEqual(5,USDCZK_return.num)
        USDCZK_return.num=0
        USDCZK_return.run_sum=0
        USDCZK_return.run_squared_sum=0
        USDCZK_return.run_sum_of_std=0
        USDCZK_return.last_price=-1
    
    def test_run_sum(self):
        self.assertEqual(1+1/2+1/3+1/4+1/5,USDCZK_return.run_sum)
        USDCZK_return.num=0
        USDCZK_return.run_sum=0
        USDCZK_return.run_squared_sum=0
        USDCZK_return.run_sum_of_std=0
        USDCZK_return.last_price=-1

    def test_run_squared_sum(self):
        self.assertEqual(0,USDCZK_return.run_squared_sum)
        USDCZK_return.num=0
        USDCZK_return.run_sum=0
        USDCZK_return.run_squared_sum=0
        USDCZK_return.run_sum_of_std=0
        USDCZK_return.last_price=-1

    def test_run_sum_of_std(self):
        self.assertEqual(0,USDCZK_return.run_sum_of_std)
        USDCZK_return.num=0
        USDCZK_return.run_sum=0
        USDCZK_return.run_squared_sum=0
        USDCZK_return.run_sum_of_std=0
        USDCZK_return.last_price=-1

    def test_last_price(self):
        x = self.curry6.last_price
        self.assertEqual(x,USDCZK_return.last_price)
        USDCZK_return.num=0
        USDCZK_return.run_sum=0
        USDCZK_return.run_squared_sum=0
        USDCZK_return.run_sum_of_std=0
        USDCZK_return.last_price=-1
   
    def test_get_avg(self):
        x = self.curry6.get_avg(0.5)
        self.assertEqual(1+1/2+1/3+1/4+1/5-1/2,USDCZK_return.run_sum)
        self.assertEqual(x,USDCZK_return.run_sum/(USDCZK_return.num))
        USDCZK_return.num=0
        USDCZK_return.run_sum=0
        USDCZK_return.run_squared_sum=0
        USDCZK_return.run_sum_of_std=0
        USDCZK_return.last_price=-1

    def test_add_to_running_squared_sum(self):
        self.curry6.add_to_running_squared_sum(0.1)
        self.assertEqual(USDCZK_return.run_squared_sum,(0.2-0.1)**2)
        USDCZK_return.num=0
        USDCZK_return.run_sum=0
        USDCZK_return.run_squared_sum=0
        USDCZK_return.run_sum_of_std=0
        USDCZK_return.last_price=-1

    def test_get_std(self):
        self.curry6.add_to_running_squared_sum(0.1)
        x = self.curry6.get_std()
        self.assertEqual(x,sqrt(((0.2-0.1)**2)/5))
        USDCZK_return.num=0
        USDCZK_return.run_sum=0
        USDCZK_return.run_squared_sum=0
        USDCZK_return.run_sum_of_std=0
        USDCZK_return.last_price=-1

    def test_get_avg_std(self):
        x = self.curry6.get_avg_std(10)
        self.assertEqual(x,-2.0)
        USDCZK_return.num=0
        USDCZK_return.run_sum=0
        USDCZK_return.run_squared_sum=0
        USDCZK_return.run_sum_of_std=0
        USDCZK_return.last_price=-1


class CurrencyTestCase9(unittest.TestCase):
    def setUp(self):
        self.curry1 = USDPLN_return(1,10)
        self.curry2 = USDPLN_return(2,20)
        self.curry3 = USDPLN_return(3,30)
        self.curry4 = USDPLN_return(4,40)
        self.curry5 = USDPLN_return(5,50)
        self.curry6 = USDPLN_return(6,60)

    def test_num(self):
        self.assertEqual(5,USDPLN_return.num)
        USDPLN_return.num=0
        USDPLN_return.run_sum=0
        USDPLN_return.run_squared_sum=0
        USDPLN_return.run_sum_of_std=0
        USDPLN_return.last_price=-1
    
    def test_run_sum(self):
        self.assertEqual(1+1/2+1/3+1/4+1/5,USDPLN_return.run_sum)
        USDPLN_return.num=0
        USDPLN_return.run_sum=0
        USDPLN_return.run_squared_sum=0
        USDPLN_return.run_sum_of_std=0
        USDPLN_return.last_price=-1

    def test_run_squared_sum(self):
        self.assertEqual(0,USDPLN_return.run_squared_sum)
        USDPLN_return.num=0
        USDPLN_return.run_sum=0
        USDPLN_return.run_squared_sum=0
        USDPLN_return.run_sum_of_std=0
        USDPLN_return.last_price=-1

    def test_run_sum_of_std(self):
        self.assertEqual(0,USDPLN_return.run_sum_of_std)
        USDPLN_return.num=0
        USDPLN_return.run_sum=0
        USDPLN_return.run_squared_sum=0
        USDPLN_return.run_sum_of_std=0
        USDPLN_return.last_price=-1

    def test_last_price(self):
        x = self.curry6.last_price
        self.assertEqual(x,USDPLN_return.last_price)
        USDPLN_return.num=0
        USDPLN_return.run_sum=0
        USDPLN_return.run_squared_sum=0
        USDPLN_return.run_sum_of_std=0
        USDPLN_return.last_price=-1
   
    def test_get_avg(self):
        x = self.curry6.get_avg(0.5)
        self.assertEqual(1+1/2+1/3+1/4+1/5-1/2,USDPLN_return.run_sum)
        self.assertEqual(x,USDPLN_return.run_sum/(USDPLN_return.num))
        USDPLN_return.num=0
        USDPLN_return.run_sum=0
        USDPLN_return.run_squared_sum=0
        USDPLN_return.run_sum_of_std=0
        USDPLN_return.last_price=-1

    def test_add_to_running_squared_sum(self):
        self.curry6.add_to_running_squared_sum(0.1)
        self.assertEqual(USDPLN_return.run_squared_sum,(0.2-0.1)**2)
        USDPLN_return.num=0
        USDPLN_return.run_sum=0
        USDPLN_return.run_squared_sum=0
        USDPLN_return.run_sum_of_std=0
        USDPLN_return.last_price=-1

    def test_get_std(self):
        self.curry6.add_to_running_squared_sum(0.1)
        x = self.curry6.get_std()
        self.assertEqual(x,sqrt(((0.2-0.1)**2)/5))
        USDPLN_return.num=0
        USDPLN_return.run_sum=0
        USDPLN_return.run_squared_sum=0
        USDPLN_return.run_sum_of_std=0
        USDPLN_return.last_price=-1

    def test_get_avg_std(self):
        x = self.curry6.get_avg_std(10)
        self.assertEqual(x,-2.0)
        USDPLN_return.num=0
        USDPLN_return.run_sum=0
        USDPLN_return.run_squared_sum=0
        USDPLN_return.run_sum_of_std=0
        USDPLN_return.last_price=-1


class CurrencyTestCase10(unittest.TestCase):
    def setUp(self):
        self.curry1 = USDINR_return(1,10)
        self.curry2 = USDINR_return(2,20)
        self.curry3 = USDINR_return(3,30)
        self.curry4 = USDINR_return(4,40)
        self.curry5 = USDINR_return(5,50)
        self.curry6 = USDINR_return(6,60)

    def test_num(self):
        self.assertEqual(5,USDINR_return.num)
        USDINR_return.num=0
        USDINR_return.run_sum=0
        USDINR_return.run_squared_sum=0
        USDINR_return.run_sum_of_std=0
        USDINR_return.last_price=-1
    
    def test_run_sum(self):
        self.assertEqual(1+1/2+1/3+1/4+1/5,USDINR_return.run_sum)
        USDINR_return.num=0
        USDINR_return.run_sum=0
        USDINR_return.run_squared_sum=0
        USDINR_return.run_sum_of_std=0
        USDINR_return.last_price=-1

    def test_run_squared_sum(self):
        self.assertEqual(0,USDINR_return.run_squared_sum)
        USDINR_return.num=0
        USDINR_return.run_sum=0
        USDINR_return.run_squared_sum=0
        USDINR_return.run_sum_of_std=0
        USDINR_return.last_price=-1

    def test_run_sum_of_std(self):
        self.assertEqual(0,USDINR_return.run_sum_of_std)
        USDINR_return.num=0
        USDINR_return.run_sum=0
        USDINR_return.run_squared_sum=0
        USDINR_return.run_sum_of_std=0
        USDINR_return.last_price=-1

    def test_last_price(self):
        x = self.curry6.last_price
        self.assertEqual(x,USDINR_return.last_price)
        USDINR_return.num=0
        USDINR_return.run_sum=0
        USDINR_return.run_squared_sum=0
        USDINR_return.run_sum_of_std=0
        USDINR_return.last_price=-1
   
    def test_get_avg(self):
        x = self.curry6.get_avg(0.5)
        self.assertEqual(1+1/2+1/3+1/4+1/5-1/2,USDINR_return.run_sum)
        self.assertEqual(x,USDINR_return.run_sum/(USDINR_return.num))
        USDINR_return.num=0
        USDINR_return.run_sum=0
        USDINR_return.run_squared_sum=0
        USDINR_return.run_sum_of_std=0
        USDINR_return.last_price=-1

    def test_add_to_running_squared_sum(self):
        self.curry6.add_to_running_squared_sum(0.1)
        self.assertEqual(USDINR_return.run_squared_sum,(0.2-0.1)**2)
        USDINR_return.num=0
        USDINR_return.run_sum=0
        USDINR_return.run_squared_sum=0
        USDINR_return.run_sum_of_std=0
        USDINR_return.last_price=-1

    def test_get_std(self):
        self.curry6.add_to_running_squared_sum(0.1)
        x = self.curry6.get_std()
        self.assertEqual(x,sqrt(((0.2-0.1)**2)/5))
        USDINR_return.num=0
        USDINR_return.run_sum=0
        USDINR_return.run_squared_sum=0
        USDINR_return.run_sum_of_std=0
        USDINR_return.last_price=-1

    def test_get_avg_std(self):
        x = self.curry6.get_avg_std(10)
        self.assertEqual(x,-2.0)
        USDINR_return.num=0
        USDINR_return.run_sum=0
        USDINR_return.run_squared_sum=0
        USDINR_return.run_sum_of_std=0
        USDINR_return.last_price=-1
        
if __name__ == '__main__':
    unittest.main()


