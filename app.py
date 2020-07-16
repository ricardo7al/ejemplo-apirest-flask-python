from flask import Flask, jsonify, request
app = Flask(__name__)

from products import products


@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})

@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "Lista de productos"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    productsFound = [product for product in products if product['nombre'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "product not found"})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "nombre": request.json['nombre'],
        "precio": request.json['precio'],
        "cantidad":request.json['cantidad']
    }
    products.append(new_product)
    return jsonify({"message": "producto agregado correctamente", "productos": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product['nombre'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['nombre'] = request.json['nombre']
        productsFound[0]['precio'] = request.json['precio']
        productsFound[0]['cantidad'] = request.json['cantidad']
        return jsonify ({
            "message": "Product Updated",
            "product": productsFound[0]
        })
    return jsonify ({"message": "Product not found"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['nombre'] == product_name]
    if (len(productsFound) > 0):
        products.remove(productsFound[0])
        return jsonify({
            "message": "Product deleted",
            "products": products
        })
    return jsonify({"message": "product not found"})


if __name__ == '__main__':
    app.run(debug=True, port=5000)