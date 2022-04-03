import logging

import azure.functions as func

from flask import *
import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials


prediction_key = "db7ae6091080465a8023ec56ac393bbf"
publish_iteration_name = "classifyModel"
ENDPOINT = "https://cognitives-test.cognitiveservices.azure.com/"
projectId = "b1de6f29-5ec0-49c3-9abf-62adcd8b4f8b"

def main(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes \n"
                 f"Blob uri: {myblob.uri}")
'''
    prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
    predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

    with open(myblob.uri, "rb") as image_contents:
        results = predictor.classify_image(
                projectId, publish_iteration_name, image_contents.read())
        result=""
        for prediction in results.predictions:
            result += "\t\t\n" + prediction.tag_name + " : {0:.2f}% ".format(prediction.probability * 100)
        logging.info(f"Results: {result}")
'''