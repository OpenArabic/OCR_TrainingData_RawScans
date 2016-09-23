# OCR_TrainingData

Training data for various Arabographic typesets to be used with [Kraken](http://kraken.re/) and [Nidaba](https://openphilology.github.io/nidaba/), which are being developed at Alexander von Humboldt Chair for DH, U Leipzig.

## Typesets

1. Arabic
	1. Bayrūt: ʿĀlam al-kutub (`bayrut_calam_kutub`), modern typeset for classical Arabic
	2.  ...
	3.  ...
2. Persian
	1. ...
	2. ...
	3. ...
3. Perso-Arabic
	1. ...
	2. ...
	3. ...

## Folder Structure

1. Folders `place_piblisher_X` are to be renamed accordingly
2. Scanned images into `1_images`
3. Images prepared for running OCR to be put into `2_preprocessed_images`
4. Transcription-ready images/html files are to be put to `3_transcription_ready`
5. Finished training data to be put into `4_training_data`

**NB:** Currently, there are folders for Arabic, Persian and Perso-Arabic. Folders for other Islamicate languages can be added as needed.

```
.
├── ara
│   ├── bayrut_calam_kutub
│   │   ├── 1_images
│   │   ├── 2_preprocessed_images
│   │   ├── 3_transcription_ready
│   │   └── 4_training_data
│   ├── place_publisher_1
│   │   ├── 1_images
│   │   ├── 2_preprocessed_images
│   │   ├── 3_transcription_ready
│   │   └── 4_training_data
│   ├── place_publisher_2
│   │   ├── 1_images
│   │   ├── 2_preprocessed_images
│   │   ├── 3_transcription_ready
│   │   └── 4_training_data
│   └── place_publisher_3
│       ├── 1_images
│       ├── 2_preprocessed_images
│       ├── 3_transcription_ready
│       └── 4_training_data
├── per
│   ├── place_publisher_1
│   │   ├── 1_images
│   │   ├── 2_preprocessed_images
│   │   ├── 3_transcription_ready
│   │   └── 4_training_data
│   ├── place_publisher_2
│   │   ├── 1_images
│   │   ├── 2_preprocessed_images
│   │   ├── 3_transcription_ready
│   │   └── 4_training_data
│   └── place_publisher_3
│       ├── 1_images
│       ├── 2_preprocessed_images
│       ├── 3_transcription_ready
│       └── 4_training_data
├── per-ara
│   ├── place_publisher_1
│   │   ├── 1_images
│   │   ├── 2_preprocessed_images
│   │   ├── 3_transcription_ready
│   │   └── 4_training_data
│   ├── place_publisher_2
│   │   ├── 1_images
│   │   ├── 2_preprocessed_images
│   │   ├── 3_transcription_ready
│   │   └── 4_training_data
│   └── place_publisher_3
│       ├── 1_images
│       ├── 2_preprocessed_images
│       ├── 3_transcription_ready
│       └── 4_training_data
 
```



