from urllib.request import urlretrieve

url = 'http://www.anbima.com.br/feriados/arqs/feriados_nacionais.xls'
path = 'date/data/feriados_nacionais.xls'

response = urlretrieve(url, filename=path)