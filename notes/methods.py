######string methods

### len()
language = "python"
print(len(language))

### [] notation
print(language[0])
print(language[-5])

print(language[0:2])
print(language[0:])
print(language[:2])
print(language[:])
#these makes a new list ^

### combining strings / concatenation
city = "Las Vegas"
state = "NV"
country = "USA"
address = city + " " + state + ", " + country
print(address)

### .method
print(city.upper())
print(address.upper())
print(address.lower())
print(address.replace("Las Vegas", "summerlin"))
