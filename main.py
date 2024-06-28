def is_Adult(age):
    if age >= 16:
        return True
    else:
        return False
result = is_Adult(34)

def convertGender(gender = "unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else:
        return gender

print(result)
print(convertGender("M"))
print(convertGender("F"))
print(convertGender("m"))