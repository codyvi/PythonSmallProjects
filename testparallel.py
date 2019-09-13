import collections
import multiprocessing
import os
import time
from pprint import pprint

Student = collections.namedtuple('Student', [
    'name',
    'semester',
    'grade',
    'id'
])

Students = (
    Student(name='David', semester='5', grade='100',id=822455),
    Student(name='Pepe', semester='6', grade='80',id=822456),
    Student(name='Paco', semester='4', grade='60',id=822457), 
)

pprint(Students)
print()
#single processing in cpu one core
# we can proccess many in parallel it is faster
def transform(x):
    print(f'Processing {os.getpid()} on {x.name}')
    time.sleep(1)
    result = {'name': x.name, 'id': x.id}
    print(f'Done processing {os.getpid()} on {x.name}')
    return result

#this calculates how much time did it took to run the function
start =time.time()

#multi processing processes = number of processes
pool = multiprocessing.Pool()
result = pool.map(transform, Students)
end = time.time()

print(f'Time elapsed: {end - start}')

pprint(result)