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

#1.3 - Unpack with a * takes those items into a list

#1.4 


#PATTERN NOTE: Similar pattern as deconstruction in ES6 as follows:
#   const data = [43.2, 90.2, [932,45,54]]
#   const [salesAvg, avg, sales] = data


