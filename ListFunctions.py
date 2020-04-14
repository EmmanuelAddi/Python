
units = ["Physics", "Chemistry", "English", "Calculus", "Probability", "Statistics"]
campus = ["MKU", "JKUAT", "Moi"]
units.extend(campus)
units.append("OOP")
units.remove("English")
units.sort()

print(units)

units2 = units.copy()
print(units2)