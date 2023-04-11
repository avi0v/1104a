# tuple , immutable like list simialr function like string
#list.clear() - clear all element of list
a=list(range(11))
print(a)
a.clear()
print(a)

#new_list=list.copy() , similar 
"""CHANGE IN OLD LIST WILL NOT REFLECT IN NEW LIST"""
b=a.copy()
print(b)
print("b==a",a==b)
a.append("ddd")
print(a ,b )
print("b==a",a==b)

# tuple creating variable = (element , e2 , e3) 
'''element - anything even nested data structure'''
a=(1,23,4,4)
b=(9) # this is int not tuple
''' tuple wiht one elemnt = (element,)'''
c=(3,)
print(type(a),type(b),type(c))

#like string 
# concatnation is OK
# type conversions
# indirectly modify tuple . tup>list>modify>tup