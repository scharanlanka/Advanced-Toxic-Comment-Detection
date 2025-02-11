# Comment Toxicity Detection

## Overview

This project uses a TensorFlow model to detect the toxicity level of comments and classify them into six categories with confidence scores. The web app is built using Streamlit, which allows users to input comments and view predictions.

## Features

- Detects toxic comments based on six predefined categories.
- Provides confidence scores for each category.
- Streamlit-based web application for user interaction.
- Real-time analysis and classification of comments.

## Prerequisites

To run this project, ensure you have Python installed. You will also need to activate the virtual environment `.venv`.

### Activate the Virtual Environment

#### 1. Activate the virtual environment (Required dependencies are available in the virtual environment already):

For MacOS:
```bash
source .venv/bin/activate
```
For Windows:
```bash
.\venv\Scripts\activate
```
#### 2. Installing Dependencies:

Run the following command to install the necessary packages:
```bash
pip3 install -r requirements.txt
```

#### 3. Run the Web Application:
Open the terminal and ensure that the virtual environment is activated. Run the following command, and the web application will be running on a local server:

```bash
streamlit run app.py
```

#### 4. Enter a comment and press Ctrl+Enter to pass the comment to the model for analysis.

### Important info for dataset
One dataset required for this project is missing due to file upload size constraints. Anyone can download it from the following link:

[Download Dataset](https://www.kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge/data)
