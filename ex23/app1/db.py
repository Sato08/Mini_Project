products = [
    {
        'id': 1,
        'code': '1001',
        'name': 'Cosy',
        'unitPrice': '45000'
    },
    {
        'id': 2,
        'code': '1002',
        'name': 'One One',
        'unitPrice': '27000'
    }
]

def getProducts():
    return products

def addProduct(code, name, unitPrice):
    if len(products) == 0:
        id = 1
    else:
        id = products[-1]['id'] + 1
    products.append({
        'id': id,
        'code': code,
        'name' : name,
        'unitPrice': unitPrice
    })

def deleteProduct(id):
    for prod in products:
        if prod['id'] == id:
            products.remove(prod)

def findById(id):
    for prod in products:
        if prod['id'] == id:
            return prod

def updateProduct(id, code, name, unitPrice):
    #TODO homework
    product = findById(id)
    if product:
        if code != None: product['code'] = code
        if name != None: product['name'] = name
        if unitPrice != None: product['unitPrice'] = unitPrice



