
import pandas as pd

from joblib import load
pipeline = load("text_classification.joblib")

def output(sentence):
  text=[sentence]
  re=pipeline.predict(text)
  return re


print(output("oppo acha ha"))
