#import mimetypes
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import Response
from moralis_api_tool import get_contract_info, check_contract, change_to_csv
app = Flask(__name__)

@app.route('/')
def nftools(name=None):
    name = "nftools"
    return render_template('index.html', name=name)

@app.route('/contract', methods=['POST'])
def contract(name=None):
    name = "contract"
    if request.method == 'POST':
        contract = request.form['contract']
        if check_contract(contract) == True:
            #info = get_contract_info(contract)
            info = [{'contract_address':contract,'contract_type':'ECR 721', 
            'collection': 'heheda', 'token_address': '0xffffffffffffffff',
            'name': 'test', 'owner_of': '0xaaaaaaaaaaaaaaaaaaaaaaa'
            },]
            return render_template('output.html', result=info)
        else:
            return render_template('error.html')
    return "Bad Request!!!"

@app.route("/getcsv", methods=['POST'])
def getcsv(name=None):
    csv = ''
    if request.method == 'POST':
        contract = request.form['contract']
        if check_contract(contract) == True:
            #info = get_contract_info(contract)
            info = [{'contract_address':contract,'contract_type':'ECR 721', 
            'collection': 'heheda', 'token_address': '0xffffffffffffffff',
            'name': 'test', 'owner_of': '0xaaaaaaaaaaaaaaaaaaaaaaa'
            },]
            csv = change_to_csv(info)
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=%s.csv" % contract})

if __name__ == '__main__':
    app.run(debug=True)