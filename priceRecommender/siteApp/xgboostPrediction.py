__author__ = 'hiro'
from .forms import AirbnbRequestForm

import profile
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.externals import joblib

class SiteappPythonBack():
    #optimized_GBM = joblib.load('pklObjects/filename.pkl')
    optimized_GBM = " sdsd"

    def getPrediction(self, formObject):
        #return optimized_GBM.predict(formObject.name,)
        # TODO create the matrix for the predict with the formobject
        return 1;