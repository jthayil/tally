import requests
import xml.etree.ElementTree as Et

url = "http://localhost:9000"

# data = "<ENVELOPE><HEADER><VERSION>1</VERSION><TALLYREQUEST>EXPORT</TALLYREQUEST><TYPE>COLLECTION</TYPE><ID>List of Ledgers</ID>"
# data += "</HEADER><BODY><DESC><STATICVARIABLES><SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT></STATICVARIABLES></DESC></BODY></ENVELOPE>"

data = '<ENVELOPE> 	<HEADER><VERSION>1</VERSION><TALLYREQUEST>Export</TALLYREQUEST>    		<TYPE>Collection</TYPE><ID>All Sales Vchs</ID> 	</HEADER><BODY><DESC><STATICVARIABLES>					</STATICVARIABLES><TDL><TDLMESSAGE><COLLECTION NAME="All Sales Vchs" ISMODIFY="No">			<TYPE>Vouchers : Voucher Type</TYPE><CHILDOF>$$VchTypeSales</CHILDOF><BELONGSTO>Yes</BELONGSTO><FETCH>*, LedgerEntries.*, Inventory Entries.*</FETCH></COLLECTION></TDLMESSAGE></TDL></DESC></BODY></ENVELOPE>'

request = requests.post(url=url, data=data)

response = request.text.strip().replace("&amp;", "and")
print(response)
