from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core import validators

from .models import AirbnbRequest, Amenities
from .forms import AirbnbRequestForm

##Datasciense imports , remove when moving the method
import profile
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.externals import joblib
##

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = AirbnbRequestForm(request.POST)
        if form.is_valid() and secondValidation(form):
            form.Amenities = helperAmenitiesTransformation(request.POST['valuesAmenities'])
            form.save()
            price = processData(form)
            return HttpResponseRedirect("GoodJobBoy you price is!",price,"yay!")
        else:
            return render(request, 'siteApp/index.html', {'form': form})
    else:
        form = AirbnbRequestForm()
        return render(request, 'siteApp/index.html', {'form': form})


#TODO move to another file
def processData(formRequest):
    # cv_params = {'max_depth': [3,5], 'min_child_weight': [3]}
    # ind_params = {'learning_rate': 0.1, 'n_estimators': 1000, 'subsample': 0.8, 'seed': 0, 'silent': 1 ,'colsample_bytree': 0.8,'objective': 'reg:linear'}
    # optimized_GBM = GridSearchCV(xgb.XGBClassifier(**ind_params),cv_params,scoring = 'accuracy', cv = 2, n_jobs = -1, verbose=0)
    # optimized_GBM.fit(X_train, y_train)

    optimized_GBM = joblib.load('pklObjects/filename.pkl')
    return optimized_GBM.predict(createVectorCaracteristics(formRequest))


def createVectorCaracteristics(form):
    pandasMatrix = pd.Series()
    return pandasMatrix

#TODO
# Helpers

def helperAmenitiesTransformation(inputString):
    amenities = []
    for item in inputString.split(","):
        if item != "":
            itemLen = len(item)
            amenities.append(item[1:itemLen-1])
    return amenities

def secondValidation(form):
    # use this function to test the latitude longitude and other params
    return False