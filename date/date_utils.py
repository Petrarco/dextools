import datetime as dt
from datetime               import timedelta
from dateutil.relativedelta import relativedelta


class DateUtils:
    def __init__(self, input_date, date_format='%Y-%m-%d'):

        self.date_format = date_format
        self.dt_refe = DateUtils.convert_string_to_date(input_date, self.date_format)
        self.st_date = DateUtils.convert_date_to_string(self.dt_refe)

    def convert_string_to_date(st_dt_refe, date_format='%Y-%m-%d') -> dt.datetime:
        try:    
            return dt.datetime.strptime(st_dt_refe, date_format)
        except:
            raise ValueError('Erro na conversão de data')
    
    def convert_date_to_string(dt_refe, date_format='%Y-%m-%d') -> str:
        if isinstance(dt_refe, str) is True:
            st_dt_refe = DateUtils.convert_string_to_date(dt_refe)
        elif isinstance(dt_refe, dt.datetime) is True or isinstance(dt_refe, dt.date) is True:
            st_dt_refe = dt_refe.strftime(date_format)
        else:
            raise ValueError('Argumento dt_refe não é do tipo date')
        return st_dt_refe

    
    def get_year(self):
        return self.dt_refe.year
    
    def get_month(self):
        return self.dt_refe.month
    
    def get_day(self):
        return self.dt_refe.day
    
    def get_day_of_year(self):
        return self.dt_refe.timetuple().tm_yday
    
    def get_week(self):
        return self.dt_refe.isoweekday()   

    def get_week_month(self):
        return (self.dt_refe.isocalendar()[1] - self.dt_refe.replace(day=1).isocalendar()[1] + 1)
    
    def get_week_year(self):
        return self.dt_refe.isocalendar()[1]

    def get_first_day_of_month(self) -> str:        
        return DateUtils.convert_date_to_string( dt.datetime(self.get_year(), self.get_month(), 1))

    def get_last_day_of_month(self) -> str:     
        return DateUtils.convert_date_to_string((DateUtils.convert_string_to_date(self.get_first_day_of_month()) + relativedelta(months=+1)) + relativedelta(days=-1))    
    
    def get_first_day_of_week(self) -> str:
        return self.dt_refe - timedelta(days = self.dt_refe.weekday()) 
    
    def get_last_day_of_week(self) -> str:
        return self.get_first_day_of_week() + timedelta(days = 6)  

    def get_bimester(self) -> int:
        month = self.get_month()
        return ((month - 1) // 2 + 1)

    def get_semester(self) -> int:
        month = self.get_month()
        return (month - 1) // 6 + 1

    def get_trimester(self) -> int:
        month = self.get_month()
        return (month - 1) // 3 + 1
    
    def get_quadrimester(self) -> int:
        month = self.get_month()
        return (month - 1) // 3 + 1

    def get_date_info(self):
        return {
            "Ano": self.get_year(),
            "Mês": self.get_month(),
            "Dia": self.get_day(),
            "Dia do Ano": self.get_day_of_year(),
            "Semana": self.get_week(),
            "Semana Mês": self.get_week_month(),
            "Semana Ano": self.get_week_year(),
            "Primeiro dia do mês": self.get_first_day_of_month(),
            "Último dia do mês": self.get_last_day_of_month(),
            "Primeiro dia da Semana": self.get_first_day_of_week(),
            "Último dia da Semana": self.get_last_day_of_week(),
            "Bimestre": self.get_bimester(),
            "Semestre": self.get_semester(),
            "Trimestre": self.get_trimester(),
        }


if __name__ == "__main__":
    data_input = '2024-10-31'  # Formato: 'YYYY-MM-DD'
    date_info = DateUtils(data_input)
    informacoes_data = date_info.get_date_info()
    for chave, valor in informacoes_data.items():
        print(f"{chave}: {valor}")
    
    #start_date = dt.datetime(2014, 12, 31)
    #print(rrule.after(start_date, True))
    #print(list(rrule(freq=MONTHLY, count=4, dtstart=start_date)))