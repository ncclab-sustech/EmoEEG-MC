# EmoEEG-MC: A Multi-Context Emotional EEG Dataset for Cross-Context Emotion Decoding

## Abstract

EEG-basedemotion decoding is essential for unveiling neural mechanisms underlying emotion and enabling artificial intelligence to understand human emotions. However, existing datasets for EEG-based emotion decoding are limited to a single context of emotion elicitation. The ability of emotion decoding methods to generalize across different contexts remains underexplored. To address this gap, we present the **Multi-Context Emotional EEG (EmoEEG-MC)** dataset, featuring 64-channel EEG and peripheral physiological data from 60 participants exposed to two distinct contexts: video-induced and imagery-induced emotions. These contexts evoke seven distinct emotional categories: joy, inspiration, tenderness, fear, disgust, sadness, and neutral emotion. The emotional experience of specific emotion categories was validated through subjective reports. Using support vector machines with L1 regularization, we achieved cross-context emotion decoding accuracies of 66.7% for binary classification (positive vs. negative emotions) and 28.9% for seven-category emotion classification, both significantly above chance levels. The EmoEEG-MC dataset serves as a foundational resource for understanding the neural mechanisms underlying emotional processing and enhancing the real-world applicability of affective computing systems.

## Introduction
<img src=".\fima\2.png" alt="framework" style="zoom:80%;" />


## Codes
These files are codes for preprocessing and stimuli material embeddings. You can find the dataset via OpenNeuro(doi:10.18112/openneuro.ds005540.v1.0.3) or ScienceDB(10.57760/sciencedb.14025).
