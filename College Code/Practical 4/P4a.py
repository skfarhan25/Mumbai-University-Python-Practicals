A = [0,2,4,6,8,10]
B = [1,3,5,6,8,9,10,0]

CommonList = [CommonNumber for CommonNumber in A if CommonNumber in B]
print(f"Common elements of List A and List B: {CommonList}")