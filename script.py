import codecademylib
import pandas as pd
inventory = pd.read_csv('inventory.csv')
inventory.head(10)
staten_island = inventory.iloc[0:10]
product_request = staten_island.product_description
print(inventory.head(10))
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
print(seed_request)
inventory['in_stock'] = inventory.apply(lambda x: True if x.quantity > 0 else False, axis=1)
print(inventory.in_stock)
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
print(type(combine_lambda))
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
print(inventory.full_description)









