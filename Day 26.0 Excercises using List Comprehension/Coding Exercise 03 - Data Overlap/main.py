with open("file1.txt") as file1:
    list1 = file1.readlines()

with open("file2.txt") as file2:
    list2 = file2.readlines()

result = [name for name in list1 if name in list2]
res = []
for sub in result:
    res.append(sub.replace("\n", ""))

print(res)