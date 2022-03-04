from fnmatch import translate
import re
import requests, os, uuid, json
from dotenv import load_dotenv 
from flask import Flask, redirect, url_for, request, render_template, session
'''
# Windows
# Create the environment
python3 -m venv venv
# Activate the environment
.\venv\scripts\activate

# macOS or Linux
# Create the environment
python3 -m venv venv
# Activate the environment
source ./venv/bin/activate
'''
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    # Read the values from the form
    original_text = request.form['text']
    target_language = request.form['language']

    # Load the values from .env
    key = os.environ['KEY']
    endpoint = os.environ['ENDPOINT']
    location = os.environ['LOCATION']

    # Indicate that we want to translate and the API version (3.0) and the target language
    path = '/translate?api-version=3.0'
    # Add the target language parameter
    target_language_parameter = '&to=' + target_language
    # Create the full URL
    constructed_url = endpoint + path + target_language_parameter

    # Set up the header information, which includes subscription key
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # Create the body of the request with the text to be translated
    body = [{'text': original_text}]

    #Make the call using post
    translator_request = requests.post(constructed_url, headers=headers, json=body)
    #Retrieve the JSON response
    translator_response = translator_request.json()
    '''
    ##translator_response format:

    [
        {
            "detectedLanguage": {
                "language": "en",
                "score": 1.0
            },
            "translations": [
                {
                    "text": "これはテストです",
                    "to": "ja"
                }
            ]
        }
    ]
    '''
    #Retrieve the translation
    translated_text = translator_response[0]['translations'][0]['text']

    #Call render template, passing the translated text, original text 
    #and target language to the template
    return render_template(
        'results.html',
        translated_text=translated_text,
        original_text=original_text,
        target_language=target_language
    )

    '''
    For results page:
    Access original_text, translated_text, and target_language, which we 
    passed as named parameters in render_template by using {{ }}. This operation 
    tells Flask to render the contents as plain text. We're also using url_for('index') 
    to create a link back to the default page. While we could, technically, type 
    in the path to the original page, using url_for tells Flask to read the path for 
    the function with the name we provide (index in this case). If we rearrange our 
    site, the URL generated for the link will always be valid.
    '''
