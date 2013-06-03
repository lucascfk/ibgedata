#!/usr/bin/env python3

from urllib.request import urlopen
from bs4 import BeautifulSoup

# address to extract information from municipalities by state
address = 'http://www.ibge.gov.br/cidadesat/ufs/download/mapa_e_municipios.php'

# requests the page sending state as parameter "uf"
request = urlopen('%s?uf=%s' % (address, 'sp'))

# parse the page as html5
page = BeautifulSoup(request.read(), 'html5')

# the data are in the table id "municipios"
table = page.find('table', id='municipios')

# labels will have the data table header
labels = []

# data will have the data table body
data = []

# runs the header for labels
for th in table.thead.tr.find_all('th'):
    labels.append(th.string.strip())

# rus the body for data
for tr in table.tbody.find_all('tr'):
    line = []
    for td in tr.find_all('td'):
        line.append(td.string.strip())

    data.append(line)

print(data)