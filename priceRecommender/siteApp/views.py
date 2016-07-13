# coding=utf-8
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core import validators
import django.forms.utils

from .forms import AirbnbRequestForm

##Datasciense imports , remove when moving the method
import pandas as pd
from sklearn.externals import joblib
from geopy import geocoders
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from geopy.distance import vincenty #distance of two points on an oblate spheroid
import cPickle as pickle
##

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = AirbnbRequestForm(request.POST)
        if form.is_valid():
            form.latitude, form.longitude = helperTransformationGPS(form.data['street'],form.data['number'])
            if secondValidation(form):
                form.amenities = helperTransformation(request.POST['valuesAmenities'])
                form.verificationUser = helperTransformation(request.POST['valuesVerifications'])
                form.apartmentDeposit = request.POST['valueApartamentDeposit']
                form.hostAbout = request.POST['valuehostAbout']
                form.hostIdentityVerified = request.POST['valuehostIdentityVerified']
                form.extraPeople = request.POST['valueExtraPeople']
                form.postalCode = helperTranformationPostalCode(form.data['street'],form.data['number'])
                #form.save()
                price = processData(form)
                outputPrice ="{0:.2f}".format(price[0])
                return render(request, 'siteApp/results.html', {'name': form.data['name'],'price':outputPrice})
                #return HttpResponseRedirect("GoodJobBoy you price is!",price,"yay!")
        return render(request, 'siteApp/index.html', {'form': form})
    else:
        form = AirbnbRequestForm()
        return render(request, 'siteApp/index.html', {'form': form})


#TODO move to another file
def processData(formRequest):
    optimized_GBM = joblib.load('siteApp/pklObjects/ObjectEncoded.pkl')
    return optimized_GBM.predict(createVectorCaracteristicsNewUser(formRequest))

#Step1_Format_raw_data.ipynb

#TODO
# Helpers

def helperTransformation(inputString):
    output = []
    for item in inputString.split(","):
        if item != "":
            itemLen = len(item)
            output.append(item[1:itemLen-1])
    return output

def secondValidation(form):
    #Remove when we fix the latitude thing
    if form.latitude == 0 or form.longitude == 0 or not checkLatitudeLong(form.latitude,form.longitude):
        errors = form._errors.setdefault("street")#, ErrorList())
        #errors.append(u"Wrong Combination or not from BCN")
        return False
    # if form.latitude == 0 or form.longitude == 0:
    #     errors = form._errors.setdefault("street")#, ErrorList())
    #     errors.append(u"Wrong Combination or not from BCN")
    #     return False
    return True


def helperTransformationGPS(street, number):
    return get_coordinates(street+" "+number+",Barcelona")

def helperTranformationPostalCode(street, number):
    result = get_geocode_location(street+" "+number+",Barcelona")
    if result is None:
        return ""
    digits = []
    for s in result.address.split(","):
        if s.replace(" ","").isdigit():
            digits.append(s)
    if len(digits)==1:
        return digits[0]
    if len(digits)>0:
        return digits[1]
    return ""

#TODO helpers to move

def createVectorCaracteristicsNewUser(form):
    pandasMatrix = pd.read_json(createJSONString(form),typ='series',orient='records')
    wrong = pandasMatrix.to_frame()
    final = wrong.transpose()
    return final

