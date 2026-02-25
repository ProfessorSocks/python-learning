# my_input = input("What is your age?")

# print(type(my_input))

# age = int(my_input)
# print(type(age))

print(bool(1))
print(bool("cat"))
print(bool("False"))
#Q string of false = true how do I convert it?
def str_to_bool(text):
    return text.strip().lower() == "true"

# print(bool(str_to_bool("False")))


#falsey value
print(bool(""))
print(bool(None))
print(bool(0))
print(bool(False))
print(bool(str_to_bool("False")))