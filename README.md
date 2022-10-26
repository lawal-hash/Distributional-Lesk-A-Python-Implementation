
# **Distributional Lesk A Python Implementation**
Python implementation of the paper: [Distributional Lesk: Effective Knowledge-Based Word Sense Disambiguation](https://aclanthology.org/W17-6931/)
[![twitter](https://preview--sophia-634ad.stackbit.dev/_static/app-assets/images/WordItOut-word-cloud-5146156.png)]()

## **WSD Theory**

Word sense disambiguation is a very popular task in natural language processing. Words can have more than one meaning, also known as polysemy. Hence, if such words are used in a sentence, it may introduce ambiguity. Thus, it is important to disambiguate such words in a sentence, for example.

"Many banks in Frankfurt are located at the banks of Main."

In the above example, the word "bank" is an ambiguous word and occurs in positions two and nine in the above sentence. Therefore, to adequately disambiguate the word "bank," we must examine the context sentence carefully. In position four, we might intuitively assume this bank refers to a financial institution, although disambiguating position nine by intuition might be difficult. Could it also be a financial institution? (bank of banks) or a river bank (I haven’t visited Frankfurt, so I am not sure if there is a river in the Main). As seen in the above example, intuition is not an efficient way to disambiguate words as it often requires a vague idea of what the sentence is about; for example, knowing about the city of Main in Frankfurt. Researchers over the years have proposed different  unsupervised learning methods to disambiguate words.

### **Most Common Sense**
This method is widely used as a baseline (upper-bound) and is far more effective than human intuition. A word can have multiple senses, and each sense has lemmas.The idea behind the most common sense is that when given an ambiguous word with its senses, our most common sense will be the sense with the highest number of lemmas.

### **Plain Lesk**
The plain lesk was proposed in the 1980s. The idea behind plain lesk is quite interesting and mitigates the limitations of most common sense. For an ambiguous word and its context sentence, we determine the overlap between the synset definition and the context sentence. The sense with the highest overlap is the assigned sense. The plain lesk finds the intersection between the words in the context sentence and the gloss definition, given the gloss definition of synset ('bar.n.02').

Context sentence : "Let ’s have a drink in the bar."

Gloss definition: "a counter where you can obtain food or drink" 

We have two intersections between the context word and the gloss definition. The above process will be repeated for all the senses in an ambiguous word, and the sense with the highest overlap will be assigned. Although plain lesk mitigates the limitations of MCS, plain lesk performs poorly when stop words are removed from both the context sentence and synset definition.

### **Distributional Lesk**
The method proposed by [3] is an interesting WSD technique based on lesk [1], although with a few differences. First, we use the word embedding representation instead of the ambiguous word. Secondly, we use the average word embedding representation of the synset definition, known as the gloss vector. Thirdly, the average word embedding representation of the context sentence is known as the context vector. Finally, the use of lexemes is embedding.

Like plain lesk, distributional lesk computes the cosine similarity between the gloss sense and the sense of the words. For a given ambiguous word w, for each sense s in word w, we compute the score given by

[![twitter](https://latex.codecogs.com/svg.image?\mathrm{Score}(s,&space;w)=\cos&space;\left(G_s,&space;C_w\right)&plus;\cos&space;\left(L_{s,&space;w},&space;C_w\right))]()

[![twitter](https://latex.codecogs.com/svg.image?G_s$,$C_w$,&space;and&space;$L_{s,&space;w}&space;\textrm{&space;represent&space;gloss&space;vector,&space;context&space;vector,&space;and&space;lexemes&space;vector&space;respectively.})]() 

The sense with the highest score is the assigned or returned sense.

## **Run Locally**

Clone the project

```bash
  git clone https://github.com/lawal-hash/Distributional-Lesk-A-Python-Implementation.git
```

Go to the project directory

```bash
  cd Distributional-Lesk-A-Python-Implementation
```

Install dependencies

```bash
  pip download requirements.txt
```

# **Conclusion**
This repo successfully re-implemented the results of [3], including its baseline with an additional extension. Although the most common sense technique has obvious limitations, it is very difficult to beat this baseline. After removing stopwords and punctuation from dictionary glosses, sense descriptions, and contexts in the occurrences of the words before measuring distance, the accuracy of plain lesk significantly decreases. On the other hand, distributional lesk is not affected when stop words and punctuation are removed; the results were as good as the initial results obtained(with stop words and punctuation).


# **References**

*  Michael Lesk. Automatic sense disambiguation using machine readable dic- tionaries: how to tell a pine code from an ice cream cone. _In Proceedings of the 5th annual international conference on Systems documentation_ - SIG- DOC ’86, pages 24–26, Toronto, Ontario, Canada, 1986. ACM Press
*  Tomas Mikolov, Ilya Sutskever, Kai Chen, Greg S Corrado, and Jeff Dean. Distributed Representations of Words and Phrases and their Composition- ality. In _Advances in Neural Information Processing Systems_, volume 26. Curran Associates, Inc., 2013.
*  Dieke Oele and Gertjan van Noord. Distributional Lesk: Effective Knowledge-Based Word Sense Disambiguation. In _IWCS 2017 — 12th International Conference on Computational Semantics_ — Short papers, 2017
*  Sascha Rothe and Hinrich Schu ̈tze. AutoExtend: Extending Word Embed- dings to Embeddings for Synsets and Lexemes. In _Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)_, pages 1793–1803, Beijing, China, July 2015. Association for Computational Linguistics.



## Author

- [@lawal-hash](https://github.com/lawal-hash)


## Contributing

Find any typos? Contributions are welcome!

First, fork this repository.

[![portfolio](https://raw.githubusercontent.com/udacity/ud777-writing-readmes/master/images/fork-icon.png)]()



Next, clone this repository to your desktop to make changes.

```
$ git clone {YOUR_REPOSITORY_CLONE_URL}

```


Once you've pushed changes to your local repository, you can issue a pull request by clicking on the green pull request icon.

[![portfolio](https://raw.githubusercontent.com/udacity/ud777-writing-readmes/master/images/pull-request-icon.png)]()

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)]()
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sophia-lawal/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Ayan_Yemi)

