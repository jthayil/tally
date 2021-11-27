import requests
import xml.etree.ElementTree as ET
import xml


def get_xml():
    request_url = 'http://localhost:9000'
    request_data = '<ENVELOPE> 	<HEADER><VERSION>1</VERSION><TALLYREQUEST>Export</TALLYREQUEST><TYPE>Collection</TYPE><ID>All Sales Vchs</ID> 	</HEADER><BODY><DESC><STATICVARIABLES></STATICVARIABLES><TDL><TDLMESSAGE><COLLECTION NAME="All Sales Vchs" ISMODIFY="No"><TYPE>Vouchers : Voucher Type</TYPE><CHILDOF>$$VchTypeSales</CHILDOF><BELONGSTO>Yes</BELONGSTO><FETCH>*, LedgerEntries.*, Inventory Entries.*</FETCH></COLLECTION></TDLMESSAGE></TDL></DESC></BODY></ENVELOPE>'
    response = requests.post(url=request_url, data=request_data)
    with open('output.xml', 'w') as f:
        f.write(str(response.text))
    return ET.fromstring(response.text.replace("&#4;","").replace("UDF:","UDF."))


def get_children(parent):
    for i, child in enumerate(parent.iter()):
        print(i, child.tag, child.attrib, child.text)


def main():
    root = get_xml()
    get_children(root)


if __name__ == "__main__":
    main()
