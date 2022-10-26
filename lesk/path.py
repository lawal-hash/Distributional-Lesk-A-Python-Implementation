# -*- coding: utf-8 -*-
"""path.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RVoJG3JYCr0f8Yk1rmQDel_5QX0ICRHy
"""

# Url  to get the data from
url = 'http://web.eecs.umich.edu/~mihalcea/downloads/semcor/semcor1.7.1.tar.gz'
url_2 = 'http://web.eecs.umich.edu/~mihalcea/downloads/senseval.semcor/senseval2.semcor.tar.gz'
url_3 = 'http://web.eecs.umich.edu/~mihalcea/downloads/senseval.semcor/senseval3.semcor.tar.gz'
url_auto = 'https://www.cis.lmu.de/sascha/AutoExtend/embeddings.zip'

# Save downloaded data as 
semcor = 'semcor1.7.1.tar.gz'
senseval2 = 'senseval2.semcor.tar.gz'
senseval3 = 'senseval3.semcor.tar.gz'
AutoExtend = 'autoextend.zip'
word2vec = 'GoogleNews-vectors-negative300.bin.gz'

# file pattern
pattern_1 = r'br-'
pattern_2 = r'.semcor.lexsn.key'
pattern_3 = r''

# 
semcor_dir = r'~/semcor1.7.1'
senseval2_dir = r'senseval2.semcor/wordnet1.7.1'
senseval3_dir = r'~/senseval3.semcor/wordnet1.7.1'
mapping = '~/mapping.txt'
lexemes = '~/lexemes.txt'
word2vec_weight_dir = '/content/drive/MyDrive/GoogleNews-vectors-negative300.bin'

offset1_7_to_3 = '/content/drive/MyDrive/wn1.7.1_to_3.0.csv'
