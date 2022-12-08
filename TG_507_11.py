import pickle
dct={'а':1,'б':2,'в':3,'Джим':20}
outfile=open('mydata.dat','wb')
pickle.dump(dct,outfile)
outfile.close()
