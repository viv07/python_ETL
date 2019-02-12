import pandas as pd
df1=pd.read_csv('D:\D Drive\python\python programming\pandas programming\emp.dat')
df2=pd.read_csv('D:\D Drive\python\python programming\pandas programming\dept.dat')

print(df1)
print(df2)

#innerjoin
result_in=pd.merge(df1,df2[['deptno','dname','loc']],on='deptno',indicator=True)
print(result_in)

#left outer join
result_left=pd.merge(df1,df2[['deptno','dname','loc']],on='deptno',how='left',indicator=True)
print(result_left)

#right outer join
result_right=pd.merge(df1,df2[['deptno','dname','loc']],on='deptno',how='right',indicator=True)
print(result_right)

#full outer join
result_full=pd.merge(df1,df2[['deptno','dname','loc']],on='deptno',how='outer',indicator=True)
print(result_full)

