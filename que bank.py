my_tuple=()
print(my_tuple)

my_tuple=(1,2,3)
print(my_tuple)

my_tuple=(1,"hello",3.4)
print(my_tuple)

my_tuple=("mouse",[8,4,6],(1,2,3))
print(my_tuple)

# max and min k value using python
my_tuple = (7, 25, 36, 9, 6, 8)

print("The tuple is : ")
print(my_tuple)

K = 2
print("The value of K has been initialized to ")
print(K)
my_result = []
my_tuple = list(my_tuple)
temp = sorted(my_tuple)

for idx, val in enumerate(temp):
   if idx < K or idx >= len(temp) - K:
      my_result.append(val)
my_result = tuple(my_result)

print("The result is : " )
print(my_result)



def Findel(tup,K):
    tup = list(tup)
    temp = sorted(tup)
    result = tuple(temp[:K] + temp[-K:])
  
    print("Max and Min K elements : ",result)
tup = (13, 10, 23, 2, 5, 6, 12, 7, 1, 8)
K = 3
print("The original tuple: ", tup)
Findel(tup,K)