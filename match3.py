# import hmni
import pandas as pd
# import hashlib

data = pd.read_csv('~/Desktop/patents/raw_names_year_v3.csv', sep='|', dtype={'raw_fname': str, 'raw_lname': str, 'clean_name': str}, na_values={'raw_fname': 'none', 'raw_lname': 'none', 'clean_name': 'none'}, keep_default_na=False)
salaries = pd.read_csv('~/Downloads/examiner_salary_data_v3.csv', sep='|', dtype={'url_name': str}, na_values={'url_name': 'none'}, keep_default_na=False)
fNamelist = []
lNamelist = []
for ind in salaries.index:
    name = salaries['url_name'][ind]
    for ind2 in data.index:
        if data['clean_name'][ind2] == name:
            fNamelist.append(data['raw_fname'][ind2])
            lNamelist.append(data['raw_lname'][ind2])
            break
    if ind == len(fNamelist):
        fNamelist.append(name)
    if ind == len(lNamelist):
        lNamelist.append(name)
    print(lNamelist[ind])
salaries['fname'] = fNamelist
salaries['lname'] = lNamelist
salaries.to_csv('~/Desktop/patents/examiner_salary_data_v4.csv', sep='|', index=False)
