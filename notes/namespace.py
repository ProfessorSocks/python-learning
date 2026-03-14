# num = 23

# print(id(num))
# print(id(23))
#q - why does namespace matter
#q - what is id useful for?

# num += 1
# print(id(num))

# num2 = 23
# print(id(num2))

#q - b = 2 now but what happens if I point 2 names to the same object?

def outer():
  outer_num = 100
  print(id(outer_num))

  def inner():
    inner_num = 200
    print(inner_num) #functions are asleep unless called

    # outer_num = 400
    print(outer_num)
 
    print(id(outer_num))

  inner()

global_num = 300

outer()

