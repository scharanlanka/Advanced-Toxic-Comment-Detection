# Comment Toxicity Detection

This project uses a TensorFlow model to detect the toxicity level of comments and classify them into six categories with confidence scores. The web app is built using Streamlit, which allows users to input comments and view predictions. 

## Prerequisites

To run this project, ensure you have Python installed. You will also need to activate the virtual environment '.venv'.

### Activate the Virtual Environment

#### 1. Activate the virtual environment(Required dependencies are available in Virtual Enivronment Already):
     For MacOS:
      source .venv/bin/activate

    For Windows:
     .\venv\Scripts\activate

#### 2. Installing Dependencies:
     Run the following command to install the necessary packages:
      pip3 install -r requirements.txt

#### 3. Run the web application:
     Open the terminal and ensure that virtual environment is activated. Run the following command and the web application will be running in local server:
      streamlit run app.py

#### 4. Enter the comment and press ctrl+Enter to get the comment passed to the model.