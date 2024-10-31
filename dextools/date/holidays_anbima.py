import os
import xlrd
from datetime import date
from urllib.request import urlretrieve

class HolidaysAnbima:
    file_url = 'http://www.anbima.com.br/feriados/arqs/feriados_nacionais.xls'
    file_path = '/data/feriados_nacionais.xls'

    def __init__(self, file_url=file_url, file_path=file_path ) -> None:
        self.file_path = file_path
        self.file_url = file_url
        
        from pathlib import Path

        # Get the current working directory
        cwd = Path.cwd()

        print(f" {file_path} então {os.path.isfile(os.path.dirname(__file__)+self.file_path)}")
        print(cwd)
        print(os.path.abspath(__file__))
        print('__file__:    ', __file__)
        print('basename:    ', os.path.basename(__file__))
        print('dirname:     ', os.path.dirname(__file__)+self.file_path)
    # directory exists




def holidays(url=None, path=None):
    if not url:
        url = 'http://www.anbima.com.br/feriados/arqs/feriados_nacionais.xls'
    if not path:
        path = 'data/feriados_nacionais.xls'
    try:
        wb = xlrd.open_workbook(path)
    except:
        response = urlretrieve(url, filename=path)
        wb = xlrd.open_workbook(path)
    ws = wb.sheet_by_index(0)
    i = 1
    dates = []
    while ws.cell_type(i, 0) == 3:
        y, m, d, _, _, _ = xlrd.xldate_as_tuple(ws.cell_value(i, 0), wb.datemode)
        dates.append(date(y, m, d))
        i += 1
    return dates


if __name__ == '__main__':
    #print(holidays())
    HolidaysAnbima()

