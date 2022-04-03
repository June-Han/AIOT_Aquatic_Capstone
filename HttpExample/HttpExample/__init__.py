import logging
import azure.functions as func

# Imports for image processing
import io
from PIL import Image
from flask import Flask, jsonify

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
            jsonStr = jsonresult.get_data(as_text = True)
            results = jsonStr
    except Exception as e:
        logging.info(f'exception: {e}')
        pass

    #return results
    logging.info('Image processed. Results: ' + results)
    return func.HttpResponse(results, status_code=200)

    '''
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    '''
