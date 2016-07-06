from django import forms


#class NameForm(forms.Form):
#    your_name = forms.CharField(label='Your name', max_length=100)



class AirbnbRequestForm(forms.Form):
    name = forms.CharField(max_length=200)

    latitude = forms.CharField(max_length=20)
    longitude = forms.CharField(max_length=20)

    accomodates = forms.IntegerField()
    bathrooms = forms.IntegerField()
    bedrooms = forms.IntegerField()
    beds = forms.IntegerField()
    guestsIncluded = forms.IntegerField()
    entireApartament = forms.BooleanField(required=False)


    #selectors
    neighborhood = forms.ChoiceField([('1','nono'), ('2','nip'),('3','patata')])
    cancellationPolicy = forms.IntegerField()
    #TODO search for the asciicode for the ny and the ampersand
    apartamentType = forms.ChoiceField([('0','Selecciona'),('1','Apartamento'),('2','Casa'),('3','Bed and Breakfast'),('4','Adosado'),('5','Autocaravana'),('6','Barco'),('7','Bungalow'),('8','Cabana'),('9','Chalet'),('10','Dormitorio compartido'),('11','Loft'),('12','Tienda de campana'),('13','Villa'),('14','Otros')])
    typeOfRoom = forms.IntegerField()
    typeOfBed = forms.IntegerField()
    Amenities = []

    #not in the form items
    pub_date = forms.DateTimeField('date published', required=False)
    finalRecomendedPrice = forms.DecimalField(decimal_places=2, max_digits=8, required=False)


class Amenities(forms.Form):
    name = forms.CharField(max_length=200)

