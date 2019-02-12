#ora cojnnection with new db
import cx_Oracle
con = cx_Oracle.connect('scott/scott@orcl2')
cursor=con.cursor()
cursor.execute("""select empno,ename,sal from emp""")
for empno,ename,sal in cursor:
    print("values:",empno,'#',ename,'#',sal)    
#print con.version
con.close()
