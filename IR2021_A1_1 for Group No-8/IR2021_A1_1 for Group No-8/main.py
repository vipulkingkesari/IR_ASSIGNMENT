import os
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import re
import numpy as np
import ir5
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
def clean(aman):
  aman11 =aman.lower()
  aman1 = aman11.rstrip()
  words = aman1.split()
  table =str.maketrans("","",string.punctuation)
  striped = [w.translate(table) for w in words]
  striped1 = []
  striped2 = []
  stop = set(stopwords.words('english'))
  for w in striped:
    if w not in stop:
      striped1.append(w)
  for w in striped1:
    if not w.isdigit():
      striped2.append(w)
  lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in striped2]
  return lemmatized_word

def Unique(Words) :
  unique = [] 
  for i in Words:
    if not i in unique:
      unique.append(i)
  return unique
def apostrope(data):
  return np.char.replace(data,",","")
folders = [x[0] for x in os.walk("./stories/")]
print(folders)
"""
dataset = []
c = False
for i in folders:
  file = open(i+"/index.html", 'r')
  text = file.read().strip()
  file_name = re.findall('><A HREF="(.*)">', text)
  if c == False:
    file_name = file_name[2:]
    c = True
  for j in range(len(file_name)):
    dataset.append((str(i) +"/"+ str(file_name[j])))
    """
List=[]
i=0
for path, dirs,files in os.walk("./stories"):
  for f in files:
    filename = os.path.join(path,f)
    with open(filename,errors="ignore") as input_tokens1:
        processed_text=[]
        wordnet_lemmatizer = WordNetLemmatizer()
        aman2 = input_tokens1.read()
        aman3 = clean(aman2)
        aman5 = Unique(aman3)
        doc={
          'id':str(i),
          'text': ' '.join(aman5)
        }
        i+=1
        List.append(doc)
def preprocess(data):
  f = Unique(clean(data))
  return f
def operations(s,lists):
  a=[]
  total=0
  comparison=0
  while len(s)>0:
    a.append(s.pop(0))
    if len(a)==3 and a[0]!="not":
      result1 = lists.lookup_q(a[0])
      result2 = lists.lookup_q(a[2])
      rnot = lists.lookup_q(a[0]+' '+a[2])
      a.append(a[0]+' '+a[2])
      if(a[1]=="or"):
        total +=result1+result2-rnot
      elif(a[1]=="and"):
        total +=rnot
      elif(a[1]=="or not"):
        total+=result1-result2-rnot
      elif(a[1=="and not"]):
        total+=rnot
      comparison+=result1+result2
      a.pop(0)
      a.pop(0)
      a.pop(0)
    if(len(a)==2 and a[0]=="not"):
      result = lists.lookup_q(a[1])
      total -=result
      comparison+=result
      a.pop(0)
      a.pop(0)
    if(total<0): total =0
  return (total,comparison)
    
def operator(cmd,inp):
  res=[]
  while len(cmd)>0 and len(inp)>0:
    if(cmd[0]=="not"):
      res.append(cmd.pop(0))
      res.append(inp.pop(0))
    elif(len(cmd)>1):
      res.append(inp[0])
      inp.pop(0)
      if(cmd[1]=="not"):
        op = cmd[0]+' '+cmd[1]
        res.append(op)
        cmd.pop(0)
        cmd.pop(0)
      else:
        res.append(cmd.pop(0))
    elif(len(cmd)==1 and len(inp)>1):
      res.append(inp.pop(0))
      res.append(cmd.pop(0))
      res.append(inp.pop(0))     
  return res
        
    

def func():
  db = ir5.db()
  index = ir5.InvertedIndex(db)
  for i in List:
    index.index_document(i)
  while(True):
    s = input("Enter Query:")
    v = [x.lower() for x in input("Input Seq:").split()]
    pres = preprocess(s)
    print(pres)
    print(operator(v,pres))
    a = operator(v,pres)
    b = operations(pres,index)
    print(a)
    print(b)

func()