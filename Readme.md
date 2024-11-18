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

## Dataset Description

The dataset includes EEG data from 60 participants, along with peripheral physiological data (PPG and GSR) for some participants. Among the 60 participants, **sub01-sub54** have complete trials (21 imagery trials and 21 video trials), while **sub55-sub60** have missing trials. The details of the missing trials are as follows:

- **sub55**: Missing 3 imagery trials (Trials 19-21) and 3 video trials (Trials 40-42).
- **sub56**: Missing 2 imagery trials (Trials 20 and 21).
- **sub57**: Missing 4 imagery trials (Trials 6, 8, 13, and 21) and 6 video trials (Trials 23, 24, 36, 37, 38, and 42).
- **sub58**: Missing 3 imagery trials (Trials 9, 20, and 21).
- **sub59**: Missing 6 imagery trials (Trials 2, 4, 6, 12, 19, and 21) and 4 video trials (Trials 29, 37, 39, and 42).
- **sub60**: Missing 14 imagery trials (Trials 8-21) and 12 video trials (Trials 31-42).

All missing values are denoted as **n/a** in the participants' behavioral data.

## Experimental Trial Reordering and Missing Trial Information

### Trial Reordering

After reordering, the sequence for both imagery and video trials is as follows:

`reorder = ['sad4', 'sad5', 'sad8', 'dis4', 'dis5', 'dis8', 'fear4', 'fear5', 'fear8', 'neu4', 'neu5', 'neu8', 'joy4', 'joy5', 'joy8', 'ten4', 'ten5', 'ten8', 'ins4', 'ins5', 'ins8']`

### Full Trial Participants

For participants with complete trials (**sub01-sub54**, with the same order for both imagery and video trials; detailed stimulus information can be found in `sub-xx/sub-xx_events`), the experimental sequence is as follows:

1. `['joy5', 'ins5', 'joy8', 'fear8', 'sad8', 'dis5', 'neu4', 'neu5', 'neu8', 'ten5', 'ten8', 'joy4', 'dis4', 'fear4', 'sad4', 'ins8', 'ins4', 'ten4', 'dis8', 'fear5', 'sad5']`
2. `['fear8', 'fear5', 'dis4', 'ins8', 'joy8', 'ins4', 'neu4', 'neu8', 'neu5', 'sad4', 'dis8', 'fear4', 'ten5', 'ten8', 'joy4', 'dis5', 'sad8', 'sad5', 'joy5', 'ten4', 'ins5']`
3. `['ten4', 'joy4', 'joy8', 'neu4', 'neu8', 'neu5', 'dis5', 'fear4', 'fear5', 'ten8', 'ten5', 'ins5', 'fear8', 'dis4', 'dis8', 'ins8', 'joy5', 'ins4', 'sad4', 'sad5', 'sad8']`
4. `['fear5', 'dis8', 'dis5', 'joy4', 'ten5', 'ins5', 'neu4', 'neu8', 'neu5', 'sad8', 'fear8', 'sad4', 'ins4', 'ins8', 'joy8', 'fear4', 'sad5', 'dis4', 'ten4', 'joy5', 'ten8']`
5. `['joy8', 'ten4', 'ins5', 'fear5', 'sad5', 'dis4', 'neu4', 'neu5', 'neu8', 'joy4', 'ten8', 'joy5', 'sad4', 'dis8', 'fear8', 'ins4', 'ten5', 'ins8', 'sad8', 'dis5', 'fear4']`
6. `['joy8', 'ins5', 'ins8', 'dis4', 'dis8', 'fear8', 'ten4', 'joy5', 'ten5', 'dis5', 'fear5', 'fear4', 'ten8', 'ins4', 'joy4', 'sad8', 'sad4', 'sad5', 'neu4', 'neu5', 'neu8']`
7. `['joy8', 'ten8', 'joy4', 'fear4', 'sad5', 'dis5', 'ins5', 'ten5', 'ten4', 'dis4', 'sad8', 'dis8', 'ins4', 'ins8', 'joy5', 'sad4', 'fear8', 'fear5', 'neu4', 'neu5', 'neu8']`
8. `['neu4', 'neu5', 'neu8', 'dis8', 'sad4', 'fear5', 'ins4', 'ins5', 'ten5', 'dis4', 'sad8', 'fear4', 'ins8', 'joy4', 'ten8', 'fear8', 'dis5', 'sad5', 'ten4', 'joy8', 'joy5']`
9. `['sad5', 'fear4', 'fear8', 'joy4', 'joy8', 'ten5', 'dis8', 'dis5', 'sad4', 'neu4', 'neu8', 'neu5', 'ins8', 'ten8', 'ins4', 'sad8', 'fear5', 'dis4', 'joy5', 'ten4', 'ins5']`
10. `['sad4', 'fear5', 'sad8', 'joy8', 'ten8', 'joy4', 'sad5', 'dis8', 'fear4', 'neu4', 'neu8', 'neu5', 'ten4', 'ten5', 'ins4', 'dis4', 'fear8', 'dis5', 'joy5', 'ins5', 'ins8']`
11. `['joy4', 'ins4', 'joy5', 'fear8', 'dis8', 'sad4', 'ten8', 'ins5', 'ten5', 'sad5', 'sad8', 'fear5', 'ins8', 'ten4', 'joy8', 'neu8', 'neu4', 'neu5', 'fear4', 'dis4', 'dis5']`
12. `['sad8', 'fear5', 'fear8', 'ten8', 'ten5', 'joy8', 'fear4', 'sad4', 'sad5', 'neu4', 'neu8', 'neu5', 'ins8', 'ins4', 'ten4', 'dis5', 'dis8', 'dis4', 'joy5', 'joy4', 'ins5']`
13. `['sad8', 'dis8', 'sad4', 'ten4', 'ten8', 'ins4', 'dis5', 'fear8', 'sad5', 'ten5', 'ins5', 'joy8', 'neu4', 'neu8', 'neu5', 'fear5', 'fear4', 'dis4', 'joy4', 'joy5', 'ins8']`
14. `['ins8', 'ten4', 'ins5', 'neu4', 'neu8', 'neu5', 'sad5', 'dis4', 'sad4', 'ins4', 'ten8', 'ten5', 'dis8', 'sad8', 'fear8', 'joy5', 'joy4', 'joy8', 'fear4', 'fear5', 'dis5']`
15. `['ins8', 'ten5', 'ten8', 'sad8', 'sad4', 'sad5', 'joy4', 'ins4', 'ins5', 'fear8', 'fear5', 'fear4', 'ten4', 'joy5', 'joy8', 'neu5', 'neu4', 'neu8', 'dis4', 'dis5', 'dis8']`
16. `['fear4', 'dis4', 'fear8', 'ins8', 'joy8', 'ten8', 'dis5', 'sad4', 'dis8', 'ins5', 'ins4', 'joy4', 'neu8', 'neu4', 'neu5', 'fear5', 'sad8', 'sad5', 'joy5', 'ten5', 'ten4']`
17. `['ten5', 'ins4', 'ins8', 'dis8', 'fear4', 'sad5', 'ins5', 'joy8', 'ten4', 'sad8', 'fear8', 'fear5', 'ten8', 'joy5', 'joy4', 'sad4', 'dis5', 'dis4', 'neu5', 'neu4', 'neu8']`
18. `['neu4', 'neu5', 'neu8', 'sad4', 'dis8', 'dis5', 'joy4', 'ten4', 'ten5', 'sad5', 'fear5', 'fear4', 'ins5', 'ins4', 'ten8', 'dis4', 'fear8', 'sad8', 'joy8', 'ins8', 'joy5']`
19. `['joy5', 'ten8', 'ins4', 'fear4', 'dis8', 'sad4', 'ten5', 'joy8', 'joy4', 'sad8', 'dis5', 'fear8', 'neu8', 'neu4', 'neu5', 'ins5', 'ten4', 'ins8', 'fear5', 'dis4', 'sad5']`
20. `['joy5', 'ins8', 'joy4', 'neu4', 'neu5', 'neu8', 'fear4', 'sad4', 'fear8', 'ins5', 'ten4', 'ten5', 'dis4', 'sad8', 'sad5', 'ten8', 'ins4', 'joy8', 'dis5', 'fear5', 'dis8']`
21. `['ten8', 'joy4', 'ins5', 'sad4', 'dis4', 'fear8', 'ins8', 'joy8', 'ins4', 'neu8', 'neu4', 'neu5', 'sad5', 'sad8', 'fear5', 'ten5', 'joy5', 'ten4', 'fear4', 'dis5', 'dis8']`
22. `['joy5', 'ten8', 'ten4', 'dis4', 'fear4', 'fear5', 'joy8', 'ten5', 'joy4', 'sad5', 'sad8', 'dis8', 'neu5', 'neu8', 'neu4', 'ins4', 'ins5', 'ins8', 'fear8', 'sad4', 'dis5']`
23. `['neu4', 'neu5', 'neu8', 'dis4', 'fear4', 'sad8', 'ins8', 'joy4', 'ten8', 'fear8', 'fear5', 'sad5', 'ten4', 'ins5', 'joy8', 'dis8', 'sad4', 'dis5', 'ten5', 'joy5', 'ins4']`
24. `['joy5', 'ten5', 'ins4', 'fear4', 'sad8', 'sad4', 'ins5', 'ten4', 'ten8', 'sad5', 'fear5', 'fear8', 'ins8', 'joy8', 'joy4', 'dis8', 'dis5', 'dis4', 'neu8', 'neu4', 'neu5']`
25. `['dis8', 'dis5', 'sad4', 'ins8', 'ten4', 'joy8', 'sad8', 'fear4', 'fear8', 'joy5', 'ins4', 'ten8', 'dis4', 'fear5', 'sad5', 'neu8', 'neu5', 'neu4', 'joy4', 'ins5', 'ten5']`
26. `['fear4', 'sad5', 'fear8', 'ten4', 'ins5', 'joy8', 'dis4', 'dis8', 'sad8', 'ins4', 'joy5', 'joy4', 'dis5', 'sad4', 'fear5', 'ins8', 'ten8', 'ten5', 'neu5', 'neu8', 'neu4']`
27. `['dis4', 'dis5', 'fear4', 'ins8', 'ins4', 'joy5', 'sad8', 'fear8', 'sad5', 'ins5', 'joy4', 'ten8', 'neu4', 'neu8', 'neu5', 'fear5', 'sad4', 'dis8', 'ten4', 'ten5', 'joy8']`
28. `['ten4', 'ins5', 'joy4', 'dis5', 'sad5', 'fear4', 'ins8', 'joy8', 'ins4', 'fear5', 'fear8', 'dis8', 'neu5', 'neu8', 'neu4', 'ten8', 'joy5', 'ten5', 'sad4', 'dis4', 'sad8']`
29. `['joy5', 'ten5', 'ins5', 'neu8', 'neu4', 'neu5', 'fear5', 'sad8', 'sad5', 'joy8', 'ten8', 'joy4', 'fear8', 'fear4', 'dis4', 'ten4', 'ins8', 'ins4', 'dis8', 'dis5', 'sad4']`
30. `['sad8', 'dis8', 'dis5', 'joy5', 'ten4', 'joy4', 'sad5', 'fear5', 'fear8', 'ten8', 'ins8', 'ins4', 'sad4', 'fear4', 'dis4', 'joy8', 'ins5', 'ten5', 'neu5', 'neu8', 'neu4']`
31. `['dis4', 'dis8', 'sad4', 'neu5', 'neu4', 'neu8', 'joy5', 'ins8', 'ins4', 'fear4', 'fear8', 'sad8', 'ins5', 'ten8', 'joy4', 'sad5', 'dis5', 'fear5', 'ten4', 'joy8', 'ten5']`
32. `['joy5', 'joy4', 'ten4', 'sad5', 'fear5', 'fear4', 'ins5', 'ten8', 'ins8', 'dis8', 'dis5', 'sad8', 'ten5', 'ins4', 'joy8', 'sad4', 'fear8', 'dis4', 'neu5', 'neu8', 'neu4']`
33. `['sad5', 'dis8', 'dis5', 'ins5', 'ten5', 'ten4', 'dis4', 'fear4', 'fear5', 'ten8', 'ins8', 'joy4', 'neu5', 'neu4', 'neu8', 'fear8', 'sad4', 'sad8', 'joy5', 'joy8', 'ins4']`
34. `['ten5', 'ins5', 'joy4', 'sad4', 'fear5', 'fear4', 'ten8', 'joy8', 'ins8', 'dis8', 'sad5', 'dis5', 'joy5', 'ten4', 'ins4', 'dis4', 'fear8', 'sad8', 'neu4', 'neu8', 'neu5']`
35. `['sad4', 'fear8', 'dis4', 'ins4', 'ins8', 'joy4', 'neu8', 'neu5', 'neu4', 'sad8', 'fear4', 'dis5', 'ten4', 'ten5', 'ten8', 'sad5', 'dis8', 'fear5', 'joy8', 'ins5', 'joy5']`
36. `['joy5', 'joy4', 'joy8', 'dis4', 'dis8', 'fear5', 'neu5', 'neu8', 'neu4', 'ins4', 'ten5', 'ten4', 'dis5', 'sad5', 'fear4', 'ten8', 'ins8', 'ins5', 'sad4', 'sad8', 'fear8']`
37. `['fear4', 'dis5', 'sad5', 'neu5', 'neu4', 'neu8', 'ins8', 'joy8', 'ten5', 'fear5', 'sad4', 'fear8', 'ins4', 'joy4', 'ten8', 'dis4', 'dis8', 'sad8', 'joy5', 'ins5', 'ten4']`
38. `['joy8', 'ten8', 'ins8', 'fear8', 'sad4', 'fear5', 'ten4', 'ten5', 'joy5', 'sad8', 'dis4', 'fear4', 'neu4', 'neu5', 'neu8', 'ins5', 'ins4', 'joy4', 'sad5', 'dis8', 'dis5']`
39. `['ins4', 'ten8', 'joy4', 'neu5', 'neu8', 'neu4', 'dis8', 'fear4', 'sad8', 'ins5', 'joy8', 'ten4', 'dis5', 'dis4', 'fear5', 'ins8', 'ten5', 'joy5', 'fear8', 'sad5', 'sad4']`
40. `['ins4', 'ten4', 'ins5', 'sad5', 'dis5', 'fear4', 'neu5', 'neu8', 'neu4', 'ten5', 'ins8', 'joy4', 'sad8', 'fear5', 'sad4', 'ten8', 'joy5', 'joy8', 'dis8', 'dis4', 'fear8']`
41. `['ins5', 'ten8', 'ins4', 'dis8', 'sad4', 'dis5', 'joy8', 'ten5', 'ins8', 'neu8', 'neu4', 'neu5', 'fear8', 'dis4', 'fear5', 'joy4', 'joy5', 'ten4', 'sad5', 'sad8', 'fear4']`
42. `['ten8', 'ten4', 'joy8', 'dis8', 'sad5', 'sad4', 'joy5', 'ins8', 'ins4', 'neu4', 'neu5', 'neu8', 'fear4', 'dis4', 'fear5', 'ins5', 'ten5', 'joy4', 'dis5', 'fear8', 'sad8']`
43. `['ins5', 'ten5', 'ins4', 'neu5', 'neu8', 'neu4', 'sad4', 'dis4', 'sad5', 'ins8', 'joy8', 'joy4', 'fear8', 'fear4', 'dis8', 'ten8', 'ten4', 'joy5', 'dis5', 'sad8', 'fear5']`
44. `['sad8', 'dis5', 'dis4', 'joy5', 'ins5', 'joy8', 'sad5', 'sad4', 'fear5', 'ten4', 'ten8', 'ins4', 'neu8', 'neu5', 'neu4', 'dis8', 'fear8', 'fear4', 'joy4', 'ten5', 'ins8']`
45. `['ins5', 'joy8', 'ins8', 'fear8', 'fear5', 'sad5', 'joy5', 'ten8', 'ten5', 'neu5', 'neu4', 'neu8', 'dis5', 'dis8', 'sad4', 'ins4', 'ten4', 'joy4', 'sad8', 'dis4', 'fear4']`
46. `['fear5', 'dis5', 'dis8', 'ins5', 'ten5', 'ten8', 'neu8', 'neu4', 'neu5', 'fear8', 'dis4', 'sad4', 'ten4', 'ins8', 'ins4', 'sad5', 'sad8', 'fear4', 'joy8', 'joy4', 'joy5']`
47. `['ins4', 'joy5', 'joy8', 'sad5', 'fear5', 'dis8', 'neu8', 'neu4', 'neu5', 'ins8', 'ten4', 'joy4', 'fear8', 'dis5', 'sad8', 'ins5', 'ten8', 'ten5', 'sad4', 'dis4', 'fear4']`
48. `['joy5', 'ins8', 'ins5', 'dis8', 'dis5', 'fear5', 'ten4', 'ins4', 'joy8', 'dis4', 'fear4', 'sad5', 'ten8', 'ten5', 'joy4', 'fear8', 'sad8', 'sad4', 'neu8', 'neu4', 'neu5']`
49. `['dis4', 'sad5', 'sad4', 'neu4', 'neu8', 'neu5', 'joy4', 'ten5', 'ten8', 'dis8', 'fear8', 'dis5', 'ins4', 'joy8', 'ten4', 'fear4', 'sad8', 'fear5', 'ins8', 'ins5', 'joy5']`
50. `['ten5', 'ins8', 'ins4', 'neu4', 'neu8', 'neu5', 'fear4', 'fear8', 'dis4', 'joy4', 'ten4', 'ins5', 'fear5', 'sad5', 'dis8', 'ten8', 'joy8', 'joy5', 'sad4', 'sad8', 'dis5']`
51. `['ten8', 'joy8', 'ten5', 'dis8', 'fear5', 'dis4', 'joy5', 'ten4', 'ins4', 'fear4', 'sad4', 'dis5', 'neu8', 'neu4', 'neu5', 'ins8', 'ins5', 'joy4', 'sad5', 'fear8', 'sad8']`
52. `['joy4', 'joy5', 'ins8', 'fear5', 'dis5', 'dis8', 'neu5', 'neu4', 'neu8', 'joy8', 'ins5', 'ten5', 'sad5', 'fear4', 'dis4', 'ten4', 'ten8', 'ins4', 'sad8', 'fear8', 'sad4']`
53. `['neu8', 'neu4', 'neu5', 'dis5', 'sad4', 'fear4', 'joy5', 'ins4', 'ten4', 'fear8', 'sad5', 'sad8', 'ten8', 'joy4', 'ten5', 'fear5', 'dis4', 'dis8', 'joy8', 'ins5', 'ins8']`

- **sub54 Imagery sequence**:  
  `['ten8', 'ten5', 'ten4', 'fear8', 'fear5', 'fear4', 'dis8', 'dis5', 'dis4', 'joy8', 'joy5', 'joy4', 'sad8', 'sad5', 'sad4', 'neu8', 'neu5', 'neu4', 'ins8', 'ins5', 'ins4']`

- **sub54 Video sequence**:  
  `['joy8', 'joy5', 'joy4', 'sad8', 'sad5', 'sad4', 'dis8', 'dis5', 'dis4', 'ins8', 'ins5', 'ins4', 'fear8', 'fear5', 'fear4', 'neu8', 'neu5', 'neu4', 'ten8', 'ten5', 'ten4']`


### Participants with Missing Trials

For participants with missing trials (**sub55-sub60**), the experimental sequences differ slightly:

- **sub55**: The sequence for imagery and video trials is:  
  `['dis5', 'sad4', 'fear8', 'joy4', 'joy5', 'ten8', 'fear5', 'sad8', 'sad5', 'joy8', 'ten5', 'ins8', 'dis8', 'dis4', 'fear4', 'ins5', 'ten4', 'ins4']`

- **sub56**:  
  - Imagery sequence:  
    `['joy8', 'joy5', 'ins4', 'sad4', 'fear5', 'dis8', 'neu4', 'neu8', 'neu5', 'ten8', 'joy4', 'ins5', 'fear4', 'dis5', 'sad8', 'ins8', 'ten5', 'ten4', 'sad5']`
  - Video sequence:  
    `['joy8', 'joy5', 'ins4', 'sad4', 'fear5', 'dis8', 'neu4', 'neu8', 'neu5', 'ten8', 'joy4', 'ins5', 'fear4', 'dis5', 'sad8', 'ins8', 'ten5', 'ten4', 'sad5', 'dis4', 'fear8']`

