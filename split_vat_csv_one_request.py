
# coding: utf-8

# Author do not assume and hereby disclaim any liability to any party for any loss, damage, or disruption caused by errors or omissions, whether such errors or omissions result from negligence, accident, or any other cause. The software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement.

# In[ ]:

"""
REFERENCES

https://www.anaconda.com/download/
http://jupyter.org/
https://www.python.org/

https://www.anaf.ro/anaf/internet/ANAF/informatii_publice/informatii_agenti_economici/RegPlataDefalcataTVA
https://webservicesp.anaf.ro/AsynchWebService/api/v3/ws/tva

Warning in Romanian language
b) Orice tentativa de suprasolicitare a serverului va fi pedepsita conform reglementarilor in vigoare.
Warning in English language
b) Any attempt to overload the server will be punished according to the regulations in force.
"""


# In[ ]:

import requests
import json
import timeit
import datetime
import sys


print(sys.version, '\n')
print(datetime.datetime.now(), '\n')

# https://www.anaf.ro/anaf/internet/ANAF/informatii_publice/informatii_agenti_economici/RegPlataDefalcataTVA
url = "https://webservicesp.anaf.ro/PlatitorTvaRest/api/v3/ws/tva"

data= [{"cui": '10874881', "data": '2017-12-22'}]
start = timeit.default_timer()
r = requests.post(url, json=data)
#print(r.text) # If you want to view entire content

key_start = r.text.find('[')
key_start+=1
key_end = r.text.find(']')

dict_r = r.text[key_start:key_end]
dict_r = json.loads(dict_r)
stop = timeit.default_timer()

print("status_code:", r.status_code)
print("data:", data) 
print("denumire:",dict_r['denumire'])
print("cui:", dict_r['cui'])
print("dataInceputSplitTVA:",dict_r['dataInceputSplitTVA'])
print("dataAnulareSplitTVA:", dict_r['dataAnulareSplitTVA'])
print("statusSplitTVA:",dict_r['statusSplitTVA'])
print("request duration", stop - start) 

# OUTPUT:
# status_code: 200
# data: [{'cui': '10874881', 'data': '2017-12-14'}]
# denumire: SOCIETATEA NATIONALA "NUCLEARELECTRICA" SA
# cui: 10874881
# dataInceputSplitTVA: 2017-09-29
# dataAnulareSplitTVA:  
# statusSplitTVA: True
# request duration 0.18321414984132353

# Rough estimation of duration for request only part for 10000 records = 1832.141498 seconds


# In[ ]:

# Entire content
r.text


# In[ ]:



