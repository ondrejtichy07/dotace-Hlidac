import requests, zipfile, io, json, sys

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
  z.extractall('/Users/ondrejtichy/Desktop/Hlidac_statu/zipfiles')
  print('Data stažena')


try:
  f = open('/Users/ondrejtichy/Desktop/Hlidac_statu/zipfiles/dataset.prijemcidotaci.dump.data.json', 'r')
  dataset = json.load(f)
  data = json.dumps(dataset, indent=4, sort_keys=True)
  #print(data)
except:
  print('V adresáři dosud nejsou žádná data. Nyní proběhne iniciální stažení dat z Hlídače. Může to chvíli trvat.')
  download_data()
  l = open('/Users/ondrejtichy/Desktop/Hlidac_statu/zipfiles/dataset.prijemcidotaci.dump.data.json', 'r')
  dataset = json.load(l)
  initial = 1

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

#search_ico('00103004')