def createJSONString(form):

    x = "\"zipcode\":{0},\"latitude\":{1},\"longitude\":{2},\"host_about\":{3}," \
        "\"host_listings_count\":{4},\"host_identity_verified\":{5},\"availability_30\":{6},\"availability_60\":{7},\"availability_90\":{8}," \
        "\"availability_365\":{9},\"cancellation_policy\":{10},\"bathrooms\":{11},\"bedrooms\":{12},\"beds\":{13}," \
        "\"accommodates\":{14},\"guests_included\":{15},\"extra_people\":{16},\"security_deposit\":{17}"

    stringAmenities = "tv,internet,kitchen,ac,smoking,hottub,heating,family,events,dryer,smoke,shampoo,elevator,washer,intercom,essentials,lock,24hourcheckin,hangers,laptopf,hairdryer,iron,firstaidkit,cabletv,fireplace,extinguisher,breakfast,pets,petsallowed,parking,safetycard,doorman,wheelchair,carbondetector,gym,washerdryer,pool"
    stringVerifications ="verified_email,verified_phone,verified_facebook,verified_linkedin,verified_google,verified_jumio,verified_reviews,verified_manual"
    stringNeighborhoods = "baro_de_viver,can_baro,can_peguera,canyelles,ciutat_meridiana,diagonal_mar_i_el_front_maritim_del_poblenou,horta,hostafrancs,montbau,navas,pedralbes,porta,provencals_del_poblenou,sant_andreu,sant_antoni,sant_genis_dels_agudells,sant_gervasi_-_galvany,sant_gervasi_-_la_bonanova,sant_marti_de_provencals,sant_pere,sants,sants_-_badal,sarria,torre_baro,vallcarca_i_els_penitents,vallvidrera,verdun,vilapicina_i_la_torre_llobeta,el_baix_guinardo,el_barri_gotic,el_besos_i_el_maresme,el_bon_pastor,el_camp_d_en_grassot_i_gracia_nova,el_camp_de_l_arpa_del_clot,el_carmel,el_clot,el_coll,el_congres_i_els_indians,el_fort_pienc,el_guinardo,el_parc_i_la_llacuna_del_poblenou,el_poble_sec,el_poblenou,el_putxet_i_el_farro,el_raval,el_turo_de_la_peira,l_antiga_esquerra_de_l_eixample,la_barceloneta,la_bordeta,la_clota,la_dreta_de_l_eixample,la_font_d_en_fargues,la_font_de_la_guatlla,la_guineueta,la_marina_de_port,la_marina_del_prat_vermell,la_maternitat_i_sant_ramon,la_nova_esquerra_de_l_eixample,la_prosperitat,la_sagrada_familia,la_sagrera,la_salut,la_teixonera,la_trinitat_nova,la_trinitat_vella,la_vall_d_hebron,la_verneda_i_la_pau,la_vila_olimpica_del_poblenou,la_vila_de_gracia,les_corts,les_roquetes,les_tres_torres"
    stringtypeApp = "apartment,bed_&_breakfast,boat,bungalow,cabin,camper_rv,chalet,condominium,dorm,house,loft,other,tent,townhouse,villa,yurt"
    stringEntireAp = "entire_home_apt,private_room,shared_room"
    stringTypeBed = "airbed,couch,futon,pull-out_sofa,real_bed"

    x = x.format(form.postalCode, form.latitude, form.longitude, form.hostAbout,
                 form.data['hostListingsCount'], form.hostIdentityVerified, form.data['availability30'], form.data['availability60'], form.data['availability90'],
                 form.data['availability365'], form.data['cancellationPolicy'], form.data['bathrooms'], form.data['bedrooms'], form.data['beds'],
                 form.data['accomodates'], form.data['guestsIncluded'], form.extraPeople, form.apartmentDeposit)

    xAmenities = pseudoOneHotEncodingJSONAmenities(stringAmenities,form.amenities)
    xVerification = pseudoOneHotEncodingJSONVerifications(stringVerifications,form.verificationUser)
    xNeighborhoods = pseudoOneHotEncodingJSON(stringNeighborhoods,(int(form.data['neighborhood'])-1))
    xAppType = pseudoOneHotEncodingJSON(stringtypeApp,(int(form.data['apartamentType'])-1))
    xEntireApp = pseudoOneHotEncodingJSON(stringEntireAp,(int(form.data['typeOfRoom'])-1))
    xTypeBed = pseudoOneHotEncodingJSON(stringTypeBed,(int(form.data['typeOfBed'])-1))
    output = "{" + x + "," + xAmenities + "," + xVerification + "," + xNeighborhoods + "," + xAppType + "," + xEntireApp + "," + xTypeBed + "}"
    return output

##WARNING CHECK THAT WE USE THE SAME LIST FOR THE DISPLAY WITH THE EXACT SAME ORDER !!!
def pseudoOneHotEncodingJSON(listItems, number):
    count = 0
    out = ""
    splitString = listItems.split(',')
    for item in splitString:
        aux = "\"{0}\":{1}".format(item, 1) if count == number else "\"{0}\":{1}".format(item, 0)
        out += aux
        count += 1
        if count < len(splitString):
            out += ","
    return out

