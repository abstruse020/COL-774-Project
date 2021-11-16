#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class TermVocab:
    def __init__(self):
        self.term2index = {}
        self.index2term = {}
        self.term2count = {}
        self.vocab_length = 0
    
    def add_term(self, term):
        if term not in self.term2count:
            self.term2index[term] = self.vocab_length
            self.term2count[term] = 1
            self.index2term[self.vocab_length] = term
            self.vocab_length += 1
        else:
            self.term2count[term] += 1
        return
    
    def to_term(self, index):
        return self.index2term[index]
    
    def to_index(self, term):
        return self.term2index[term]
    
    def get_count(self, term):
        return self.term2count[term]

