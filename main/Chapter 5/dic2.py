marks = {
    "daksh": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "daksh"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"daksh": 99, "Renuka": 100})
# print(marks)
print(marks.get("daksh")) # Prints None
print(marks.get("daks")) # Prints None
print(marks["Harry2"]) # Returns an error