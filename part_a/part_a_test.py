import itertools

set_1 = {1, 2, 3}
set_2 = {3, 4, 5}
set_3 = {4, 5, 6}

full_set = set()
full_set.update(set_1)
full_set.update(set_3)
full_set.update(set_2)

sub_sets = set(itertools.combinations(full_set, 2))
print(sub_sets)