"""Q5: Delete student by roll number"""
import json
try:
    with open('students.json') as f: data=json.load(f)
    roll=input('Roll to delete: '); new=[s for s in data if s['roll']!=roll]
    with open('students.json','w') as f: json.dump(new,f,indent=2)
    print('Deleted' if len(new)<len(data) else 'Roll not found')
except FileNotFoundError: print('Run Q01 first')
