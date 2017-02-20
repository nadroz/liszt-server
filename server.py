import json
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request
from service.address_service import email_address_service

app = Flask(__name__)
CORS(app)


@app.route('/health')
def health():
    return json.dumps({'status': 'all good', 'code': '200'})


@app.route('/email-addresses/<email>', methods=['ADD', 'DELETE'])
def handle_email(email):
    service = email_address_service()
    if request.method == 'ADD':
        service.add_address(email)
        return json.dumps({'status': 'success', 'code': '200'})

    if request.method == 'DELETE':
        service.remove_address(email)
        return json.dumps({'status': 'success', 'code': '200'})


@app.route('/email-addresses')
def get_addresses():
    service = email_address_service()
    addresses = service.get()
    return json.dumps({'code': '200', 'status': 'success', 'addresses': addresses})
