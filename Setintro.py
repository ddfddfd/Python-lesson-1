sample_list = [1,1,2,2,3,3]
print(sample_list)
sample_set = set(sample_list)
print(sample_set)
#sets can store multiple unique values that means it will not store duplicates.

#check if 4 exixts in the set
if 4 in sample_set:
    print("yes its in the set")
else:
    print("its not in the set")
if 3 in sample_set:
    print("yes it in the set")
else:
    print("no its not in the set")

#create an empty set
set1=set()
#add
set1.add("mango")
set1.add("watermelon")
set1.add("oranges")
set1.add("apple")
set1.add("bannana")
print(set1)
#remove and item
set1.remove("apple")
print(set1)



a={1,2,3,4,5}
b={4,5,6,7,8}
print(a.union(b))#it will have all unique values from sets
print(a.intersection(b))#it will show only common values
print(a.difference(b))#keeps values of a and remove common that is in b;
print(b.difference(a))