import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
import itertools
import time


def apriori_frequent_item_sets(data_frame, min_support, max_len):
    item_set_dict = {}
    all_ms = set()
    for i in range(1, 100):
        all_ms.add(f'M{i}')

    item_sets = []
    item_set_1 = set()
    for m in all_ms:
        count = 0
        for index, row in data_frame.iterrows():
            if row[m]:
                count += 1
        if count >= min_support:
            item_set_1.add(m)
            item_set_dict[f'(\'{m}\')'] = count

    item_sets.append(item_set_1)
    for i in range(1, max_len):
        all_entries = set()
        if i == 1:
            for m in item_sets[0]:
                all_entries.add(m)
        else:
            for ms in item_sets[i - 1]:
                all_entries.update(ms)

        sub_sets = set(itertools.combinations(all_entries, i + 1))
        item_set = []
        h = 1
        for sub_set in sub_sets:
            h += 1
            count = 0
            in_row = False
            for index, row in data_frame.iterrows():
                for m in sub_set:
                    if row[m]:
                        in_row = True
                    else:
                        in_row = False
                        break
                if in_row:
                    count += 1
            if count >= min_support:
                item_set.append(sub_set)
                item_set_dict[str(sub_set)] = count
        item_sets.append(item_set)

    for key in item_set_dict.keys():
        print(f'{key} {item_set_dict[key]}')

start_time = time.time()
df = pd.read_csv('part_a/transactionsmall.csv', header=None)

data_set = []
for index, row in df.iterrows():
    data_row = []
    for value in row.values:
        if str(value) != 'nan':
            data_row.append(value)
    data_set.append(data_row)

te = TransactionEncoder()
te_array = te.fit(data_set).transform(data_set)

data_frame = pd.DataFrame(te_array, columns=te.columns_)
apriori_frequent_item_sets(data_frame, 3, 3)
print(f'Runtime: {time.time() - start_time} seconds')
