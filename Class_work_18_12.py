# create list
nums = [1, 2, 3, 4, 5]
category = ['drama', 'comedy', 'fantasy']
courses = list(('math', 'db', 'python'))
words = 'one two three'.split()
print(words)
print(nums)

list1 = [i * i for i in range(10)]
print(list1)

list2 = [i + "*" for i in 'example']
print(list2)

list3 = [i * i for i in range(1, 11) if i % 2 == 0]
print(list3)

customers = ['Bob', 'Anna', 'Jon', 'Bill']
list4 = [i for i in customers if i != 'Bob' and i != 'Jon']
print(list4)

for elem in customers:
    print(elem, end=' | ')

print("\n-------------")
print('first customer - ', customers[0])
print('last customer - ', customers[len(customers) - 1])

print(customers[1:3])
print(customers[-4:-2])
print(customers[:8])
print(customers[2:])
print(customers[::-1])

prices = [233, 544, 543, 66, 123]
print("sum price = ", sum(prices))
print('min = ', min(prices))
print('max = ', max(prices))
print(sorted(prices))
print(sorted(customers))

print([1, 2] + [3, 4])
print([1, 2] * 2)

category2 = ['drama']
print(category2)
category2.append('fantasy')
print("after add ", category2)

category2.insert(0, 'triller')
print("after insert ", category2)

category2.extend(['cat1', 'cat2'])
print("after extend - ", category2)

# category2.pop()
# category2.pop(0)
print('after delete - ', category2)

# if 'cat1' in category2:
# category2.remove('cat1')
print("after remove - ", category2)

# category2.clear()

# change elem
category2[0] = 'new elem'
print("after change - ", category2)

print('find index = ', category2.index('new elem'))
print('count elem = ', category2.count('fantasy'))
category2.sort(reverse=True)
print("afte sort = ", category2)
category2.reverse()
print(category2)

list1 = [1, 2, 3]
list2 = list1.copy()
list3 = list(list2)
list4 = list1[:]

list2[0] = 10
print(list2)
print(list1)

matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix)
for row in matrix:
    print("|", end="")
    for elem in row:
        print(elem, end="|")
    print('')

print(matrix[1][2])