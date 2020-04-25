arr = [9,7,9,4,3,9,5,2,1,0,6,3,0]
dict = {}
for i in arr:
  dict[i] = dict.get(i,0) + 1
lst = sorted(dict.items(), key = lambda t:t[1], reverse = True)
lst1 = []
for i in range(len(lst)):
    lst1.append(lst[i][0])
print(lst1)