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


# 1.5 Implementing a Priority Queue - sorts items by a given priority

import heapq
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

# To be able to compare the queue consists of tuples of the form (-priority, index, item).
a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))


# 1.6. Mapping Keys to Multiple Values in a Dictionary
# a so-called “multidict” - you need to store the multiple values in another container such as a list or set.

d = {
 'a' : [1, 2, 3],
 'b' : [4, 5]
}
e = {
 'a' : {1, 2, 3},
 'b' : {4, 5}
}

# Use a list if you want to preserve the insertion order of the items. 
# Use a set if you want to eliminate duplicates (and don’t care about the order).
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
        d[key].append(value)
# Using a defaultdict simply leads to much cleaner code:
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
# This recipe is strongly related to the problem of grouping records together in data pro‐
# cessing problems. See Recipe 1.15 for an example.

#One caution with defaultdict is that it will automatically create dictionary entries for
# keys accessed later on (even if they aren’t currently found in the dictionary). If you don’t
# want this behavior, you might use setdefault() on an ordinary dictionary insteadwarning it always creates a new instance of the initial value on each invocation (the empty list [] in the example).
d = {} # A regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)


# 1.7. Keeping Dictionaries in Order - create a dictionary, and you also want to control the order of items when
# iterating or serializing. --> Collections in Python containers that are used to store collections of data
from collections import OrderedDict
# Note for extra memory overhead more than twice as large as normal dictionary due to extra linked list created.
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
 print(key, d[key])
# self note from JS background - collections is kinda like lodash - really common NON built in functionality added to python 
import json
json.dumps(d)
>>>'{"foo": 1, "bar": 2, "spam": 3, "grok": 4}'
# build it in order to control the order of fields appearing in a JSON encoding,


# 1.8. Calculating with Dictionaries
prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')
# Similarly, to rank the data, use zip() with sorted(), as in the following:
prices_sorted = sorted(zip(prices.values(), prices.keys()))
# be aware that zip() creates an iterator that can only be consumed once. For example, the following code is an error:
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names)) # OK
print(max(prices_and_names)) # ValueError: max() arg is an empty sequence
# It should be noted that in calculations involving (value, key) pairs, the key will be used to determine the result in instances where multiple entries happen to have the same
#value. For instance, in calculations such as min() and max(), the entry with the smallest or largest key will be returned if there happen to be duplicate values. For example:
prices = { 'AAA' : 45.23, 'ZZZ': 45.23 }
min(zip(prices.values(), prices.keys()))
(45.23, 'AAA')
max(zip(prices.values(), prices.keys()))
(45.23, 'ZZZ')

# 1.9. Finding Commonalities in Two Dictionaries
a = {
 'x' : 1,
 'y' : 2,
 'z' : 3
}
b = {
 'w' : 10,
 'x' : 11,
 'y' : 2
}

# Find keys in common
a.keys() & b.keys() # { 'x', 'y' }
# Find keys in a that are not in b
a.keys() - b.keys() # { 'z' }
# Find (key,value) pairs in common
a.items() & b.items() # { ('y', 2) }
# Alter or filter dictionary contents
# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# c is {'x': 1, 'y': 2}
# A little-known feature of keys views is that they also support common 
# set operations such as unions, intersections, and differences. 
# if you use values() does not contain the operations above so if you must perform such calculations, they
# can be accomplished by simply converting the values to a set first.
