import logging
import azure.functions as func

# Imports for image processing
import io
from PIL import Image
from flask import Flask, jsonify

import json

#Imports for prediction
from .predict import _initialize, _predict_image

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    results = "{}"
    try:
        #get and load image from POST
        image_bytes = req.get_body()
        image = Image.open(io.BytesIO(image_bytes))

        #Load and initialize the model and the app context
        app = Flask(__name__)
        _initialize()

        with app.app_context():
            #predict image and process results in json string format
            results = _predict_image(image)
            jsonresult = jsonify(results)
            #jsonStr = jsonresult.get_data(as_text = True)
            jsonStr = jsonresult.get_json()
            results = jsonStr
        '''
        # returns UnboundLocalError: local variable 'my_headers' referenced before assignment
        #Assigned directly inside the httpresponse
        my_headers = {
                "Content-type": "application/json",
                "Access-Control-Allow-Origin": "*"
        }
        '''
        
    except Exception as e:
        logging.info(f'exception: {e}')
        pass


    #return results
    #logging.info('Image processed. Results: ' + results)
    return func.HttpResponse(json.dumps(results), headers = {
                "Content-type": "application/json",
                "Access-Control-Allow-Origin": "*"
        }, status_code=200)
