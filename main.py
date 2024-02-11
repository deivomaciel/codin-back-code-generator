from src.utils.classes import QRcode
from flask import Flask, request, jsonify
import base64
import time
import os

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return "I'm alive!"

@app.route('/getqrcode', methods = ['POST'])
def getCode():
    if request.is_json:
        data = request.get_json()
        if 'link' not in data or (data['link'].strip() == ''):
            return jsonify({'message': 'Missing or empty link'}), 400

        try:
            timestamp = int(time.time())
            fileName = f'qrcode_{timestamp}'
            newCode = QRcode(data['link'])
            qrcodeBase64 =  newCode.GenerateCode()
            return jsonify({'message': 'success', 'qr_code_base64': qrcodeBase64}), 200
        
        except Exception as e:
            return jsonify({'message': f'Error: {str(e)}'}), 500

    else:
        return jsonify({'message': 'Invalid JSON format'}), 415

if __name__ == '__main__':
    app.run(port=3000)