- **sub57**:  
  - Imagery sequence:  
    `['neu8', 'neu5', 'neu4', 'ins4', 'joy5', 'sad5', 'sad8', 'ins8', 'joy4', 'ten8', 'dis5', 'fear8', 'joy8', 'ins5', 'ten5', 'fear4', 'fear5']`
  - Video sequence:  
    `['neu8', 'ins4', 'joy5', 'ten4', 'sad5', 'sad4', 'sad8', 'ins8', 'joy4', 'ten8', 'dis8', 'dis5', 'ten5', 'fear4', 'fear5']`

- **sub58**:  
  - Imagery sequence:  
    `['sad5', 'fear5', 'sad8', 'ins8', 'joy5', 'joy4', 'sad4', 'dis8', 'neu5', 'neu8', 'neu4', 'ten8', 'joy8', 'ten4', 'fear4', 'fear8', 'dis5', 'ins5']`
  - Video sequence:  
    `['sad5', 'fear5', 'sad8', 'ins8', 'joy5', 'joy4', 'sad4', 'dis8', 'dis4', 'neu5', 'neu8', 'neu4', 'ten8', 'joy8', 'ten4', 'fear4', 'fear8', 'dis5', 'ins5', 'ten5', 'ins4']`

- **sub59**:  
  - Imagery sequence:  
    `['dis5', 'fear4', 'ins8', 'fear8', 'dis8', 'fear5', 'neu4', 'neu8', 'joy4', 'ten8', 'ten4', 'dis4', 'sad5', 'sad4', 'joy5']`
  - Video sequence:  
    `['dis5', 'sad8', 'fear4', 'joy8', 'ins8', 'ins5', 'fear8', 'fear5', 'neu4', 'neu8', 'neu5', 'joy4', 'ten8', 'ten4', 'sad5', 'ten5', 'joy5']`

