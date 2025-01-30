"""
Author: Luis Rodriguez Chaves
Beggining date: 12-1-25

File dedicated to normalization of dates. It uses decorators, it mostly work for exercises.
Python version used: 3.13

#must install python-dateutil first
pip install python-dateutil
Version: 1.0
"""

from dateutil import parser
from datetime import datetime
import pytz


class RegionDate():

    def normalize_date(date_func):
        def wrapper(self,*arg, **kw):
            region_datetime=date_func(self,*arg, **kw)
            if type(region_datetime)==datetime:
                return region_datetime.strftime("%d-%m-%Y %H:%M:%S")
            else:
                return parser.parse(region_datetime).strftime("%d-%m-%Y %H:%M:%S")
            
        return wrapper

    @normalize_date
    def japan_time(self):
        japan_tz = pytz.timezone('Asia/Tokyo')
        japan_time = datetime.now(japan_tz)
        return japan_time
    
    @normalize_date
    def england_time(self):
        england_tz=pytz.timezone("Europe/London")
        england_time=datetime.now(england_tz)
        return england_time

    @normalize_date
    def india_time(self):
        #in a disordered way to later on get it ordered
        india_tz=pytz.timezone("Asia/Kolkata")
        india_time=datetime.now(india_tz).strftime("%Y-%m-%d %H:%M:%S")
        return india_time

    @normalize_date
    def california_time(self):
        california_pt_tz=pytz.timezone("US/Pacific")
        california_time=datetime.now(california_pt_tz).strftime("%Y-%m-%d")
        return california_time

    def show_all_timezones(self):
        return pytz.all_timezones

dates_around_the_world=RegionDate()
japan_time=dates_around_the_world.japan_time()
england_time=dates_around_the_world.england_time()
india_time=dates_around_the_world.india_time()
california_time=dates_around_the_world.california_time()
print(f"The time in Japan right now is: {japan_time}")
print(f"The time in England right now is: {england_time}")
print(f"The time in India right now is: {india_time}")
print(f"The time in California(US) right now is: {california_time}")

