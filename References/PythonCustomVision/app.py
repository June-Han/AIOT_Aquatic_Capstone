from fnmatch import translate
import re
import requests, os, uuid, json
from dotenv import load_dotenv 
from flask import Flask, redirect, url_for, request, render_template, session

#https://medium.com/@syed.sohaib/creating-a-classifier-using-custom-vision-api-and-consuming-it-in-a-flask-application-2ba580fd32e7

load_dotenv()

app = Flask(__name__)


