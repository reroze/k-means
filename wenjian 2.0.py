import numpy as np
np.set_printoptions(threshold=3000000)
from scipy.cluster.vq import vq,kmeans,whiten
file =open("F:\\bigdata\\ceshishuchu4.txt","r")
file2 =open("F:\\bigdata\\result.txt","w")
list = file.readlines()
lists =[]
a=[]
for fields in list:
    fields=fields.strip();
    fields=fields.strip("[]");
    fields=fields.split(",");
    lists.append(fields);
    #print (lists)
for fields in list:
    fields=fields.strip();
    fields=fields.strip("[]");
    fields=fields.split(",");
    #print (fields)
    a_float=[float(i) for i in fields]
for s in a_float:    
    print (s)
print (a_float)
for w in lists:
        w=[float(i) for i in w]
        a=a+[w]
        #print(w)
#print (a)
data=np.array(a)
whiten=whiten(data)
centroids,_=kmeans(whiten,10)
result,_=vq(whiten,centroids)
#print(result)
file2.write(str(result));
file2.close()
