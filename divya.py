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





