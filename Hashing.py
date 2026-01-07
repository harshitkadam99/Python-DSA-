# prestoring values into same datastructure like list/dictionary/set and then fetching it.

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
for num in m:
    count=0            #brute force
    for x in n:
        if x == num:
            count+=1
    print(count)


n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
hash_list = [0]*11
for num in n:
    hash_list[num] += 1        #optimal solution
for num in m:
    if num<1 or num>10:
        print(0)
    else:
        print(hash_list[num])


n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
hash_dic = {}
for num in n:
    if num in hash_dic:
        hash_dic[num] += 1.    #according to dictonary
    else:
        hash_dic[num] = 1
for num in m:
    if num in hash_dic:
        print(hash_dic[num])
    else:
        print(0)

#### character hashing
s = "azyxyyzaaaa"
q = ['d', 'a', 'y', 'x']

hash_list = {}

# Count frequency
for ch in s:
    ascii_val = ord(ch)
    index = ascii_val - 97
    if index in hash_list:
        hash_list[index] += 1
    else:
        hash_list[index] = 1

# Query frequencies
for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print(f"{ch} -> {hash_list.get(index, 0)}")

# Cleaner pythonic version
s = "azyxyyzaaaa"
q = ['d','a','y','x']

freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in q:
    print(f"{ch} -> {freq.get(ch, 0)}")





