"""Q7: Menu-driven book CRUD"""
books=[]
while True:
    c=input('1 Add 2 View 3 Update 4 Delete 0 Exit: ')
    if c=='1': books.append({'id':input('ID: '),'title':input('Title: ')})
    elif c=='2': print(books)
    elif c=='3':
        k=input('ID: ')
        for b in books:
            if b['id']==k: b['title']=input('New title: ')
    elif c=='4': books=[b for b in books if b['id']!=input('ID: ')]
    elif c=='0': break
