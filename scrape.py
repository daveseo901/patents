import pandas as pd
import requests

examiners = pd.read_csv('~/Downloads/raw_names_year.csv', sep='|', dtype={'raw_fname': str, 'raw_lname': str}, na_values={'raw_fname': 'none', 'raw_lname': 'none'}, keep_default_na=False)
data = pd.DataFrame()

rawfnames = examiners['raw_fname']
rawlnames = examiners['raw_lname']
names = examiners[['raw_lname', 'raw_fname']].agg(' '.join, axis=1)
names = list(set(names))
for name in names:
    print(name)
    name = name.replace(' ', '-').replace('.', '').lower()

    url = "https://www.federalpay.org/employees/patent-and-trademark-office/" + name

    r = requests.get(url)
    if r.ok:
        df_list = pd.read_html(r.text)
        df = df_list[0]
        df['url_name'] = name
        data = data.append(df)
data.to_csv('~/Desktop/patents/examiner_salary_data_v2')
