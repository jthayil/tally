from requests import request
from xml.etree import ElementTree as Et


def submit_click(from_dt, to_dt):
    xml = "<ENVELOPE><HEADER><VERSION>1</VERSION><TALLYREQUEST>EXPORT</TALLYREQUEST><TYPE>DATA</TYPE><ID>DayBook</ID></HEADER><BODY><DESC><STATICVARIABLES><SVEXPORTFORMAT>$$SysName:XML</SVEXPORTFORMAT><SVFROMDATE TYPE='DATE'>" + from_dt + "</SVFROMDATE><SVTODATE TYPE='DATE'>" + to_dt + "</SVTODATE></STATICVARIABLES></DESC></BODY></ENVELOPE>"
    daybook_res = get_data(xml)
    print(daybook_res)
    amount = 0
    for vch in daybook_res.findall("./BODY/DATA/TALLYMESSAGE/VOUCHER"):
        if len(vch.findall("ALLLEDGERENTRIES.LIST")) == 0:
            amount = vch.findall("LEDGERENTRIES.LIST").__getitem__(
                0).find("AMOUNT").text
        else:
            amount = vch.findall("ALLLEDGERENTRIES.LIST").__getitem__(
                0).find("AMOUNT").text
        print(vch, amount)


def get_data(payload):
    req = request("GET", url="http://localhost:9000", data=payload)
    print(req)
    res = req.text.encode("UTF-8")
    return Et.fromstring(res)


submit_click("01-11-2021", "30-11-2021")
