import pickle
dct={'а':1,'б':2,'в':3,'Джим':20}
infile=open('mydata.dat','rb')
a=pickle.load(infile)
print(a)
infile.close()
