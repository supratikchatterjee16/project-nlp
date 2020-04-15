# Project NLP

## Introduction

During a previous project work, it was found that NLTK lags behind on multiple aspects and fails to deliver on aspects it should have. 
This problem while has been attempted by many to rectify, it hasn't been done in any easy to understand format.

My approach to the problem is to provide the system perfect information of the words, 
and to make the system develop a logical sense of actually understanding them.

It is a gereal intelligence based program, that should enable the computer to look into each language fed, objectively, 
and create human verifiable logics.

Current goals for this experiment are the folllowing:

1. Precise Named Entity Recognition
2. Accurate Co-Reference resolution, both Anaphoric as well as Cataphoric
3. Interlingua Tree Generations
4. Fact finding and Fact understanding

The experiment is supposed to make an intelligent subsystem for textual comprehension and response generation.

## Technologies in use

1. Python3.8 is the language most things will be developed in
2. For my data intensive projects, I make use of 
	a. PostgreSQL
	b. MongoDB. 
3. Furthermore to simulate STM nodes, I will be making use of Redis.
4. There are various other Python Modules in use, kindly check requirements.txt for a full list

I am waiting for python bindings in Rust, till the completion of a significant part of the project.
When and as the project enters Production usage capable standards, I will look into making them on my own, 
possibly through Cython.

## POS tagging

This is the current system of interest, as it forms the core of almost all other work.

We understand what a word is, however, the computer is unable to do the same. 
POS tags logic developed for this is targetted towards accurately knowing what a word is, 
such that when unknown words are thrown at it, it is able to rectify, or understand it's 'intention'.

Understanding sarcasm and jokes for a computer is a step that would allow it to make real intelligent conversations.

We have different taggers available already, a few of which are:
1. NLTK perceptron tagger 
2. Hunter POS tagger
3. Stanford POS tagger
4. Senna POS tagger

While they haven't been completely looked into, the information they provide creates an information chasm, 
that could be covered by providing the statistical information to them.

Reducing the statistical workload is a matter for later.

Previous taggers most commonly make use of N-gram models to predict the tagging, and provide a single tag for it.
