numbers1 = set([1, 2, 3, 4, 5,6,7,8,9,10])
numbers2 = set([5, 6, 7, 8, 9, 10,11,12,13,14,15])

union = numbers1 | numbers2
print("Union:", union)

intersection = numbers1 & numbers2
print("Intersection:", intersection)

difference = numbers1 - numbers2
print("Difference (numbers1 - numbers2):", difference)

symmetric_difference = numbers1 ^ numbers2
print("Symmetric Difference:", symmetric_difference)