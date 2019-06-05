import os,sys,h5py
import numpy as np
import argparse
inputs = sys.argv
import pandas
# file name+ dataset+:

parser = argparse.ArgumentParser()
if len(inputs)==1:
    print("python 0605_read_hdf5_from_terminal_v1.py filename dataset_name(can be multiple)")
    print("If no dataset_name, all header names from the hdf5 file will be shown")

elif len(inputs)==2:
    print("Data name_of_dataset(1D only!) save_name")
    save_name = str(inputs[1])
    hf = h5py.File(save_name, "r")

    print(list(hf.keys()))

    hf.close()
else:
    # data = map(float, inputs[1].strip('[]').split(','))
    # if no dataset name, print hdf5 key

    save_name = str(inputs[1])
    name_of_dataset = str(inputs[2])
    N_length = len(inputs)-2
    name_of_dataset_array = []
    for i in range(0,N_length):
        name_of_dataset_array.append(str(inputs[2+i]))
    name_of_dataset_array = np.array(name_of_dataset_array)

    hf = h5py.File(save_name, "r")
    df = pandas.DataFrame()


    for i in range(0, N_length):
        data = np.array(hf[name_of_dataset_array[i]])
        df[name_of_dataset_array[i]]=data

    hf.close()


    # output:
    #print("name_of_dataset \n %s" % name_of_dataset)
    #print("Shape of data \n ")
    #print(data.shape)
    #print(data)

    print(df)







#print(data.shape)
#print(name_of_dataset)
#print(save_name)



