import requests, zipfile, io, json, sys
import module
import os.path


headers = {
  'Content-Type': 'application/json',
  'Authorization': 'eeb5e2cb3f6448b7a509dcc2d4ef0ed9'
}

URL = 'https://www.hlidacstatu.cz/api/v1/dump?datatype=dataset.prijemcidotaci'
ic = ''
download_new_data = ''
initial = 0

def download_data():
  print('Stahuji nová data..')
  r = requests.get(URL, headers=headers)
  z = zipfile.ZipFile(io.BytesIO(r.content))
  z.extractall('./zipfiles')
  print('DATA STAŽENA')

if os.path.isfile('./zipfiles/dataset.prijemcidotaci.dump.data.json') == True:
  pass
else:
  print('V adresáři dosud nejsou žádná data. Nyní proběhne iniciální stažení dat z Hlídače. Může to chvíli trvat.')
  download_data()

'''
def search_ico(ico):
 for keyval in dataset:
  if ico == keyval['ICO']:
    print('Jméno: ', keyval['Jmeno'], '\nAdresa: ', keyval['Adresa'], '\nRok: ', keyval['Rok'], '\nZdroje ČR: ', keyval['ZdrojeCr'], '\nZdroje EU: ', keyval['ZdrojeEu'], '\nURL: ', keyval['Url'], '\n===========================================')


if initial != 1:
  download_new_data = input('Chcete stáhnout aktuální dataset o příjemcích dotací z Hlídače státu? (Y/N): ')
if download_new_data.upper() == 'Y':
  download_data()

while ic.upper() != 'X':
  ic = input('Pro jaké IČO chcete hledat záznamy (pro konec zadejte X): ')
  try:
    search_ico(ic)
  except:
    pass
'''

#search_ico('00103004')

path = '/Users/ondrejtichy/Desktop/Hlidac/zipfiles/dataset.prijemcidotaci.dump.data.json'
sheetname  = 'data'
output_file = '/Users/ondrejtichy/Desktop/Hlidac/xlsx'
module.json_toXlsx(path,output_file,sheetname)