- **sub60**:  
  - Imagery sequence:  
    `['neu5', 'neu4', 'neu8', 'dis5', 'sad4', 'dis4', 'ten4']`
  - Video sequence:  
    `['neu5', 'neu4', 'neu8', 'dis5', 'sad4', 'dis4', 'ten4', 'ins4', 'ten5']`

### Participants' Behaviour Reports
The ten behavioral rating items for the participants are as follows: 

- Joy
- Inspiration
- Tenderness
- Sadness
- Fear
- Disgust
- Arousal
- Valence
- Familiarity
- Liking

### Channels
The EEG channels follow the 10-20 system with 64 channels, and the channel names are as follows:

'Fp1', 'Fpz', 'Fp2', 'AF7', 'AF3','AF4','AF8', 'F7', 'F5','F3','F1','Fz', 'F2', 'F4', 'F6', 'F8',
'FT7', 'FC5', 'FC3', 'FC1','FCz','FC2','FC4', 'FC6', 'FT8', 'T7','C5', 'C3', 'C1', 'Cz', 'C2', 'C4', 'C6', 'T8',
'TP7', 'CP5', 'CP3', 'CP1','CPz','CP2', 'CP4','CP6', 'TP8', 'P7','P5', 'P3', 'P1', 'Pz','P2', 'P4', 'P6', 'P8',
'PO7', 'PO3','POz', 'PO4','PO8', 'O1','Oz','O2', 'F9', 'F10', 'TP9', 'TP10'

