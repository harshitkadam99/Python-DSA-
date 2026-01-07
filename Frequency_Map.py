# Store Frequency in the dictionary 
nums = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5]
frequency_map = {}         #{}/dict()#
for i in range (0,len(nums)):
    if nums[i] in frequency_map:
        frequency_map[nums[i]]+=1
    else:
        frequency_map[nums[i]]=1
print(frequency_map)
print(frequency_map[5])


nums = [1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5]
hash_map = dict()
n = len(nums)
for i in range(0,n):
   hash_map[nums[i]]= hash_map.get (nums[i],0) + 1
print(hash_map)
print(hash_map[2])
 