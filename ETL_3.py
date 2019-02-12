#import cx_Oracle
import pandas as pd

df=pd.read_csv('D:\D Drive\python\python programming\python_db_conn\emp_det.txt')
print(df)
df_list=df.values.tolist()

print (df_list)


conn=cx_Oracle.connect('scott/scott@orcl2')
cur=conn.cursor()

sql='insert into emp_t1 values(:1,:2,:3,:4)'
for rec in df_list:
    cur.execute(sql,rec)

conn.commit()
conn.close()
