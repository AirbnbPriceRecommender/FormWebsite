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
    entireApartament = forms.BooleanField()


    #selectors
    neighborhood = forms.ChoiceField([('1','nono'), ('2','nip'),('3','patata')])
    cancellationPolicy = forms.IntegerField()
    apartamentType = forms.IntegerField()
    typeOfRoom = forms.IntegerField()
    typeOfBed = forms.IntegerField()

    #not in the form items
    pub_date = forms.DateTimeField('date published')
    finalRecomendedPrice = forms.DecimalField(decimal_places=2, max_digits=8)


class Amenities(forms.Form):
    name = forms.CharField(max_length=200)

