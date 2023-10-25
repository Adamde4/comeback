list1 = []
list2 = []
list1.append(int(input("list 1: ")))
list2.append(int(input("list 2: ")))
sum_list = []
if len(list1) == len(list2):
    for i in range(len(list1)):
        sum_list.append((list2[i] * list1[i]))
    print(sum_list)
else: print('fall')