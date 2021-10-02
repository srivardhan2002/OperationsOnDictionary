N = {1,5,3,2,6,0,9}
E = {2,3,4,6,8,9,0}
Intersection = set()
Union = set()
DifferenceOfEandN = set()
SymmetricDifferenceOfEandN = set()
for i in N:
    if i in E:
        Intersection.add(i)
print(Intersection)

for i in N:
    Union.add(i)
for i in E:
    if i not in Union:
        Union.add(i)
print(Union)

for i in E:
    if i not in N:
        DifferenceOfEandN.add(i)
print(DifferenceOfEandN)

for i in Union:
    if i not in Intersection:
        SymmetricDifferenceOfEandN.add(i)
print(SymmetricDifferenceOfEandN)
