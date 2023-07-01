lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [element for sublist in lists for element in sublist]
print(flattened_list)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
data = [{"name": "John", "age": 25, "city": "New York"},        {"name": "Jane", "age": 32, "city": "London"},        {"name": "Jim", "age": 41, "city": "Paris"}]

names = [person["name"] for person in data]
print(names)
# Output: ['John', 'Jane', 'Jim']

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
cartesian_product = [(x, y) for x in list1 for y in list2]
print(cartesian_product)
# Output: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]