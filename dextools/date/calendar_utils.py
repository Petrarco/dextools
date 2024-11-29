import os
import sys
sys.path.insert(1, os.getcwd())
from dextools.date.date_utils import DateUtils
from dateutil.relativedelta import relativedelta

class CalendarUtils:
    def __init__(self, start_date: str, end_date: str, is_business_days=False) -> None:
        self.start_date = DateUtils.convert_string_to_date(start_date)
        self.end_date = DateUtils.convert_string_to_date(end_date)
        self.date_days_diff = abs((self.start_date - self.end_date).days)
        self.is_business_days = is_business_days
        print(self.date_days_diff)

    def get_calendar(self) -> list:

        list_calendar = []
        i=0
        while (i <= self.date_days_diff):
            dt_refe = self.start_date + relativedelta(days=i)
            st_dt_refe = DateUtils.convert_date_to_string(dt_refe)
            date_utils = DateUtils(st_dt_refe)
            if self.is_business_days:
                if date_utils.check_is_business_days():
                    list_calendar.append(date_utils.dt_refe)
            else:
                list_calendar.append(date_utils.dt_refe)
            i+=1
        
        return list_calendar

if __name__ == "__main__":
    
    cale = CalendarUtils('2024-10-01', '2024-11-30', True).get_calendar()
    print((cale))
    print(len(cale))



