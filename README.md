# EmoEEG-MC: A Multi-Context Emotional EEG Dataset for Cross-Context Emotion Decoding

## Authors

Xin XU[^1,†], Xinke SHEN[^1,†,*], Xuyang CHEN[^1], Qingzhu ZHANG[^1], Sitian WANG[^1], Yihan LI[^1], Zongsheng LI[^1,^2], Dan ZHANG[^3], Mingming ZHANG[^1], Quanying LIU[^1,*]

[^1]: Department of Biomedical Engineering, Southern University of Science and Technology, Shenzhen, 518055, China  
[^2]: School of Science and Engineering, The Chinese University of Hong Kong, Shenzhen, 518172, China  
[^3]: Department of Psychological and Cognitive Sciences, Tsinghua University, Beijing, 100084, China  

*Corresponding authors:* Quanying LIU (liuqy@sustech.edu.cn); Xinke SHEN (shenxk@sustech.edu.cn)  
† These authors contributed equally to this work.

---

## Abstract

Decoding emotions using electroencephalography (EEG) is gaining increasing attention due to its objectivity in measuring emotional states. However, the ability of existing EEG-based emotion decoding methods to generalize across different contexts remains underexplored, as most approaches are trained and evaluated only within a single context. Studying emotions across multiple contexts is essential for advancing our understanding of the neural mechanisms underlying emotional processing and enhancing the real-world applicability of affective computing systems.

A key limitation in this field is the lack of EEG datasets designed specifically to capture emotional responses across diverse contexts. To address this gap, we present the **Multi-Context Emotional EEG (EmoEEG-MC) dataset**, featuring 64-channel EEG and peripheral physiological data from 60 participants exposed to two distinct contexts: video-induced and imagery-induced emotions. These contexts evoke seven distinct emotional categories: joy, inspiration, tenderness, fear, disgust, sadness, and neutral emotion. The emotional experience of a specific emotion category was validated through subjective reports.

Using Support Vector Machines (SVMs) with L1 regularization, we achieved cross-context emotion decoding accuracies of 66.7% for binary classification (positive vs. negative emotions) and 28.9% for seven-category emotion classification, both significantly above chance levels. The **EmoEEG-MC dataset** serves as a foundational resource for advancing cross-context emotion recognition and enhancing the real-world application of emotion decoding methods.

## Codes
These files are codes for preprocessing and stimuli material embeddings. You can find the dataset via OpenNeuro(doi:10.18112/openneuro.ds005540.v1.0.3) or ScienceDB(10.57760/sciencedb.14025).
