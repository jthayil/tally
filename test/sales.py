import csv
import requests
import xml.etree.ElementTree as ET


def loadRSS():
    request_url = 'http://localhost:9000'
    request_data = '<ENVELOPE> 	<HEADER><VERSION>1</VERSION><TALLYREQUEST>Export</TALLYREQUEST><TYPE>Collection</TYPE><ID>All Sales Vchs</ID> 	</HEADER><BODY><DESC><STATICVARIABLES></STATICVARIABLES><TDL><TDLMESSAGE><COLLECTION NAME="All Sales Vchs" ISMODIFY="No"><TYPE>Vouchers : Voucher Type</TYPE><CHILDOF>$$VchTypeSales</CHILDOF><BELONGSTO>Yes</BELONGSTO><FETCH>*, LedgerEntries.*, Inventory Entries.*</FETCH></COLLECTION></TDLMESSAGE></TDL></DESC></BODY></ENVELOPE>'

    resp = requests.post(url=request_url, data=request_data)
    with open('output.xml', 'w') as f:
        f.write(resp.text)


def parseXML(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    newsitems = []
    for item in root.findall('./channel/item'):
        news = {}
        for child in item:
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')
        newsitems.append(news)
    return newsitems


def savetoCSV(newsitems, filename):
    fields = ['guid', 'title', 'pubDate', 'description', 'link', 'media']
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(newsitems)


def main():
    loadRSS()
    newsitems = parseXML('topnewsfeed.xml')
    # savetoCSV(newsitems, 'topnews.csv')


if __name__ == "__main__":
    main()
