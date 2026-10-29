"""Q6: CRUD on employee dictionary"""
employees={}
while True:
    c=input('1 Add 2 View 3 Update 4 Delete 0 Exit: ')
    if c=='1': employees[input('ID: ')]={'name':input('Name: '),'salary':input('Salary: ')}
    elif c=='2': print(employees)
    elif c=='3':
        k=input('ID: ')
        if k in employees: employees[k]['salary']=input('New salary: ')
    elif c=='4': employees.pop(input('ID: '),None)
    elif c=='0': break
