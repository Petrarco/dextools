import os
import xlrd
import datetime as dt
from datetime import date
from urllib.request import urlretrieve
from dextools.date.date_utils import DateUtils

class HolidaysAnbima:
    file_url = 'http://www.anbima.com.br/feriados/arqs/feriados_nacionais.xls'
    file_name = 'feriados_nacionais.xls'
    file_path = '/data/'

    def __init__(self, file_url=file_url, file_path=file_path, file_name=file_name ) -> None:
        self.file_name = file_name
        self.file_path = file_path
        self.file_url  = file_url 
        self.file_name_full = os.path.dirname(__file__) + self.file_path + self.file_name    

    def _validate_file(self) -> bool:
        
        print(f'filename is {self.file_name_full} ')
        if os.path.isfile(self.file_name_full):
            file_status = True
        else:
            os.mkdir(os.path.dirname(__file__) + '/data')
            urlretrieve(self.file_url, filename=self.file_name_full)
            file_status = os.path.isfile(self.file_name_full)

        return file_status
    
    def get_dates(self) -> list:

        if self._validate_file():

            wb = xlrd.open_workbook(self.file_name_full)    
            ws = wb.sheet_by_index(0)
            i = 1
            dates = []
            while ws.cell_type(i, 0) == 3:
                y, m, d, _, _, _ = xlrd.xldate_as_tuple(ws.cell_value(i, 0), wb.datemode)
                dates.append(date(y, m, d))
                i += 1
            return dates
        else:
            raise ValueError('Não foi possível carregar o arquivo')
        
    def check_is_holiday_anbima(st_dt_refe):

        datas = HolidaysAnbima().get_dates()  
        dt_aux = dt.datetime.strptime(st_dt_refe, '%Y-%m-%d')
        dt_refe = dt.date(dt_aux.year, dt_aux.month, dt_aux.day)

        if dt_refe in datas:
            is_holiday = True
        else:
            is_holiday = False
        
        return is_holiday


if __name__ == '__main__':
    #print(holidays())    
    datas = HolidaysAnbima().get_dates()    
    print(HolidaysAnbima.check_is_holiday_anbima('2024-11-15'))
    