The order of the 64 channels mentioned in subsequent files follows the same order as listed above.

### Preprocess Procedure
The EEG preprocessing procedures were as follows: First, the data were filtered to 0.1-47 Hz, downsampled to 200 Hz, and then segmented into trials. For imagery trials, we used the 30 seconds before the button press (or 30 seconds before the start of the rating if no button was pressed) for further analysis; for video trials, we selected the last 30 seconds of the video clip presentation for further analysis\cite{shen_contrastive_2023,hu_eeg_2017}. Next, we inspected bad channels based on two criteria. First, channels containing more than 30\% outliers were flagged, where outliers are defined as absolute values exceeding three times from the trial's median of absolute\cite{DECHEVEIGNE2018903}. Second, we identified channels with abnormal variance by plotting the variance for each channel across trials to detect significant variance jumps. Suspected bad channels were further verified through visual inspection of the EEG signals and were subsequently interpolated using the average of three neighboring channels. Then we performed Independent Component Analysis (ICA) and manually removed components derived from eye movements and muscle artifacts. Finally, common average referencing and trial reordering were applied. As the order of materials presentation was randomized across subjects, reordering of the trials ensured that the order of EEG data was the same for all subjects to facilitate subsequent analysis.

Our dataset also provides several commonly used EEG features, including differential entropy (DE) and power spectral density (PSD) features. DE and PSD features were extracted from the preprocessed data within each non-overlapping second at five frequency bands (delta band: 1-4 Hz, theta band: $4-8 \mathrm{~Hz}$, alpha band: $8-14 \mathrm{~Hz}$, beta band: $14-30 \mathrm{~Hz}$, and gamma band: $30-47 \mathrm{~Hz}$ ). The formula to calculate DE and PSD followed the practice in the SEED dataset :

