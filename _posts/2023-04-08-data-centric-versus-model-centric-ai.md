---
layout: post
title:  "Data-Centric AI vs. Model-Centric AI"
short_title: "Data vs. Models"
series: "Introduction to Data-Centric AI"
date:   2023-03-31
format_equations: false
include_bokeh: false
visible: true
---

# Introduction to Data-Centric AI
Traditional approaches to machine learning commonly follow a model-centric paradigm, in which the greatest effort is spent making improvements to model architectures, tuning hyperparameters, modifying loss functions, or introducing regularisation. In an academic setting, this is often done using the assumption of having a fixed clean dataset. However, it has been demonstrated that popular academic datasets contain labelling errors (see the website by [Northcutt et al.](https://labelerrors.com)), thus the results of experiments may be biased or not reflect the performance when tested using real world data.

A data-centric paradigm places emphasis on using systematic methods to help improve the quality and quantity of data available during training and testing, with an ambition to produce more favourable outcomes (e.g., better generalisation, consistent performance across subpopulations, etc.) that are independent of model design. Within this series, there are two overarching data-centric approaches:
1. Development of techniques to better understand existing data and leverage this information to train better models. For example, Curriculum Learning<a style="text-decoration: none;" href="#cite-curriculum-learning"><sup>[1]</sup></a> and coreset selection<a style="text-decoration: none;" href="#cite-coreset-selection"><sup>[2]</sup></a>.
2. Development of techniques to modify existing data to train better models. For example, Confident Learning<a style="text-decoration: none;" href="#cite-confident-learning"><sup>[3]</sup></a> and data augmentation<a style="text-decoration: none;" href="#cite-data-augmentation"><sup>[4]</sup></a>.

In summary, a model-centric approach is centered around taking any dataset and producing the best possible model, while a data-centric approach leverages systematic approaches to produce the best possible dataset, which in turn can be used to train "better" models.


# Lab

# References
<ol>
<li id="cite-curriculum-learning">
    <span><cite>Bengio, Y., Louradour, J., Collobert, R. and Weston, J., 2009, June. Curriculum learning. In Proceedings of the 26th annual international conference on machine learning (pp. 41-48).</cite></span>
</li>

<li id="cite-coreset-selection">
    <span><cite>Mirzasoleiman, B., Bilmes, J. and Leskovec, J., 2020, November. Coresets for data-efficient training of machine learning models. In International Conference on Machine Learning (pp. 6950-6960). PMLR.</cite></span>
</li>

<li id="cite-confident-learning">
    <span><cite>Northcutt, C., Jiang, L. and Chuang, I., 2021. Confident learning: Estimating uncertainty in dataset labels. Journal of Artificial Intelligence Research, 70, pp.1373-1411.</cite></span>
</li>

<li id="cite-data-augmentation">
    <span><cite>Shorten, C., Khoshgoftaar, T.M. and Furht, B., 2021. Text data augmentation for deep learning. Journal of big Data, 8, pp.1-34.</cite></span>
</li>
</ol>