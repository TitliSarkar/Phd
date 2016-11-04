##import os
##for file in os.listdir("F:\\Studies\\Ph.D\\Ph.D Work\\sampleDataSet\\sampleDataDebanjali\\alpha\\3"):
##    if file.endswith(".keys"):
##        print(file)
import sys
sys.path.append('c:\\program files\\anaconda3\\lib\\site-packages')

import glob, os
import os, os.path
import csv
import operator
import numpy as np
import pandas as pd

#Getting all Protein files and saving them in a list'Protein[]'
Protein =[]
os.chdir("F:\\Studies\\Ph.D\\Ph.D Work\\ProteinDataSet")
for file in glob.glob("*.keys"):
        Protein.append(file)
#print(Protein)
#print("#Proteins = ",len(Protein))  

#Sorting all Protein files
'''for p in Protein:
        with open(p, "r") as p_file:
                filename = "F:\\Studies\\Ph.D\\Ph.D Work\\ProteinDataSet\\"+p_file.name
                #print(" File -->",filename)
                f = open(filename, "r")
                lines = f.readlines()
                #print (lines)
                lines.sort(key=lambda a_line: a_line.split()[0])
                #print (lines)
                f2 = open(filename, "w")
                f2.write(''.join(lines)) # Write a sequence of strings to a file
                f2.close()
                f.close()
print("File sorting Done!")
'''
'''
#Getting all unique keys in a  sorted list 'Keys[]'
Keys = []
#f2 = open("F:\\Studies\\Ph.D\\Ph.D Work\\ProteinDataSet\\keys.txt", "w")
for pt in Protein:
        with open(pt, "r") as p_file:
                filename = "F:\\Studies\\Ph.D\\Ph.D Work\\ProteinDataSet\\"+p_file.name
                print(filename);
                f = open(filename, "r")
                for line in f:
                        item = line.split(None, 1)[0]
                        #print(item)
                        #if item not in Keys:
                        Keys.append(item) #add only 1st number of each line of the files as keys
                f.close()
                #f2.write(item) # Write a sequence of strings to a file
              #f2.close()
Keys = np.unique(Keys)
Keys = np.sort(Keys)
num_unq_keys = Keys.shape[0]
np.save("F:\\Studies\\Ph.D\\Ph.D Work\\ProteinDataSet\\keys", Keys);
print("#Unique Keys=",num_unq_keys); 
print(Keys)
print(" Getting unique keys Done!")
'''
print(Protein[:5])
Keys = np.load("F:\\Studies\\Ph.D\\Ph.D Work\\ProteinDataSet\\keys.npy")

df = pd.DataFrame(Keys, index=np.arange(Keys.shape[0]), columns=['Key'])
#print(df)

result = np.zeros((len(Protein), Keys.shape[0]))

i = 0
for pt in Protein:
        with open(pt, "r") as p_file:
                filename = "F:\\Studies\\Ph.D\\Ph.D Work\\ProteinDataSet\\"+p_file.name
                #print(filename)
                f = open(filename, "r")
                d = {}
                for line in f:
                        item = line.split('\t')
                        #print(item)
                        #if item not in Keys:
                        d[item[0]] = item[1]
                indices = df[df['Key'].isin(d.keys())].index
                temp = np.zeros((Keys.shape[0],))
                temp[indices] = list(d.values())
                result[i] = temp
                i += 1
print(result)
print(result.shape)
np.save('F:\\Studies\\Ph.D\\Ph.D Work\\ProteinDataSet\\result.npy', result)
df = pd.DataFrame(result, columns=Keys)
df.to_csv('F:\\Studies\\Ph.D\\Ph.D Work\\ProteinDataSet\\result.csv')
#Forming Protein-key matrix

