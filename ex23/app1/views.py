from django.shortcuts import render, redirect
from . import db

# Create your views here.
def index(request):
    return render(request, 'index.html',
                    context = {'products': db.getProducts()})

def saveProduct(request):
    id = request.POST['id']
    code = request.POST['code']
    name = request.POST['name']
    unitPrice = request.POST['unitPrice']

    print(code, name)
    if id.strip()=='':
        db.addProduct(code, name, unitPrice)
    else:
        db.updateProduct(int(id), code, name, unitPrice)
    return redirect('home')
        
def addProduct(request):
    return render(request, 'product.html')
def editProduct(request, id):
    product = next((p for p in db.products if p['id'] == id), None)
    context = {}
    context.update(product)
    return render(request, 'product.html', context = context)

def deleteProduct(request, id):
    db.deleteProduct(id)
    return redirect('home')

