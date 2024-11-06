# EmoEEG-MC: A Multi-Context Emotional EEG Dataset for Cross-Context Emotion Decoding

## Abstract

EEG-basedemotion decoding is essential for unveiling neural mechanisms underlying emotion and enabling artificial intelligence to understand human emotions. However, existing datasets for EEG-based emotion decoding are limited to a single context of emotion elicitation. The ability of emotion decoding methods to generalize across different contexts remains underexplored. To address this gap, we present the **Multi-Context Emotional EEG (EmoEEG-MC)** dataset, featuring 64-channel EEG and peripheral physiological data from 60 participants exposed to two distinct contexts: video-induced and imagery-induced emotions. These contexts evoke seven distinct emotional categories: joy, inspiration, tenderness, fear, disgust, sadness, and neutral emotion. The emotional experience of specific emotion categories was validated through subjective reports. Using support vector machines with L1 regularization, we achieved cross-context emotion decoding accuracies of 66.7% for binary classification (positive vs. negative emotions) and 28.9% for seven-category emotion classification, both significantly above chance levels. The EmoEEG-MC dataset serves as a foundational resource for understanding the neural mechanisms underlying emotional processing and enhancing the real-world applicability of affective computing systems.

## Introduction
<img src=".\fima\2.png" alt="framework" style="zoom:50%;" />

**Experimental procedures and the experimental setup.** (a) The block-design experimental protocol. (b) Video trial & imagery trial. (c) The 64-channel EEG acquisition system (g.HIamp, g.tec Medical Engineering), the wristband for PPG and GSR signal collection (Psychorus, HuiXin), and the experimental environment.
This repository contains codes for preprocessing and stimuli material embeddings. You can find the dataset via **OpenNeuro**(doi:10.18112/openneuro.ds005540.v1.0.3) or **ScienceDB**(10.57760/sciencedb.14025).

<img src=".\fima\t1.png" alt="framework" style="zoom:50%;" />

**The summary of key features of the EmoEEG-MC dataset.**

## Method
The EEG preprocessing procedures were as follows: First, the data were filtered to $0.1-47 \mathrm{~Hz}$, downsampled to 200 Hz , and then segmented into trials. For imagery trials, we used the 30 seconds before the button press (or 30 seconds before the start of the rating if no button was pressed) for further analysis; for video trials, we selected the last 30 seconds of the video clip presentation for further analysis . Next, we inspected bad channels based on two criteria. First, channels containing more than $30 \%$ outliers were flagged, where outliers are defined as absolute values exceeding three times from the trial's median of absolute. Second, we identified channels with abnormal variance by plotting the variance for each channel across trials to detect significant variance jumps. Suspected bad channels were further verified through visual inspection of the EEG signals and were subsequently interpolated using the average of three neighboring channels. Then we performed Independent Component Analysis (ICA) and manually removed components derived from eye movements and muscle artifacts. Finally, common average referencing and trial reordering were applied. As the order of materials presentation was randomized across subjects, reordering of the trials ensured that the order of EEG data was the same for all subjects to facilitate subsequent analysis.

Our dataset also provides several commonly used EEG features, including differential entropy (DE) and power spectral density (PSD) features. DE and PSD features were extracted from the preprocessed data within each non-overlapping second at five frequency bands (delta band: 1-4 Hz, theta band: $4-8 \mathrm{~Hz}$, alpha band: $8-14 \mathrm{~Hz}$, beta band: $14-30 \mathrm{~Hz}$, and gamma band: $30-47 \mathrm{~Hz}$ ). The formula to calculate DE and PSD followed the practice in the SEED dataset :

$$
\begin{gathered}
P S D=E\left[x^2\right] \\
D E=\frac{1}{2} \ln \left(2 \pi e \sigma^2\right)
\end{gathered}
$$

where $x$ is the EEG signal filtered into a frequency band and $\sigma^2$ is the variance of the EEG signal.

## Participants' Behaviour Reports
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

## Channels
The EEG channels follow the 10-20 system with 64 channels, and the channel names are as follows:

'Fp1', 'Fpz', 'Fp2', 'AF7', 'AF3','AF4','AF8', 'F7', 'F5','F3','F1','Fz', 'F2', 'F4', 'F6', 'F8', 'FT7', 'FC5', 'FC3', 'FC1','FCz','FC2','FC4', 'FC6', 'FT8', 'T7','C5', 'C3', 'C1', 'Cz', 'C2', 'C4', 'C6', 'T8', 'TP7', 'CP5', 'CP3', 'CP1','CPz','CP2', 'CP4','CP6', 'TP8', 'P7','P5', 'P3', 'P1', 'Pz','P2', 'P4', 'P6', 'P8', 'PO7', 'PO3','POz', 'PO4','PO8', 'O1','Oz','O2', 'F9', 'F10', 'TP9', 'TP10'

The order of the 64 channels mentioned in subsequent files follows the same order as listed above.
