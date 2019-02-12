#copying multiple file data to master file

import os

lis=os.listdir('D:\D Drive\python\python programming\data_files\data_files')
print(lis)
tgt=os.listdir('D:\\D Drive\\python\\python programming\\data_files\\target_file')
file_dir='D:\D Drive\python\python programming\data_files\data_files'
out_file=r'D:\D Drive\python\python programming\data_files\target_file\master_tgt.txt'
ct=0

print('target file :',tgt)
try:
    if len(tgt)>0:
        os.remove('D:\\D Drive\\python\\python programming\\data_files\\target_file\\master_tgt.txt')
        open(tgt,'a').close() 
    else:
        open(tgt,'a').close() 
except:
    head=open('D:\\D Drive\\python\\python programming\\data_files\\target_file\\master_tgt.txt','a+')
    line='empno,ename,sal'
    print >>head,line
    head.close()
    for line1 in lis:
        f_dir=file_dir+'\\'+line1
        in_file=open(f_dir,'r+')
        w=open(out_file,'a+')
        d=in_file.readline()
        d=in_file.readlines()
        w.write("\n")
        for line2 in d:
            print(line2)
            w.write(line2)
            
        ct=ct+1    
    w.close()       





