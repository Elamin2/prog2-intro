
print ("ta ett tall från användaren")

tal = input("skriv din tal: ") 

print ("Hej din tal är " + tal )

horses = [
    {"name": "seabiscuit", "age": 3, "color": "brown"},
    {"name": "black beauty", "age": 5, "color": "black"},
    {"name": "silver", "age": 4, "color": "white"},
    {"name": "shadowfax", "age": 7, "color": "grey"},
    {"name": "rocinante", "age": 6, "color": "white"}
]

for horse in horses:
    print(horse["name"], horse["age"], horse["color"])
    