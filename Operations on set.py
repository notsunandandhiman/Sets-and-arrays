

my_set = {1,2,3}
print(my_set)

my_set = {1.0, "Hello", (1,2,3)}
print(my_set)

my_set = {1,2,3,4,3,2}
print(my_set)

my_set =({1,2,3,2})
print(my_set,"\n")

num_set = set({0,1,3,4,5})
print("Orignal set:")
print(num_set)
num_set.pop()
print("Afer removing the first element from the said set:")
print(num_set,"\n")

num_set.add(8)
print("After adding element from the said set:")
print(num_set,"\n")
