a = (1,45,342,3424,False, 45, "Rohan", "Shivam")
print(a) 

no = a.count(45) # kitni baar 45 he wo bateyga
print(no)

i = a.index(3424)
print(i)

print(len(a))

# Tuple operations and built-in functions

t1 = (1, 2, 3)
t2 = (4, 5)

# Concatenation
t3 = t1 + t2
print(t3)        # (1, 2, 3, 4, 5)

# Repetition
t4 = t1 * 3
print(t4)        # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Length
print(len(t1))   # 3

# Minimum element
print(min(t3))   # 1

# Maximum element
print(max(t3))   # 5

# Sum of elements
print(sum(t3))   # 15

# Membership test
print(2 in t1)   # True

# Slicing
print(t3[1:4])   # (2, 3, 4)

# Tuple unpacking
a, b, c = (10, 20, 30)
print(a, b, c)   # 10 20 30
