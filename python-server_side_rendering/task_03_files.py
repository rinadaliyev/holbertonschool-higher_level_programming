from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json(file_path='products.json'):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv(file_path='products.csv'):
    products = []
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert id to int and price to float
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception:
        pass
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products_list = []

    if source == 'json':
        products_list = read_json()
    elif source == 'csv':
        products_list = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source", products=None)

    if product_id:
        filtered = [p for p in products_list if p['id'] == product_id]
        if not filtered:
            return render_template('product_display.html', error="Product not found", products=None)
        products_list = filtered

    return render_template('product_display.html', products=products_list, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
