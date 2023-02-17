some_list = ['a', 'b', 'c', 'd', 'e', 'd', 'b']

no_dupes = [x for n, x in enumerate(some_list) if x not in some_list[:n]]
print(no_dupes)
