import pandas as pd
import json

openfile=open('/home/ubuntu/scripts/python/test3.json')
jsondata=json.load(openfile)
df=pd.DataFrame(jsondata)

openfile.close()
print(df)
df.to_csv('test_output.csv',index=False, encoding='utf-8')
