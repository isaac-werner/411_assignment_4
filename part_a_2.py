import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import itertools
import time


start_time = time.time()
df = pd.read_csv('transactionlarge.csv', header=None)  # real data set
# df = pd.read_csv('transactionsmall.csv', header=None)  # test data set

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

frequent_itemsets = apriori(data_frame, min_support=0.01, use_colnames=True, max_len=3)
print(f'Runtime: {time.time() - start_time} seconds')
print(frequent_itemsets)