$$
\begin{gathered}
P S D=E\left[x^2\right] \\
D E=\frac{1}{2} \ln \left(2 \pi e \sigma^2\right)
\end{gathered}
$$

where $x$ is the EEG signal filtered into a frequency band and $\sigma^2$ is the variance of the EEG signal.


### Guide for labels

- **Using Preprocessed Data**
If you prefer to work with preprocessed data, navigate to the following directories:
`\derivatives\sub-idx\ses-ima\eeg` or `\derivatives\sub-idx\ses-vid\eeg`.

Here, you will find:
- `_task-emotion_de.npy`
- `_task-emotion_psd.npy`
- `_task-emotion_reorder.npy`

These files have been preprocessed and reordered in the following sequence: **sad-dis-fear-neu-joy-ten-ins**. This means: 
- stimuli 1-3: sadness, stimuli 4-6: disgust, stimuli 7-9: fear, stimuli 10-12: neutral, stimuli 13-15: joy, stimuli 16-18: tenderness, stimuli 19-21: inspiration.

Each session (`ima` or `vid`) typically includes **21 trials**. For information on participants with missing trials, refer to the **Participants with Missing Trials** section above.

---

- **Preprocessing Data on Your Own**
If you'd like to preprocess the data yourself, follow these steps:

1. **Locate Raw Data**:
   - The raw EEG data is in the directory: `sub-idx\eeg\sub-idx_task-emotion_eeg.edf`.
   - Triggers are marked directly in the `.edf` file's notations.

2. **Map Triggers to Trial Types**:
   - Use the mapping information in `sub-idx\sub-idx_events` to link `stim_type` (triggers) with `trial_type`. This file also contains time of the triggers.

3. **Segment Data**:
   - Based on the trigger-trial mapping, segment the data accordingly.

4. **Reorder Trials**:
   - Use the sequence provided in the **Trial Reordering** section above to rearrange the trials in your preferred order.

This approach allows flexibility for custom analyses while ensuring alignment with the established trial order. You can also refer to our preprocess.py in /codes folder, especially the segementation part.
