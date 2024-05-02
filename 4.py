list = input().split()
diction = {
    'Jhon':input(),
    'Emma':input(),
    'Kelly':input(),
    'Jason':input(),
}

list2 = []
for i in list:
    for key,val in diction.items():
        if val == i:
            list2.append(i)
print(list2)