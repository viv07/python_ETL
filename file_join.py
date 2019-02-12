import csv

data1=open(r'D:\D Drive\python\python programming\data_files\emp.txt')
data2=open(r'D:\D Drive\python\python programming\data_files\dept.txt')
out_file=r'D:\D Drive\python\python programming\data_files\master_tgt.txt'

d1=data1.readline()
d1=data1.readlines()
d2=data2.readline()
d2=data2.readlines()

#will print header in file
lt=[['empno,name,sal,deptno,dname,loc']]

ct=0

for line1 in d1:
    c1=line1.split(',')
    
    for line2 in d2:
        c2=line2.split(',')
        
        if c1[3].strip()==c2[0].strip():
            
            row=[]
            
            row.append(c1[0])
            row.append(c1[1])
            row.append(c1[2])
            row.append(c2[0])
            row.append(c2[1])
            row.append(c2[2].strip('\n'))
            lt.append(row)
            
            print(lt)
            

#write to outfile

with open(out_file,'w') as f:
    for line in lt:
        for item in line:
            f.write(item +',')
            
        f.write('\n')
		
with open('C:\\Users\\Vivek\\Desktop\\viv.txt','w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(lt)
csvfile.close()		
        
f.close()    
          
data1.close()
data2.close()
            
        
    
