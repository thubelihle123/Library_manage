"""The libraries is using the codes 14, 15, 16, 17, 18, 19, 20 to all programming related books:
§ Create a normal and comprehensive list that will display the codes.
§ Create a normal and comprehensive list that will add the codes together for auditing purpose.
§ Create a normal and comprehensive list that will display only codes that are tracked by odd 
numbers.
§ Create a set to display the list of codes"""

codes = [14, 15, 16, 17, 18, 19, 20]

#Create a normal and comprehensive list that will display the codes.
codeN = []
for c in codes:
    codeN.append(c)
print(codeN)


codeC = [c for c in codes]
print(codeC)

#Create a normal and comprehensive list that will add the codes together for auditing purpose.
addCodeN = []
sum =0
for N in codes:
    sum = sum +N
    addCodeN.append(sum)

print(addCodeN)

sum =0
addCodeC = [sum + NComp for NComp in codes]
print(addCodeC)

#Create a normal and comprehensive list that will display only codes that are tracked by odd numbers.
oddCodeN = []
for oN in codes:
    if oN%2 != 0:
        oddCodeN.append(oN)
print(oddCodeN)

oddCodeC = [oc for oc in codes if oc%2 !=0]
print(oddCodeC)

#Create a set to display the list of codes
setN =set(codes)
print(setN)