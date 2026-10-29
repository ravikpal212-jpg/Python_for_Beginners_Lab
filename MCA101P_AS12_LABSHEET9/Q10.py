"""Q10: CRUD records in JSON file"""
import json, os
file='records.json'
data=json.load(open(file)) if os.path.exists(file) else []
while True:
    c=input('1 Add 2 View 3 Modify 4 Delete 0 Exit: ')
    if c=='1': data.append({'id':input('ID: '),'value':input('Value: ')})
    elif c=='2': print(data)
    elif c=='3':
        k=input('ID: ')
        for r in data:
            if r['id']==k: r['value']=input('New value: ')
    elif c=='4': data=[r for r in data if r['id']!=input('ID: ')]
    elif c=='0': break
with open(file,'w') as f: json.dump(data,f,indent=2)
