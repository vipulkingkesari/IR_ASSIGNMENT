import os
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import re
import numpy as np
#import pandas as pd
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
# def apostrope(data):
#   return np.char.replace(data,"'","")
#entry = os.listdir('C:/Users/Hp/Pictures/stories/')
folders = [x[0] for x in os.walk("E:\IR\Assignemnt1/stories/")]
print(folders)

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
am =len(dataset)

List=[]
i=0
for path, dirs,files in os.walk("E:\IR\Assignemnt1/stories/"):

  for f in files:
    filename = os.path.join(path,f)
    with open(filename,errors="ignore") as input_tokens1:
        #stop = set(stopwords.words('english'))
        #print(op)
        processed_text=[]
        wordnet_lemmatizer = WordNetLemmatizer()
        aman2 = input_tokens1.read()
        aman3 = clean(aman2)
        # aman4 = apostrope(aman3)
        
        #aman4 = nltk.word_tokenize(str(aman3))
        aman5 = Unique(aman3)
        doc={
          'id':str(i),
          'text': ' '.join(aman5)
        }
        i+=1
        List.append(doc)
        print(doc)
        #print(aman5)
        
        
