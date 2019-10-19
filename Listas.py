l = [2, "tres", True,["uno", 10]]
l2 = l[0]
l3 = l[3][0]
l[1] = 4
l4 = l[0:3:2]
l5 = l[1::2]
l[0:2] = [3]
l6 = l[-1]

print l
print l2
print l3
print l[1]
print l4
print l5
print l[0:2]
print l6

tryal = [1,2,3,4,5,6,7,8,9,0]

print tryal
print len(tryal)

tryal.append(11)

print tryal
print len(tryal)

tryal.remove(5)
indexof3 = tryal.index(3)

print "index of 3 is " + str(indexof3)

tryal.pop(indexof3)

print tryal
print len(tryal)