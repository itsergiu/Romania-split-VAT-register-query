
# coding: utf-8

# Author do not assume and hereby disclaim any liability to any party for any loss, damage, or disruption caused by errors or omissions, whether such errors or omissions result from negligence, accident, or any other cause.
# The software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement.

# In[ ]:

# Do not run this cell.
# https://www.anaconda.com/download/
# http://jupyter.org/
# https://www.python.org/
# https://www.anaf.ro/anaf/internet/ANAF/informatii_publice/informatii_agenti_economici/RegPlataDefalcataTVA
# url = "https://webservicesp.anaf.ro/AsynchWebService/api/v3/ws/tva"
# Warning in Romanian language
# b) Orice tentativa de suprasolicitare a serverului va fi pedepsita conform reglementarilor in vigoare.
# Warning in English language
# b) Any attempt to overload the server will be punished according to the regulations in force.


# In[ ]:

# Do not run this cell. Create the file.
Source path_upload: active_vendor.csv:
Vendor_key,Vendor_name,CUI
"SNN","S.N. NUCLEARELECTRICA S.A.","10874881"
"SNP","OMV PETROM S.A.","1590082"


# In[ ]:

# Run cell
date = '2017-12-20'
path_upload = "C:/00SplitVAT/active_vendor.csv"
path_save = "C:/00SplitVAT/active_vendor_result.csv"


# In[ ]:

# Run cell
import requests
import json
import timeit
import time
import csv
import sys

print(sys.version)
# https://www.anaf.ro/anaf/internet/ANAF/informatii_publice/informatii_agenti_economici/RegPlataDefalcataTVA
# url = "https://webservicesp.anaf.ro/AsynchWebService/api/v3/ws/tva"
url = "https://webservicesp.anaf.ro/PlatitorTvaRest/api/v3/ws/tva"

file_upload = open(path_upload, newline='')
reader = csv.reader(file_upload)
header = next(reader)

file_save = open(path_save, 'w', encoding="utf-8")
writer = csv.writer(file_save)
writer.writerow (["Vendor_key", "Vendor_name", "CUI", "status_code", "data", "denumire",                   "cui:", "dataInceputSplitTVA", "dataAnulareSplitTVA", "statusSplitTVA"])

start = timeit.default_timer()
i = 0
for row in reader:
    i+=1
    cui = row[2]
    data_dict = {'cui': cui, 'data': date}
    data = []
    data.append(data_dict)
    r = requests.post(url, json=data)
    #print(r.text) # If you want to view entire content

    key_start = r.text.find('[')
    key_start+=1
    key_end = r.text.find(']')

    if r.status_code == 200:
        r_dict = r.text[key_start:key_end]
        r_dict = json.loads(r_dict)
        writer.writerow([row[0], row[1], row[2], r.status_code, data, r_dict['denumire'],                          r_dict['cui'], r_dict['dataInceputSplitTVA'], r_dict['dataAnulareSplitTVA'],                          r_dict['statusSplitTVA']])
    else:
        writer.writerow ([row[0], row[1], row[2], r.status_code, data,"","","","",""])
        
# If you want to print results        
#    print([row[0], row[1], row[2], r.status_code, data, r_dict['denumire'], \
#          r_dict['cui'], r_dict['dataInceputSplitTVA'], r_dict['dataAnulareSplitTVA'], \
#          r_dict['statusSplitTVA']])
#    print(row[0])
        
    print('{} / {} / {}.'.format(row[0],r.status_code,i), end='\r')
    sys.stdout.flush()

file_save.close()
stop = timeit.default_timer()
print("request duration:", stop - start)


# In[ ]:

# Do not run this cell.
Result path_save: active_vendor.csv
Vendor_key,Vendor_name,CUI,status_code,data,denumire,cui:,dataInceputSplitTVA,dataAnulareSplitTVA,statusSplitTVA
SNN,S.N. NUCLEARELECTRICA S.A.,10874881,200,"[{'cui': '10874881', 'data': '2017-12-20'}]","SOCIETATEA NATIONALA ""NUCLEARELECTRICA"" SA",10874881,2017-09-29, ,True
SNP,OMV PETROM S.A.,1590082,200,"[{'cui': '1590082', 'data': '2017-12-20'}]",OMV PETROM SA,1590082,,,False

