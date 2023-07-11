from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1/production-line/start', methods=['POST'])
def start_production_line():
    request_payload = request.get_json()
    if not request_payload:
        return jsonify({'error': 'Invalid request payload'}), 400

    product_id = request_payload.get('productId')
    quantity = request_payload.get('quantity')

    if not product_id or not quantity:
        return jsonify({'error': 'Missing required fields'}), 400

    if quantity < 1 or quantity > 10000:
        return jsonify({'error': 'Invalid quantity'}), 400

    # Logic to start the production line

    return jsonify({'message': 'Production line started successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
