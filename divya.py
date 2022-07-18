'''s1 = {'a', 'b', 'c', 'd'}
s2 = ['a', 'b', 'c', 'd']
print(s1)
print(s2)
print(type(s1))
print(type(s2))


a_list=print(['a','b','mpiligrim','true','false','42'])
s=[]
s=print(set(range(1,6)))
s=print(set('reva'))
s.update({2,4,6})
print(s)
s.update([10,20,30])'''

'''s1={2,4,6,8}
s2={1,3,5,7}
s1.update(s2)
print(s1)
s1.pop()
print(s1)
s1.pop()
print(s1)
s1.remove(4)
print(s1)
s1.discard(2)
print(s1)
s1.clear()
print(s1)
print(len(s1))'''

'''s1={1,2,3,4,5}
for i in s1:
    print(i)'''

'''s1={1,2,3}
s2=s1
print(s2)
s2.remove(2)
print(s2)
print(s1)'''


'''s3={2,3,4,5}
s4=s3.copy()
print(s4)
s4.remove(3)
print(s4)
print(s3)'''

#python operations

'''s1={1,2,3}
s2={4,5,6}
print(s1.union(s2))'''

'''s1={1,2,3}
s2={4,5,6}
print(s1|s2)'''

'''s1={1,2,3}
s2={4,5,6}
print(s1.intersection(s2))'''

'''s1={1,2,3}
s2={4,5,6}
print(s1 & s2)'''

'''s1={1,2,3}
s2={4,5,6}
print(s1.difference(s2))'''

'''s1={1,2,3}
s2={4,5,6}
print(s1 - s2)'''

'''s1={1,2,3}
s2={4,5,6}
print(s1.symmetricdifference(s2))'''

'''s1={1,2,3}
s2={4,5,6}
print(s1^s2)'''

#disjoint set

'''s1={1,2}
s2={2,3}
print(s1.isdisjoint(s2))'''

'''s1={1,2,3}
s2={4,5,6}
print(s1.isdisjoint(s2))'''

print({1,2}.issubset({2,3}))
print({1,2}.issuperset({2,3}))

print({1,2}.issubset({1,2,3}))
print({1,2}>={1,2,3})




#6/7/22
import re
string="python is fun"
s=re.match('python',string)
print(s)
'''
'''
import re
txt="my name is divya"
x=re.findall("[a-m]",txt)
print(x)
'''
'''
import re
txt="acd"
x=re.findall("..",txt)
print(x)
'''
'''
import re
pattern='^b...s$'
test_string='basds'
result=re.search(pattern,test_string)
print(result)
'''
'''
import re
input='aaa'
result=re.sub('^a','b',input)
print(result)
'''
'''
import re 
input='sdsf'
s=re.sub('s','n','sdsf',1)
print(s)
'''
import re 
input='sdsf'
s=re.subn('s','n','sdsf',1)
print(s)
import re 
input='sdsf'
s=re.subn('s','n','sdsf',1)
print(s)
'''
'''
import re 
input='dnvr'
s=re.findall('d','dnvr')
print(s)
'''
import re 
txt='drsxhygyt'
s=re.split('x','txt')
print(s)
import re 
pattern='\w+'
s1='divya'
s2='sri'
s3='bhoomi'
a=re.search(pattern,s1)
b=re.search(pattern,s2)
c=re.search(pattern,s3)
print(a)
print(b)
print(c)


#11-7-22
import re
txt="the rain in spain"
x=re.search("ai",txt)
print(x)    #this will return an object

import re
txt="the rain in spain"
x=re.findall("ai",txt)
print(x) 

import re
txt="the rain in spain"
x=re.split("ai",txt)
print(x) 


import re
x=re.split('ai',"the rain in spain")
print(x)

import re
txt="the rain in spain"
x=re.sub('ai','AI',txt)
print(x) 


import re
txt="the rain in spain"
x=re.sub("[ai]",'AI',txt)
print(x) 

#metacharacters
# 1. []
import re
txt="the rain in spain"
x=re.findall("[ai]",txt)
print(x) #metacharacter square bracket will match for both a and i 

import re
txt="the rain in spain"
x=re.findall("[a-i]",txt)
print(x)

import re
txt="the rain in  sp9ain 1236439"
x=re.findall("[0-9]",txt)
print(x)

# 2.\
import re
txt="the rain in spain 123"
x=re.findall("\d",txt)
print(x)

import re
txt="the rain in spain"
x=re.findall("\n",txt)
print(x)

# 3- .
import re 
txt="the rain in spain"
x=re.findall("sp..n",txt)
print(x)

import re 
txt="the rain in spain"
x=re.findall("s...n",txt)
print(x)

import re 
txt="the rain in spain"
x=re.findall("r.....",txt)
print(x)

import re 
txt="the rain in sp79n"
x=re.findall("sp..n",txt)
print(x)

import re 
txt="the rain in spain"
x=re.findall("r.....s",txt)
print(x)

# 4-^  (cap or caret symbol)   checks foe starting character
import re 
txt="abc"
x=re.findall("^a",txt)
print(x)

import re 
txt="bac"
x=re.findall("^a",txt)
print(x)

import re 
txt="abc"
x=re.findall("^ab",txt)
print(x)

# 5-$ (ends with)
import re 
txt="abc"
x=re.findall("$ab",txt)
print(x)

import re 
txt="abc"
x=re.findall("c$",txt)
print(x)

import re 
txt="abc"
x=re.findall("bc$",txt)
print(x)

import re
txt='the rain in spain'
x=re.findall("n$",txt)
print(x)

import re
txt='the rain in spaid'
x=re.findall("n$",txt)
print(x)

# 6-*(zero or more occurance)
# 7- +(one or more occurance)
# 8- ?(zeo or one occurance)


#13-07-22
class _318:
    bench = 100  #attribute
    monitor = 1
    def learn():
        print("hi divya")
print(_318.bench)
print(_318.monitor)
print(_318.learn)

a = _318
print(a.bench)
print(a.monitor)

a.learn()
 
class MyClass:
    'this is my second class'
    a=10
    def func(self):
        print("hii sri")
print(MyClass.__doc__)

#18/07/22
'''class student:
    srn=15'''
    
#init is used to initialize the class
class student:
    def __init__(self,srn,name):
        self.srn=srn
        self.name=name
    def display(self):
        print("my name is {1} and srn is {0}".format(self.name,self.srn))
p1=student("divzz","r21ef215")
p1.display()
s1=student("R21EF215","divya")
print(s1.srn)
print(s1.name)