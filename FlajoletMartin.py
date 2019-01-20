"""
Created on Wed Dec  5 20:59:18 2018

@author: akash
"""

import mmh3
import math
from statistics import median

# Number of hash functions
k = 10
# Data structure to store tailing zeroes
tail = [0] * k

# Function to return number of trailing zeroes
def trailingZeros(n):
	s = str("{:032b}".format(n))
	return len(s)-len(s.rstrip('0'))

# Input files
files = ['quotes_2008-08.txt', 'quotes_2008-09.txt', 'quotes_2008-10.txt', 'quotes_2008-11.txt',
         'quotes_2008-12.txt', 'quotes_2009-01.txt', 'quotes_2009-02.txt', 'quotes_2009-03.txt',
         'quotes_2009-04.txt' ]

# Reading quotes from the files
for file in files:
    with open(file) as f:
        for line in f:
            if(line[0] == 'Q'):
                quote = line.split('\t')[1][:-1]
                
                for i in range(k):
                    hashVal = abs(mmh3.hash(quote, i))
                    TZ = trailingZeros(hashVal)
                    tail[i] = max(tail[i], TZ)
                
# Dividing the number of hash functions in two groups and 
# calculating the average

# Calculating sum and average of group1
group1 = 0
for i in range(k//2):
    group1 += 2**(tail[i])
group1 = group1 / (k//2)

# Calculating sum and average of group2
group2 = 0
for i in range(k//2, k):
    group2 += 2**(tail[i])
group2 = group2 / (k//2)

# Calculating median of two groups

print("================================================================")
print("Estimated count of distinct elements is: ", math.floor(median([group1, group2])))
print("================================================================")


"""
Output:
    
================================================================
Estimated count of distinct elements is: 214748364
================================================================

"""
