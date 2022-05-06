import requests
import sys
import json

def change_to_csv(infolist):
    csv = 'Token Address,Owner Address,Collection,Name,	Contract Type\n'
    for item in infolist:
        csv += "%s," % item['token_address']
        csv += "%s," % item['owner_of']
        csv += "%s," % item['collection']
        csv += "%s," % item['name']
        csv += "%s," % item['contract_type']
        csv += '\n'
    return csv

def check_contract(contract):
    if contract.startswith('0x') == False:
        return False
    elif len(contract) != 42:
        return False
    try:
        value = int(contract, 16)
    except ValueError:
        return False
    return True

def get_contract_info(contract):
    url = 'https://deep-index.moralis.io/api/v2/nft/'
    chain = 'polygon'
    formats = 'decimal'
    headers = {
        #'accept': 'application/json',
        'X-API-Key': 'q7jT2BZmjX9HnnYssLnJbm74NaSKl2hRz5C7VxV4xGXGynf4SQELa1AqAh0heK4g',
    }
    reslist = []
    info_url = url + contract + '/owners?chain=' + chain + '&format=' + formats
    response = requests.request("GET", info_url, headers=headers)
    result = response.json()['result']
    for item in result:
        itemdict = {}
        itemdict['contract_address'] = item['contract_address']
        itemdict['contract_type'] = item['contract_type']
        itemdict['collection'] = item['name']
        itemdict['token_address'] = item['token_address']
        if type(item['metadata']) == str:
            itemdict['name'] = json.loads(item['metadata'])['name']
        else:
            itemdict['name'] = 'None'
        itemdict['owner_of'] = item['owner_of']
        reslist.append(itemdict)
    return reslist
