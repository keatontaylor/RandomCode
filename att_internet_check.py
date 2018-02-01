""" Will check the provided address and apartment number for att service
    and return the JSON string containing the services offered and other
    data normally returned to the website lookup page.
"""

from datetime import datetime

import json
import queue
import urllib.request

street = '123 Somewhere Drive'
apt = ''
zip = '555555'


jsoncontent = {'Content-Type': 'application/json'}

url = "https://www.att.com/services/shop/model/ecom/shop/view/unified/qualification/service/CheckAvailabilityRESTService/invokeCheckAvailability"
postdata = json.dumps({
    'userInputZip': zip,
    'userInputAddressLine1': street,
    'userInputAddressLine2': apt,
    'mode': 'fullAddress'}).encode(encoding='utf-8')
req = urllib.request.Request(url=url, data=postdata, headers=jsoncontent, method='POST')
resp = urllib.request.urlopen(req)
respobj = json.loads(resp.read().decode('utf-8'))
print(json.dumps(respobj, indent=4))
