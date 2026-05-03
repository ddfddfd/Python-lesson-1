planets=["mercury","venus","earth","mars","jupiter","saturn","uranus","neptune"]
set1=set(planets)
answer=input("enter a name of a planet in the solar system ")
if answer in set1:
    print("you answered correct")
else:
    print("you answered incorrectly")