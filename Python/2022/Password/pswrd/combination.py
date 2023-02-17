import itertools
from itertools import combinations 
  
def combine(arr, s): 
    return list(combinations(arr, s)) 

array = ['a', 'b', 'c', 'd'] 
set = 3
print(combine(array, set))


st = "1234"
 
per = itertools.permutations(st)
 
for val in per:
    print(*val)
