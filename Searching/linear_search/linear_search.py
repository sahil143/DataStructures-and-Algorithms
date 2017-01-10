import sys

# a is the list and b is the entity to be searched
def linear_search(a, b):
	for i in a:
		if i == b:
			return True

print("Enter the list:")
a = sys.stdin.readline().split()
b = input("Enter the number to be searched: ")
if linear_search(a, b) == True:
	print("found match")
else:
	print("Not found")
