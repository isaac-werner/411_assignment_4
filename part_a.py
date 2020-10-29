import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
import itertools


def apriori_frequent_item_sets(data_frame, min_support, max_len):
    all_ms = set()
    for i in range(1, 5):
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
        for sub_set in sub_sets:
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
        item_sets.append(item_set)
    return item_sets


# df = pd.read_csv('transactionlarge.csv', header=None) # real data set
df = pd.read_csv('transactionsmall.csv', header=None)  # test data set

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
print(data_frame)
result = apriori_frequent_item_sets(data_frame, 2, 3)
print(result)

