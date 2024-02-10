from src.utils.classes import QRcode
from flask import Flask, request, jsonify
import base64
import time
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def getCode():
    if request.is_json:
        data = request.get_json()
        if 'link' not in data or (data['link'].strip() == ''):
            return jsonify({'message': 'Missing or empty link'}), 400

        try:
            timestamp = int(time.time())
            fileName = f'qrcode_{timestamp}'
            newCode = QRcode(data['link'], fileName)
            newCode.GenerateCode()

            with open(newCode.filePath, "rb") as img_file:
                imageBase64 = base64.b64encode(img_file.read()).decode('utf-8')

            os.remove(newCode.filePath)
            return jsonify({'message': 'success', 'qr_code_base64': imageBase64}), 200
        
        except Exception as e:
            return jsonify({'message': f'Error: {str(e)}'}), 500

    else:
        return jsonify({'message': 'Invalid JSON format'}), 415

if __name__ == '__main__':
    app.run(port=3000)
