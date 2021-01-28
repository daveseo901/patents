import hmni
from dask import dataframe as dd
import pandas as pd
import hashlib

data = pd.read_csv('~/Downloads/master_patents.csv', sep='|', encoding='ISO-8859-1', engine='python', dtype={'app_code': 'object', 'app_date': 'object', 'pub_date': 'object', 'art': 'object', 'class': 'object', 'n_claims': 'object', 'pub_kind': 'object', 'exam_prim': 'object', 'exam_asst': 'object'}, na_values={'exam_asst_fName': 'null', 'exam_asst_lName': 'null'}, keep_default_na=False)
primNamelist = []
primNamelist = (data[['exam_prim_fName', 'exam_prim_lName']].apply(lambda x: ' '.join(x), axis=1))
asstNamelist = []
asstNamelist = (data[['exam_asst_fName', 'exam_asst_lName']].apply(lambda x: ' '.join(x), axis=1))
primIDlist = []
asstIDlist = []
matcher = hmni.Matcher(model='latin')
print(matcher.similarity("B. Dobeck", "Benjamin Dobeck"))
primNamelist = matcher.dedupe(primNamelist, threshold=0.6, keep='frequent', replace=True)
asstNamelist = matcher.dedupe(asstNamelist, threshold=0.6, keep='frequent', replace=True)
for Name in primNamelist:
    primIDlist.append(int(hashlib.sha256(Name.encode('utf-8')).hexdigest(), 16) % 10**8)
for Name in asstNamelist:
    asstIDlist.append(int(hashlib.sha256(Name.encode('utf-8')).hexdigest(), 16) % 10**8)
data['exam_prim_clean'] = primNamelist
data['exam_prim_id'] = primIDlist
data['asst_prim_clean'] = asstNamelist
data['asst_prim_id'] = asstIDlist
data.to_csv('~/Downloads/sample_master_patents_v2.csv', encoding='ISO-8859-1', index=False)
