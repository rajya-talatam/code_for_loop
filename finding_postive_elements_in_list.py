list1 = [12, -7, 5, 64, -14]
newlist = []
for i in list1:
    if i > 0:
        newlist.append(i)
newlist1 = [str(element) for element in newlist]
print(",".join(newlist1))