# Python3 code to demonstrate working of
# Sort Matrix by index-value equality count
# Using sorted() + lambda + len() + enumerate()

# initializing list
test_list = [[3, 1, 2, 5], [0, 1, 2, 3],
			[6, 5, 4, 3], [0, 5, 4, 2]]

# printing original list
print("The original list is : " + str(test_list))

# transposing matrix
test_list = zip(*test_list)

# sorting using sorted()
# utility injection using lambda
# element and index compared, if equal added in
# list, length computed using len()
res = sorted(test_list, key=lambda row: len(
	[ele for idx, ele in enumerate(row) if ele == idx]))

# performing transpose again to get result.
res = zip(*res)

# converting list of tuples to list of lists
res = [list(sub) for sub in res]

# printing result
print("Sorted List : " + str(res))
