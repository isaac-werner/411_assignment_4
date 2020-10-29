import pandas as pd
from mlxtend.preprocessing import TransactionEncoder


def apriori_frequent_item_sets(data_frame, min_support, max_len):
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

    for i in range(1, max_len):
        pass


df = pd.read_csv('transactionlarge.csv', header=None)
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

apriori_frequent_item_sets(data_frame, 20, 20)

