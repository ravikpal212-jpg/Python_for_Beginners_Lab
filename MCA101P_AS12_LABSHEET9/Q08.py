"""Q8: CRUD product details"""
products={}
while True:
    c=input('1 Add 2 View 3 Update 4 Delete 0 Exit: ')
    if c=='1': products[input('ID: ')]={'name':input('Name: '),'price':float(input('Price: '))}
    elif c=='2': print(products)
    elif c=='3':
        k=input('ID: ')
        if k in products: products[k]['price']=float(input('New price: '))
    elif c=='4': products.pop(input('ID: '),None)
    elif c=='0': break
