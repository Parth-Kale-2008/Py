nums = [2,7,5,11]
target = 16
for i in range (len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j] == target:
            print(i,j)
            
    