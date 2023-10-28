# def binarySearch(start,end,target):
#     while start<=end :
#         mid=(start+end)//2
#         if mid == target :
#             return mid
#         elif mid < target :
#             start = mid + 2
#         else:
#             end = mid - 2
#     return None






# function displays the numbers with difference 2
def binarySearch(start,end):
    for val in range(start,end,2):
        print(val,end=" ")

# taking input for the interval 
Range=int(input("\nEnter range from 0 - : "))
# even values starts from 0 
print(f"\nValues start from 0 ")
binarySearch(0,Range+1)
# odd values starts from 1
print(f"\n\nValues start from 1 ")
binarySearch(1,Range)




# target=int(input("Enter target value  : "))
# if target > 0 and target < Range+1 :
#     result=binarySearch(0,Range,target)
#     if result is not None :
#         print(f"{target} is found with in range ")
#     else:
#         print(f"{target} is not found with in range ")
# else:
#     print(f"target is not in given range ")
