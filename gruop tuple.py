print("Enter details for 5 gruops")
for i in range(1,6):
    print(f"Enter the details for group {i}:")
    groupname=input("Group name:")
    total_students=input("Total no. of students:")
    girls=input("How many girls:")
    boys=input("How many boys:")
    record=(groupname,total_students,girls,boys)
    print(record)