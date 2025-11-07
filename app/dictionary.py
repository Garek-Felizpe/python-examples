person = {"name": "Felipe", "age": 31, "city": "Cotia", "weight": 110, "height": 1.83, "etniethnicity": "white", "gender": "male","country": "Brazil"}
print(person.get("name"))
print(person.get("age"))
print(person.get("city"))
print(person.get("weight"))
print(person.get("height"))
print(person.get("etniethnicity"))
print(person.get("gender"))
print(person.get("country"))

print(person.keys()) #shows only keys
print(person.values()) #shows only values
print(person.items()) #shows both keys and values

person.update({"profession": "student"}) #adds a new key-value pair
print(person)