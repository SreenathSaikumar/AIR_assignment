from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd
import numpy as np

df=pd.read_csv('train.csv')
stop_words=set(stopwords.words('english'))
df['texttoken']=df['text'].apply(word_tokenize)
df['texttoken']=df['texttoken'].apply(lambda words:[word.lower() for word in words if word.isalpha()])
df['stop_remd']=df['texttoken'].apply(lambda x:[item for item in x if item not in stop_words])

ps=PorterStemmer()
df['stemmed']=df['stop_remd'].apply(lambda x:[ps.stem(item) for item in x])
idx_dict={}
for postext,text in enumerate(df['stemmed'].head(20)):
    for pos,term in enumerate(text):
        if term not in idx_dict.keys():
            idx_dict[term]=[0,{}]
        idx_dict[term][0]+=1
        if postext not in idx_dict[term][1].keys():
            idx_dict[term][1][postext]=[]
        idx_dict[term][1][postext].append(pos)
print("Term [Frequency,Entry number:[Positions in that entry]]")
for i in idx_dict:
    print(i,idx_dict[i])

def search(t1,t2,idx_dict):
    res=[]
    if t1 not in idx_dict.keys() or t2 not in idx_dict.keys():
        print("Query does not exist")
    else:
        idx1=idx_dict[t1][1]
        idx2=idx_dict[t2][1]
        interset=set(idx1.keys()).intersection(idx2.keys())
        for i in interset:
            l1=idx1[i]
            l2=idx2[i]
            for j in l1:
                if j+1 or j-1 in l2:
                    if i not in res:
                        res.append(i)
    if len(res)==0:
        print('Query does not exist')
    return res


inp=input("Enter query separated by spaces:").split()
inp=[ps.stem(i) for i in inp]
res=search(inp[0],inp[1],idx_dict)
print(res)
if len(res)!=0:
    for i in res:
        print(i,"\t",df['text'].iloc[i])




