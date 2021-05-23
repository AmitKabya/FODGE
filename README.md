# FODGE - Fast Online Dynamic Graph Embedding

### Contact
********@gmail.com

## Overview

FODGE is a novel dynamic graph embedding algorithm (DGEA) to gradually shift the projection of modified vertices. FODGE optimizes CPU And memory efficacy by separating the projection of the graph densest K-core and its periphery. FODGE then smoothly updates the projection of the remaining vertices, through an iterative local update rule. As such it can be applied to extremely large dynamic graphs. Moreover, it is highly modular and can be combined with any static projection, including graph convolutional networks, and has a few hyperparameters to tune. FODGE obtains a better performance in auxiliary task of link prediction and ensures a limited difference in vertex positions in following time points.

## About This Repo

This repo contains source code of the FODGE dynamic graph embedding algorithm. 

### The Directories

- `datasets` - Examples of datasets files
- `fodge` - The main files to run the FODGE framework
- `GEA` - State-of-the-art static graph embedding algorithms implementations, currently [node2vec](https://arxiv.org/abs/1607.00653)/[GF](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/40839.pdf)/[HOPE](https://www.kdd.org/kdd2016/papers/files/rfp0184-ouA.pdf)/[GCN](https://arxiv.org/abs/1609.02907)/[GAE](https://arxiv.org/abs/1611.07308).
- `evaluation_tasks` - Implementation of temporal link prediction task + main file to calculate the embedding and evaluate performance

#### Notes:
- The implementations of GF and HOPE were taken from [GEM toolkit](https://github.com/palash1992/GEM)
- Node2vec is implemented using [node2vec public package](https://github.com/eliorc/node2vec)
- The implementation of GCN was taken from their [public github repository](https://github.com/tkipf/pygcn)
- The implementation of GAE was taken from their [public github repository](https://github.com/tkipf/gae)

## Dependencies
- python >=3.6.8
- numpy >= 1.18.0
- scikit-learn >= 0.22.1
- heapq
- node2vec==0.3.2
- networkx==1.11
- scipy >= 1.41
- pytorch==1.7.0
- matplotlib==3.1.3
- pandas >= 1.0.5
- tensorflow == 2.4.1
- keras == 2.4.3

## Cloning This Repo

If this repository is cloned as a pycharm project, one needs to make all the directories as sources directories.

## Datasets
- Facebook
- Facebook Friendships
- Facebook Wall Posts
- DBLP
- Math
- Enron
- Wiki Temporal

**Note:** All the datasets used can be found in this [google drive link](https://drive.google.com/drive/folders/15tlgyf3GO8s8HjCsd5S5zQ7_n28DafA7?usp=sharing). 

If you use one of these datasets, all you have to do is choose the dataset (see name of directories) and put the appropriate `.txt` file in `datasets`directory. 

If you want to use your own dataset, you should follow this format: Give a single `.txt` file where each row is in the form:

Notice you will have to adjust them to our files format (will be further explained) or provide a data loader function in order to produce the networkx graph. For .mat files, see how Youtube and Flickr datasets are loaded. You can add the appropriate condition to the function "load_data" in evaluation_tasks -> eval_utils.py. Note that when having .mat file, it has both the edges and labels. To see an example for a use go to "load_data" in evaluation_tasks -> eval_utils.py and to evaluation_tasks -> calculate_static_embeddings.py.
