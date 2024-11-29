import os
import xlrd
from datetime import date
from urllib.request import urlretrieve

class HolidaysAnbima:
    file_url = 'http://www.anbima.com.br/feriados/arqs/feriados_nacionais.xls'
    file_name = 'feriados_nacionais.xls'
    file_path = '/data/'

    def __init__(self, file_url=file_url, file_path=file_path, file_name=file_name ) -> None:
        self.file_name = file_name
        self.file_path = file_path
        self.file_url  = file_url 
        self.file_name_full = os.path.dirname(__file__) + self.file_path + self.file_name    

    def validate_file(self) -> bool:
        
        print(f'filename is {self.file_name_full} ')
        if os.path.isfile(self.file_name_full):
            file_status = True
        else:
            os.mkdir(os.path.dirname(__file__) + '/data')
            urlretrieve(self.file_url, filename=self.file_name_full)
            file_status = os.path.isfile(self.file_name_full)

        return file_status
    
    def get_dates(self) -> list:

        if self.validate_file():

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



if __name__ == '__main__':
    #print(holidays())
    print(str(HolidaysAnbima().get_dates()))
    

