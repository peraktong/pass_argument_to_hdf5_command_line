import os,sys,h5py
import numpy as np
import argparse
inputs = sys.argv
parser = argparse.ArgumentParser()
if len(inputs)==1:
    print("Data name_of_dataset(1D only!) save_name")



data = map(float, inputs[1].strip('[]').split(','))
name_of_dataset = str(inputs[2])
save_name = str(inputs[3])

data = list(data)
data = np.array(data)

print(data.shape)
print(name_of_dataset)
print(save_name)


hf = h5py.File(save_name,"w")

hf.create_dataset(name_of_dataset,data=data,dtype="f")

hf.close()

# check the hdf5 file
print("Check hdf5 file")

hf = h5py.File(save_name,"r")

data = np.array(hf[name_of_dataset])
print(data,name_of_dataset,save_name)

hf.close()

# remove the same
os.system("rm %s"%save_name)
