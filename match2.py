# import hmni
import pandas as pd
# import hashlib

data = pd.read_csv('~/Downloads/raw_names_year_v2.csv', sep='|', dtype={'raw_fname': str, 'raw_lname': str}, na_values={'raw_fname': 'none', 'raw_lname': 'none'}, keep_default_na=False)
cleanNamelist = data[['raw_lname', 'raw_fname']].agg(' '.join, axis=1)
for ind in range(len(cleanNamelist)):
    name = cleanNamelist[ind]
    cleanNamelist[ind] = name.replace(' ', '-').replace('.', '').lower()
    print(cleanNamelist[ind])
data['clean_name'] = cleanNamelist
data.to_csv('~/Desktop/patents/raw_names_year_v3.csv', sep='|', index=False)
