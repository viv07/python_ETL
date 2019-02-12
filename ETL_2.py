import cx_Oracle

conn=cx_Oracle.connect('vivek/vivek@orcl2')
cur=conn.cursor()
df=[]
file=open(r'D:\D Drive\python\python programming\python_db_conn\emp_det.txt')
data=file.readline()
data=file.readlines()

print(data)
for line in data:
    df.append(line.strip().split(','))
    print(df)

sql='insert into emp_t1 values(:1,:2,:3,:4)'
for rec in df:
    cur.execute(sql,rec)
conn.commit()
conn.close()
