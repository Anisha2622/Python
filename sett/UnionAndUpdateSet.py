s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2)) # union of two sets
s1.update(s2) # update s1 with elements from s2
print(s1,s2)

cities = {'New York', 'Los Angeles', 'Chicago'}
cities2 = {'Chicago', 'Houston', 'Seattle'}
cities3 = cities.union(cities2)
print(cities3)