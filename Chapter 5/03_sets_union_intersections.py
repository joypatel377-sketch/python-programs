s1 = {1,2,3,44,55}
s2 = {2,3,66,77,88}
a = s1.union(s2)
s3 = s1.intersection(s2)
print(sorted(a))

c = a.union(s3)
print(sorted(c))


a