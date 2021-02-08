import hmni
import random
import pickle
import pandas as pd
import hashlib

salaries = pd.read_csv('~/Desktop/patents/examiner_salary_data_v4.csv', sep='|', dtype={'url_name': str, 'fname': str, 'lname': str}, na_values={'url_name': 'none'}, keep_default_na=False)
data = pd.read_csv('~/Desktop/patents/raw_names_year_v3.csv', sep='|', dtype={'raw_fname': str, 'raw_lname': str, 'clean_name': str}, na_values={'raw_fname': 'none', 'raw_lname': 'none', 'clean_name': 'none'}, keep_default_na=False)
matchdict = {}
print('aggregating')
dataNamelist = []
for ind in data.index:
    dataNamelist.append((data['clean_name'][ind], data['raw_fname'][ind] + ' ' + data['raw_lname'][ind]))
dataNamelist = list(set(dataNamelist))
salNamelist = []
for sind in salaries.index:
    salNamelist.append((salaries['url_name'][sind], salaries['fname'][sind] + ' ' + salaries['lname'][sind]))
salNamelist = list(set(salNamelist))
salnum = len(salNamelist)

print('preparing matcher')
matcher = hmni.Matcher(model='latin')
counter = 0
print('matching')
for salName in salNamelist:
    matchlist = []
    for dataName in dataNamelist:
        if matcher.similarity(salName[1], dataName[1]) > 0.55:
            matchlist.append(dataName[0])
    if len(matchlist) > 3:
        matchlist = [salName[0]]
    matchdict[salName[0]] = matchlist
    counter += 1
    if random.randint(1, 10) > 9:
        print(salName)
        print(matchlist)
    print(str(counter) + '/' + str(salnum))

f = open('matchdict.pkl', 'wb')
pickle.dump(matchdict, f, protocol=pickle.HIGHEST_PROTOCOL)
f.close()
