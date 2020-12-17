# MASTERING PYTHON3 - Cookbook
# Master built in data structures such as lists, sets, dictionaries 
# working with data - searching, sorting, ordering, filtering, and using collections.

# Unpacking - taking an iterable and putting each value into its own variable

#1.1
data = [43.2, 90.2, (932,45,54)]
a,b,c = data 
_, b, _ = data #using dummy variables for some of the values not needed

#1.2 - Unpacking with iterables with arbitrary length 
record = ('Frank', 'frank@gmail.com', '333-444-6666', '999-333-5543')
name, email, *phone_numbers, = record
# PATTERN NOTE: 1. used powerfully with string processing
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
# PATTERN NOTE: 2. used with unpacking tuples of different lengths 
# PATTERN NOTE: 3. used for createing throw away variables with unwanted items in the unpack
# PATTERN NOTE: 4. ex: clever for list-processing liek maybe split into a head, tail, then recursively iterate 

#PATTERN NOTE: Similar pattern as deconstruction in ES6 as follows:
#   const data = [43.2, 90.2, [932,45,54]]
#   const [salesAvg, avg, sales] = data

#1.3 - Keeping the last N items during iteration or some processing 
from collections import deque
# queue performs better than doing this with a list 
def search(lines, pattern, history=5):
    # deque(maxlen=history) creates a fixed size queue - why does this remind me of caching and memoize
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
           yield line, previous_lines
        previous_lines.append(line)   
# Example use on a file 
if __name__ == '__main__':
      with open('somefile.txt') as f:
          for line, prevlines in search(f, 'python', 5):
              for pline in prevlines:
                  print(pline, end='')
              print(line, end='')
              print('-'*20)    
# extended note: using generators with yield for searching and decoupling the process of searching from the code that uses the results

#1.4 Finding the largest or smallest N Items
import heapq 
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]
portfolio = [
 {'name': 'IBM', 'shares': 100, 'price': 91.1},
 {'name': 'AAPL', 'shares': 50, 'price': 543.22},
 {'name': 'FB', 'shares': 200, 'price': 21.09},
 {'name': 'HPQ', 'shares': 35, 'price': 31.75},
 {'name': 'YHOO', 'shares': 45, 'price': 16.35},
 {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# if N is small compared to the overall size of the collection, these functions provide superior performance 
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
# (N=1), it is faster to use min() and max() AND  when N is close to the size of the collection then this is usually faster, sorted(items)[:N] or sorted(items)[-N:])
# this works by converting the data to a list ordered as a heap ie heap[0] is always the smallest item
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq
heap = list(nums)
heapq.heapify(heap)
heap #[-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8] can use heapq.heappop() to get next smallest on the first item



