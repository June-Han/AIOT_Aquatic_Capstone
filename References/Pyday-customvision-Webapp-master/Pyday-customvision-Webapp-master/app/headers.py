from flask import *
import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from app import app



prediction_key = "db7ae6091080465a8023ec56ac393bbf"
publish_iteration_name = "classifyModel"
ENDPOINT = "https://cognitives-test.cognitiveservices.azure.com/"
projectId = "b1de6f29-5ec0-49c3-9abf-62adcd8b4f8b"
# prediction_key = "your-prediction key"
# publish_iteration_name = "classifyModel"
# ENDPOINT = "your-endpoint"
# projectId = "your project id"
