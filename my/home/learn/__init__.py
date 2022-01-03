from my.home.learn.arrays.ArrayActions import ArrayActions
from my.home.learn.arrays.TestArray import Test


def create_copy():
    temp = Test.array_with_numbers[:]
    return temp


print("array:")
print(Test.array)
array = create_copy()
print("array after copy:")
print(array)
array += create_copy()
print("array after copy:")
print(array)
print("Loop w/ array copy:")

for i in range(Test.array_counter):
    array.append(Test.array_with_numbers)
print(array)

print("filter array:")
array = ArrayActions.filter_array(array)
print(array)

