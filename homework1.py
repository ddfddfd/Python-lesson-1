country_capitals={"pakistan":"islamabad" ,"india":"New Delhi","france":"paris","USA":"Washington DC","Japan":"Tokyo"}
print(country_capitals)
print(country_capitals.keys())
print(country_capitals.values( ))
#find if france in country capitals or no
if "france" in country_capitals:
    print("yes its capital is ",country_capitals["france"])
else:
    print("no france isnt in the caiptals")
#delete france from the dictionary
del country_capitals["france"]
print(country_capitals)
if "france" in country_capitals:
    print("yes its capital is ",country_capitals["france"])
else:
    print("no france isnt in the caiptals")
#add france back
country_capitals["france"]="paris"
print(country_capitals)