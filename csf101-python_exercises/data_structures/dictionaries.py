name = "Sonam Wangmo"
age = 19
height = 1.52
is_student = True
person_info = {
    "name": name,
    "age": age,
    "height": height,
    "is_studeent": is_student
}
print(person_info)
try:
    print(person_info["weight"])
except KeyError as e:
    print(f"Error: {e}")
    