import numpy as np
# arr=np.array([1,2,3,4,5,6,])
# new=arr.reshape(2,3)
# print(new)


# arr=np.array([[1,2,3],[4,5,6]])
# print(arr.ravel())#return view disrtub orginal  
# print("--------------")
# print(arr.flatten()) #return copy dont distrub orginal 



# arr = np.array([1,2,3,4,5,6])
#arry,index,value,asxis=none
#asxis=none
#axis = 0 rows wise 
#axis = 1 coloum wise
# new=np.insert(arr,6,[1,2,3])
# print(new)


#2d array 
# arr = np.array([[1,2],[3,4]])
# new1 = np.insert(arr,2,[5,6],axis=None)
# print(new1)
# print("------------------------------")
# new2 = np.insert(arr,2,[5,6],axis=0)
# print(new2)
# print("---------------------------")
# new3 = np.insert(arr,2,[5,6],axis=1)
# print(new3)




# #append at the end 
# arr = np.array([1,2,3,4,5,6])
# new = np.append(arr,[9,7,6])
# print(new)


# concate adding two array 
# #np.concatenate((1,2),axis=0) in the form of tuple
# arry1=np.array([1,2,3])
# arry2=np.array([4,5,6])
# new = np.concatenate((arry1,arry2))
# print(new)


#removing element of an array 
#delete () 
#np.delete (arr,index,axis=none)
#flattern arry 
# arr = np.array([1,2,3,4,5,6])
# new = np.delete(arr,0,axis=None)
# print(new)

#2d array 
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)
# new = np.delete(arr,0,axis=0)
# print(new)
"""
stacking 
vertically 
horizontally

vstack() row wise 
hstack() coloum wise
"""
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(np.vstack((arr1,arr2)))
print("-------------------")
print(np.hstack((arr1,arr2)))


"""
spliting 
np.split() equal 
np.hsplit()
np.vsplit()
"""
# arr = np.array([[1,2,3],[4,5,6]])
# # print(np.split(arr,2))
# print("-----------")
# print(np.vsplit(arr,1))
# print("-----------")
# print(np.hsplit(arr,1))



"""
chapter 5 
broadcasting and vectorization 
"""