def pseudoOneHotEncodingJSONVerifications(stringVerifications,verifications):
    count = 0
    out = ""
    aux = ""
    splitString = stringVerifications.split(',')
    if len(verifications) == 0:
        for item in splitString:
            aux ="\"{0}\":{1}".format(item, 0)
            out += aux
            count += 1
            if count < len(splitString):
                out += ","
    else:
        for item in splitString:
            for v in verifications:
                if ("verified_" + v.lower() == item):
                    aux = "\"{0}\":{1}".format(item, 1)
                    break;
                else:
                    aux ="\"{0}\":{1}".format(item, 0)
            out += aux
            count += 1
            if count < len(splitString):
                out += ","
    return out

def pseudoOneHotEncodingJSONAmenities(stringAmenities,amenities):
    count = 0
    out = ""
    aux = ""
    splitString = stringAmenities.split(',')
    if (len(amenities) == 0):
        for item in splitString:
            aux ="\"{0}\":{1}".format(item, 0)
            out += aux
            count += 1
            if count < len(splitString):
                out += ","
    else:
        for item in splitString:
            for a in amenities:
                if (parseStringAm(a) == item):
                    aux = "\"{0}\":{1}".format(item, 1)
                    break;
                else:
                    aux ="\"{0}\":{1}".format(item, 0)
            out += aux
            count += 1
            if count < len(splitString):
                out += ","
    return out

def parseStringAm(a):
    a = a.lower()
    a = a.replace(" ","")
    a = a.replace("/","")
    if a == 'wirelessInternet':
        return 'internet'
    if a == 'airconditioning':
        return 'ac'
    if a == 'smokingallowed':
        return 'smoking'
    if a == 'familykidfriendly':
        return 'family'
    if a == 'suitableforevents':
        return 'events'
    if a == 'smokedetector':
        return 'smoke'
    if a == 'elevatorinbuilding':
        return 'elevator'
    if a == 'buzzerwirelessintercom':
        return 'intercom'
    if a == 'lockonbedroomdoor':
        return 'lock'
    if a == '24-hourcheck-in':
        return '24hourcheckin'
    if a == 'laptopfriendlyworkspace':
        return 'laptopf'
    if a == 'indoorfireplace':
        return 'fireplace'
    if a == 'fireextinguisher':
        return 'extinguisher'
    if a == 'petsliveonthisproperty' or a == 'otherpet(s)' or a == 'dog(s)' or a == 'cat(s)':
        return 'pets'
    if a == 'freeparkingonpremises':
        return 'parking'
    if a == 'wheelchairaccessible':
        return 'wheelchair'
    if a == 'carbonmonoxidedetector':
        return 'wheelchair'
    return a

def get_coordinates(address_string):
    '''This function finds the latitude and longitude given an address string.
    If no address is found returs 0,0 (location in the ocean)
    It does not privide more than one result'''
    location = get_geocode_location(address_string)
    if location is None:
        return 0,0
    else:
        return location.latitude,location.longitude

def get_geocode_location(address_string):
    g = geocoders.Nominatim()
    try:
        return g.geocode(address_string, timeout=10,exactly_one=True)
    except:
        return None

def find_mydistance(lat,lng,data,neighbors_number=25):
    '''This function finds the first neighbors to a point given a set of coordinates from a file.
        It calclutates the distance from the chosen point to all the neighbors,
        and returns the median distance to the neighbors'''
    neigh = NearestNeighbors(n_neighbors=neighbors_number, metric='euclidean', n_jobs=-1)
    neigh.fit(data.loc[:,('latitude','longitude')])
    my_coordinates=np.array([lat, lng])
    my_neighbors=neigh.kneighbors(my_coordinates.reshape(1, -1),neighbors_number, return_distance=False)
    d_meters=np.zeros(neighbors_number)
    counter=0
    for i in my_neighbors[0,:]:
        lat_long_neigh=np.array([data.iloc[i].latitude, data.iloc[i].longitude])
        d_meters[counter]=vincenty(my_coordinates,lat_long_neigh).meters
        counter=counter+1
    return np.median(d_meters)

def check_mypos(mydistance, control_parameter):
    '''This function checks if the distance of the point is within the chose accaptance range,
    and returns a boolean value'''
    return mydistance<control_parameter

def checkLatitudeLong(latitude, longitude):
    data=pd.read_csv("siteApp/pklObjects/step2_output.csv", sep=";")
    central_lat=np.mean(data.loc[:,('latitude')].values)
    central_long=np.mean(data.loc[:,('longitude')].values)
    control_parameter=pickle.load(open("siteApp\pklObjects\save_control.p", "rb"))
    return  check_mypos(find_mydistance(latitude,longitude,data),control_parameter)
#TODO
