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

**Experiment Procedure**
During the experiment, participants were seated approximately 160 cm away from a 43 -inch monitor (Konka, China). The experiment involved two distinct emotion-induction contexts: video-induced emotion context and imagery-induced emotion context. The video context used external visual and auditory stimuli, and the imagery context relied on guided narratives and internal imagery to evoke emotion. This setup provided a good testbed for cross-context comparison of EEG representations. Each context comprised seven blocks, with a total of fourteen blocks. From the start of the experiment, each consecutive two blocks included a video block and an imagery block, with the order of the two blocks randomized. Each block consisted of three imagery trials or three video trials. The materials in one block were randomly selected from those with the same valence to minimize the potential influence of alternating valence, and they were presented in a random order. Between two blocks, participants were asked to solve 20 arithmetic problems to attenuate their previous emotional experience.

Each imagery block began with an instruction to guide participants to close their eyes and relax. After that, participants would listen to the guided narratives for emotion induction, where they were asked to imagine the described scene and immerse themselves in the emotional state. There were 30 seconds for the imagery process, but if participants felt the emotion dissipate before the time was up, they could press a button to end the imagination early. Subsequently, participants completed subjective ratings including items of six discrete emotions and four affective dimensions, the same as those in the Stimuli Selection section. After completing the ratings, a "washout" audio was played, prompting participants to relax before starting the next trial.

In the video trials, following a five-second fixation with a white cross in the center of a black screen, the video clip is displayed. After watching the video, participants made the same subjective report as that in the imagery part. A landscape picture was shown for 30 seconds between trials to help participants relax. The experimental program was implemented in Python using the Pygame framework.

Two sessions of resting-state EEG data were collected: a session of four minutes before the experiment and another of four minutes after all trials were completed. The first two minutes of each session were recorded with eyes open and the last two minutes with eyes closed. To prevent excessive fatigue among the participants, they were given a break after the seventh block was completed. During this break, participants were allowed to rest for any duration while wearing the EEG cap and wristwatch. Most participants chose to rest for 15 minutes.

**EEG Signal Preprocessing**
The EEG preprocessing procedures were as follows: First, the data were filtered to $0.1-47 \mathrm{~Hz}$, downsampled to 200 Hz , and then segmented into trials. For imagery trials, we used the 30 seconds before the button press (or 30 seconds before the start of the rating if no button was pressed) for further analysis; for video trials, we selected the last 30 seconds of the video clip presentation for further analysis . Next, we inspected bad channels based on two criteria. First, channels containing more than $30 \%$ outliers were flagged, where outliers are defined as absolute values exceeding three times from the trial's median of absolute. Second, we identified channels with abnormal variance by plotting the variance for each channel across trials to detect significant variance jumps. Suspected bad channels were further verified through visual inspection of the EEG signals and were subsequently interpolated using the average of three neighboring channels. Then we performed Independent Component Analysis (ICA) and manually removed components derived from eye movements and muscle artifacts. Finally, common average referencing and trial reordering were applied. As the order of materials presentation was randomized across subjects, reordering of the trials ensured that the order of EEG data was the same for all subjects to facilitate subsequent analysis.

Our dataset also provides several commonly used EEG features, including differential entropy (DE) and power spectral density (PSD) features. DE and PSD features were extracted from the preprocessed data within each non-overlapping second at five frequency bands (delta band: 1-4 Hz, theta band: $4-8 \mathrm{~Hz}$, alpha band: $8-14 \mathrm{~Hz}$, beta band: $14-30 \mathrm{~Hz}$, and gamma band: $30-47 \mathrm{~Hz}$ ). The formula to calculate DE and PSD followed the practice in the SEED dataset :

$$
\begin{gathered}
P S D=E\left[x^2\right] \\
D E=\frac{1}{2} \ln \left(2 \pi e \sigma^2\right)
\end{gathered}
$$

where $x$ is the EEG signal filtered into a frequency band and $\sigma^2$ is the variance of the EEG signal.

**Stimuli Embedding**
The stimulus-related materials are stored in the stimuli folder of the EmoEEG-MC dataset. In the stimuli/ses-ima folder, the imagery_guidance.xlsx file contains the text of imagery guidance. The stimuli/ses-vid folder includes the video_description.xlsx file, providing descriptions of the video content, as well as embedding files (e.g., video_01_embedding.mat), providing embeddings extracted by vision Transformer from the video frames and the audio. The video frames were rescaled to a size of $112^* 112$, segmented into 16*16 patches, and fed into a pretrained vision Transformer. 128 Mel Filterbank features were extracted from the audio and fed into a base-scale Data-efficient Image Transformer (DeiT). Visual and audio embeddings were both of 768 dimensions. The embeddings were averaged within each second.

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
