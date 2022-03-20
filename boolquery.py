from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd
import numpy as np

def intersect(p1,p2):
    res=[]
    i,j=0,0
    while(i<len(p1) and j<len(p2)):
        if(p1[i]==p2[j]):
            res.append(p1[i])
            i+=1
            j+=1
        elif p1[i]<p2[i]:
            i+=1
        else:
            j+=1
    return res

def postunion(p1,p2):
    res=[]
    res=list(set().union(p1,p2))
    return res

# def multiintersect(t,post_list):
#     terms=sorted(t,key=lambda x: post_list[x] for x in t)
#     res=post_list[terms[1]]
#     terms=terms[1:]
#     i,j=0,0
#     while(i<len(terms) and j<len(res)):
#         res=intersect(post_list[res],post_list[terms[0]])
#         terms=terms[1:]
#     return res


df=pd.read_csv('train.csv')
stop_words=set(stopwords.words('english'))
df['texttoken']=df['text'].apply(word_tokenize)
df['texttoken']=df['texttoken'].apply(lambda words:[word.lower() for word in words if word.isalpha()])
df['stop_remd']=df['texttoken'].apply(lambda x:[item for item in x if item not in stop_words])
post_list={}
for postext,text in enumerate(df['stop_remd'].head(10)):
    for pos,term in enumerate(text):
        if term not in post_list.keys():
            post_list[term]=[]
        post_list[term].append(postext)

for i in post_list:
    print(i,"\t",post_list[i])

inp=input("Enter boolean AND query:").split()
print(intersect(post_list[inp[0]],post_list[inp[2]]))
print(postunion(post_list[inp[0]],post_list[inp[2]]))
