#!/usr/bin/env python3
import re
class appear:
    def __init__(self,docID,frq):
        self.docID=docID
        self.frq = frq

    def __repr__(self):
        return str(self.__dict__)

class db:
    def __init__(self):
        self.db=dict()

    def __repr__(self):
        return str(self.__dict__)

    def get(self,id):
        return self.db.get(id,None)

    def add(self,document):
        return self.db.update({document['id']: document})
    def remove(self,document):
        return self.db.pop(document['id'],None)

class InvertedIndex:
    def __init__(self,db):
        self.index=dict()
        self.db=db

    def __repr__(self):
        return str(self.index)

    def index_document(self,document):
        cln_tx = re.sub(r'[^\w\s]','',document['text'])
        terms = cln_tx.split(' ')
        appear_dict = dict()
        for term in terms:
            term_freq = appear_dict[term].frq if term in appear_dict else 0
            appear_dict[term]=appear(document['id'],term_freq+1)
        update_dict = {key: [appearance] if key not in self.index else self.index[key] + [appearance] for (key,appearance) in appear_dict.items() }
        self.index.update(update_dict)

        self.db.add(document)

        return document
    def lookup_q(self,query):
        return {term: self.index[term] for term in query.split(' ') if term in self.index}

def highlight_term(id, term, text):
    replaced_text = text.replace(term, "\033[1;32;40m {term} \033[0;0m".format(term=term))
    return "--- document {id}: {replaced}".format(id=id, replaced=replaced_text)
""" Test Works 
def main():
    Db = db()
    index = InvertedIndex(Db)
    d1 = {
        'id':'1',
        'text': 'beer Belgium sharks'
        'preprocess':'<preprocessed text>'
    }
    d2={
        'id':'2',
        'text':'Belgium has great beer'
    }
    index.index_document(d1)
    index.index_document(d2)
    s = input()
    result = index.lookup_q(s)
    for i in result.keys():
        for a in result[i]:
            doc = Db.get(a.docID)
            print(highlight_term(a.docID,i,doc['text']))

main()
"""
