# -*- coding: utf-8 -*-
"""Dataloader.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RVoJG3JYCr0f8Yk1rmQDel_5QX0ICRHy
"""

import codecs
import os
import tarfile
from urllib.request import urlretrieve

import numpy as np
from lxml import html

np.random.seed(1234)
from enum import Enum
from pywsd import EN_STOPWORDS
import shutil
# from tqdm import tqdm
# from tqdm.notebook import tqdm_notebook
from lesk.path import *

embeddings = None


class ModelType(Enum):
    MFS = 'most_common_sense'
    PLAIN = 'plain_lesk'
    DIST = 'distributional_lesk'
    SENSE = 'vector'
    LEXMES = 'lexemes'
    GLOSS = 'gloss'
    BOTH = 'lexemes_gloss'


def to_ascii(s):
    # remove all non-ascii characters
    return codecs.encode(s, 'ascii', 'ignore')


def catch(value):
    try:
        vectors = value
    except  KeyError:
        vector = np.zeros((300,)).tolist()
    return vector


def data(url, savename, type='r:gz'):
    """Downloads and Extracts url"""
    local_filename, _ = urlretrieve(url, savename)
    if type is None:
        shutil.unpack_archive(savename)
    else:
        tar = tarfile.open(savename, type, encoding='utf-8')
        try:
            tar.extractall()
            tar.close()
        except PermissionError:
            tar.close()


def get_filenames(path, pattern=pattern_1):
    """Gets the directory of all the files in a folder"""
    filename_list = []
    files = os.walk(path)
    for dirpath, dirnames, filenames in files:
        for sample in filenames:
            print(sample)
            if pattern in sample:
                filename_list.append(os.path.join(dirpath, sample))
    # print(filename_list)
    return filename_list


def parser(filenames):
    """Open file as an html element"""
    parsed_list = []
    for file in filenames:
        parsed = html.fromstring(open(file).read())
        parsed_list.append(parsed)
    return parsed_list


class SenseEvalInstance:

    def __init__(self, my_id, lemma, context, context_vector, key, sense, pos, index):
        self.id = my_id  # id of the WSD instance
        self.lemma = lemma  # lemma of the word whose sense is to be resolved
        self.context = context  # lemma of all the words in the sentential context
        self.context_vector = context_vector
        self.key = key
        self.sense = sense
        self.pos = pos
        self.index = index  # index of lemma within the context

    def __str__(self):
        """
        For printing purposes.
        """
        return '%s\t%s\t%s\t%d' % (self.id, self.lemma, ' '.join(self.context), self.index)


def senseval_loader(parsed, remove_stop_words=False, word2vec=embeddings):
    """Loads seneval datasets"""
    instances = {}
    keys = {}
    for parse in parsed:
        sentences = parse.iterchildren()
        for sentence in sentences:

            if remove_stop_words:
                context = [word.text for word in sentence.iterchildren()]
                context = set(context).difference(EN_STOPWORDS)
                vector = np.array([catch(word2vec[word]) for word in context])
                context_vector = vector.mean(axis=0)
                # print(context)
            else:
                vector = np.array([catch(word2vec[word.text]) for word in sentence.iterchildren()])
                context_vector = vector.mean(axis=0)
                context = [word.text for word in sentence.iterchildren()]

            for i, word in enumerate(sentence.iterchildren()):
                if word.get('cmd') == 'done':
                    if word.text in context:
                        my_id = word.get('id')
                        lemma = to_ascii(word.get('lemma'))
                        key = word.get('lexsn')
                        pos = word.get('pos')
                        sense = word.get('wnsn')
                        instances[my_id] = SenseEvalInstance(my_id, lemma, context, context_vector, key, sense, pos, i)
                        keys[my_id] = sense
                    else:
                        continue
    return instances, keys


class SemCorInstance:
    def __init__(self, lemma, context, context_vector, key, sense, pos, index):
        # self.id = my_id         # id of the WSD instance
        self.lemma = lemma  # lemma of the word whose sense is to be resolved
        self.context = context  # lemma of all the words in the sentential context
        self.context_vector = context_vector
        self.key = key
        self.sense = sense
        self.pos = pos
        self.index = index  # index of lemma within the context

    def __str__(self):
        """
        For printing purposes.
        """
        return '%s\t%s\t%s\t%d' % (self.id, self.lemma, ' '.join(self.context), self.index)


def semcor_loader(parsed, remove_stop_words=False, word2vec=embeddings):
    """Loads SemCor data set"""
    instances = []
    keys = []
    all_sentences = []
    for parse in parsed:
        paragraphs = parse.getchildren()[0].getchildren()
        for paragraph in paragraphs:
            sentences = paragraph.iterchildren()
            all_sentences.extend(sentences)

    length = len(all_sentences)
    print(length)
    indices = np.random.choice(length, size=5000)
    for idx in indices:
        sent = all_sentences[idx]
        if remove_stop_words:
            context = [word.text for word in sent.iterchildren()]
            context = set(context).difference(EN_STOPWORDS)
            vector = np.array([catch(word2vec[word]) for word in context])
            context_vector = vector.mean(axis=0)

        else:
            vector = np.array([catch(word2vec[word.text]) for word in sent.iterchildren()])
            context_vector = vector.mean(axis=0)
            context = [word.text for word in sent.iterchildren()]

        for idx, word in enumerate(sent.iterchildren()):
            if word.get('cmd') == 'done' and word.get('lexsn') is not None:
                if word.text in context:
                    lemma = to_ascii(word.get('lemma'))
                    key = word.get('lexsn')
                    pos = word.get('pos')
                    sense = word.get('wnsn')
                    instances.append(SemCorInstance(lemma, context, context_vector, key, sense, pos, idx))
                    keys.append(sense)
                else:
                    continue

    return instances, keys


def load_data(url, savename=senseval2, filepath=senseval2_dir,
              type='r:gz', pattern=pattern_2, loader=senseval_loader, remove_stop_words=False, word2vec=embeddings):
    """Dataset Loader"""

    data(url, savename, type)
    files = get_filenames(filepath, pattern)
    print(files)
    parsed = parser(files)
    print(parsed)
    instances, keys = loader(parsed, remove_stop_words, word2vec)
    return instances, keys
