cities = {'New York', 'Los Angeles', 'Chicago2'}
cities2 = {'Chicago', 'Houston', 'Seattle'}
print(cities.issuperset(cities2))
cities3 = {'New York', 'Los Angeles', 'Chicago2'}
print(cities.issuperset(cities3))  # True
# issuperset () method returns True if all elements of the set are present in the set, otherwise it returns Fals
# if the set is a subset of another set, then it is not a superset of that set