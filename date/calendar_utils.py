from date_utils import DateUtils
from dateutil.relativedelta import relativedelta

class Calendar:
    def __init__(self, start_date: str, end_date: str, is_business_days=False) -> None:
        self.start_date = DateUtils.convert_string_to_date(start_date)
        self.end_date = DateUtils.convert_string_to_date(end_date)
        self.date_days_diff = (self.start_date - self.end_date).days
        self.is_business_days = is_business_days

    def get_calendar(self):

        i=0
        while (i <= self.date_days_diff):
            dt_refe = self.end_date + relativedelta(days=i)
            st_dt_refe = DateUtils.convert_date_to_string(dt_refe)
            date_utils = DateUtils(st_dt_refe)



