"""Day 8: 30 Days of python programming"""

# Create an empty dictionary called dog
dog = {}
# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Fluffy"
dog['color'] = 'red'
dog['legs'] = 4
dog['age'] = 3
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills,
# country, city and address as keys for the dictionary
student = {
    "first_name": "Manolo",
    "last_name": "Lopez",
    "gender": "male",
    "age": 16,
    "marital_status": "single",
    "skills": ["social", "Python"],
    "country": "spain",
    "city": "haro",
    "address": "calle falsa 123"
}
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
print(student["skills"], type(student["skills"]))
# Modify the skills values by adding one or two skills
student["skills"].append("write")
print(student)
# Get the dictionary keys as a list
print(student.keys())
# Get the dictionary values as a list
print(student.values())
# Change the dictionary to a list of tuples using items() method
print(student.items())
# Delete one of the items in the dictionary
print(student)
del student["city"]
print(student)
# Delete one of the dictionaries
del student
