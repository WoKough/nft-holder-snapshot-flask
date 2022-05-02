#!/usr/bin/env python3
import requests
import sys
import json

url = 'https://deep-index.moralis.io/api/v2/nft/'
contract_address = sys.argv[1]
API_KEY = sys.argv[2]
chain = 'polygon'
formats = 'decimal'

require_url = url + contract_address + '/owners?chain=' + chain + '&format=' + formats


if __name__ == '__main__':
    headers = {
        'X-API-Key': API_KEY,
    }
    response = requests.request("GET", require_url, headers=headers)
    result = response.json()['result']
    for item in result:
        print ('####################')
        print ('contract_type: %s' % item['contract_type'])
        print ('Collection: %s' % item['name'])
        if type(item['metadata']) == str:
            print ('Name: %s' % json.loads(item['metadata'])['name'])
        else:
            print('Name: None')
        print ('token_address: %s' % item['token_address'])
        print ('owner_of: %s' % item['owner_of'])

