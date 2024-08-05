list1=[1,2,3,4,5,6]
print(list1)
def swap(list1):
    size=len(list1)
    temp=list1[0]
    list1[0]=list1[size-1]
    list1[size-1]=temp
    print("after swap of first and last element ...")
    print(list1)
swap(list1)
