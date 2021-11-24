import requests
import xml.etree.ElementTree as Et

url = "http://localhost:9000"

data = "<ENVELOPE><HEADER><VERSION>1</VERSION><TALLYREQUEST>EXPORT</TALLYREQUEST><TYPE>COLLECTION</TYPE><ID>List of Ledgers</ID>"
data += "</HEADER><BODY><DESC><STATICVARIABLES><SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT></STATICVARIABLES></DESC></BODY></ENVELOPE>"

request = requests.post(url=url, data=data)

response = request.text.strip().replace("&amp;", "and")

responseXML = Et.fromstring(response)

for data in responseXML.findall('./BODY/DATA/COLLECTION/LEDGER'):
    print(data.get('NAME'))
