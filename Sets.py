set1={1,2,3,4,5,6,7,8,9}
print(set1)

set2=set([1,2,3,4,5,6,7,8,9])
print(set2)

set3={2,2,2,1,2,3,2,4,2,5}
print(set3)

set4={"quiencia", "queenie", "quiety"}
set4.add("qutie")
print(set4)

#union
set5={1,2,3}
set6={3,4,5}
print(set5|set6)
print(set5.union(set6))

#intersection
set7={1,2,3}
set8={2,3,4}
print(set7 & set8)
print(set7.intersection(set8))