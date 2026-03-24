print("-" * 50)
print("------------welcome to weight converter-----------")
print("-" * 50)

weight = float(input("entre the weight: "))
unit = input("entre the unit(lbs/kg): ")
if unit == "kg":
    weight = weight * 2.205
    unit = "lbs"
    print(f"your weight is: {round(weight ,1)} {unit}")
elif unit == "lbs":
    weight = weight / 2.205
    unit = "kg"
    print(f"your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not a valid unit")

