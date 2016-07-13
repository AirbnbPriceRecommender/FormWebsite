# coding=utf-8
from django import forms


class AirbnbRequestForm(forms.Form):
    #SelectorsValues
    apartmentValues = [('','Select'),('1','Apartment'),('2','House'),('3','Bed and Breakfast'),('4','Townhouse'),('5','Mobile Home'),('6','Ship'),('7','Bungalow'),('8','Cottage'),('9','Chalet'),('10','Shared Bedroom'),('11','Loft'),('12','Tent'),('13','Town'),('14','Others')]
    neighborhoodsValues = [('','Select'),('1','Eixample'),('2','Ciutat Vella'),('3','Sants-Montjuic'),('4','Camp d\'en  Grassot i Gracia Nova'),('5','Can Baro'),('6','Diagonal Mar - La Mar Bella'),('7','Carmel'),('8','Dreta de l\'Eixample'),('9','El Baix Guinardó'),('10','El Besòs i el Maresme'),('11','El Born'),('12','El Camp de l\'Arpa del Clot'),('13','El Clot'),('14','El Coll '),('15','El Congres i els Indians'),('16','El Gótic'),('17','El Poble-Sec'),('18','El Poblenou'),('19','El Putget i Farró'),('20','El Raval'),('21','Glòries -El Parc'),('22','Gràcia'),('23','Guinardó'),('24','Horta'),('25','Horta-Guinardó'),('26','L\'Antiga Esquerra de l\'Eixample'),('27','La Barcelonet'),('28','La Font d\'en Fargues'),('29','La Maternitat i Sant Ramon'),('30','La Nova Esquerra de l\'Eixample'),('31','La Prosperitat'),('32','La Sagrada Familia'),('33','La Sagrera'),('34','La Salud'),('35','La Vall d\'Hebron'),('36','La Verneda i La Pau'),('37','La Vila Olímpica'),('38','Les Corts'),('39','Les Tres Torres'),('40','Navas'),('41','Nou Barris'),('42','Pedralbes'),('43','Porta'),('44','Provençals del Poblenou'),('45','Sant Andreu'),('46','San Andrés de Palomar'),('47','Sant Antoni'),('48','Sant Gervasi - Galvany'),('49','Sant Gervasi - La Bonanova'),('50','Sant Martí'),('51','San Martín de Provensals'),('52','Sant Pere/ Santa Caterina'),('53','Sarrià'),('54','Sarrià-Sant Gervasi'),('55','Turó de la Peira - Can Peguera'),('56','Vallarca y los Penitentes'),('57','Verdum - Los Roquetes'),('58','Villa de Gracia'),('59','Vilapicina i la Torre Llobeta'),('60','Fort Pienc')]
    roomTypeValues = [('','Select'),('1','Entire House/Apartment'),('2','Private Room'),('3','Shared Room')]
    bedTypeValues = [('','Select'),('1','Real Bed'),('2','Pull-out Sofa'),('3','Futon'),('4','Couch'),('3','Airbed')]
    cancelationPolicyTypeValues = [('','Select'),('1','Strict'),('2','Moderate'),('3','Flexible')]

    name = forms.CharField(max_length=200)

    street = forms.CharField(max_length=100)
    number = forms.IntegerField(min_value=1,max_value=1500)

    accomodates = forms.IntegerField(min_value=1,max_value=100)
    bathrooms = forms.IntegerField(min_value=0,max_value=12)
    bedrooms = forms.IntegerField(min_value=1, max_value=12)
    beds = forms.IntegerField(min_value=1, max_value=22)
    guestsIncluded = forms.IntegerField(min_value=0, max_value=22)
    availability30 = forms.IntegerField(min_value=0, max_value=30)
    availability60 = forms.IntegerField(min_value=0, max_value=60)
    availability90 = forms.IntegerField(min_value=0, max_value=90)
    availability365 = forms.IntegerField(min_value=0, max_value=365)
    hostListingsCount = forms.IntegerField(min_value=1, max_value=500)

    #booleanFields
    entireApartament = forms.BooleanField(required=False,initial=False)
    apartmentDeposit = forms.BooleanField(required=False,initial=False)
    hostAbout = forms.BooleanField(required=False,initial=False)
    hostIdentityVerified = forms.BooleanField(required=False,initial=False)
    extraPeople = forms.BooleanField(required=False,initial=False)


    #selectors
    neighborhood = forms.ChoiceField(neighborhoodsValues,)
    cancellationPolicy = forms.ChoiceField(cancelationPolicyTypeValues)
    #TODO search for the asciicode for the ny and the ampersand
    apartamentType = forms.ChoiceField(apartmentValues)
    typeOfRoom = forms.ChoiceField(roomTypeValues)
    typeOfBed = forms.ChoiceField(bedTypeValues)
    verificationUser = []
    amenities = []

    #not in the form items
    pub_date = forms.DateTimeField('date published', required=False)
    finalRecomendedPrice = forms.DecimalField(decimal_places=2, max_digits=8, required=False)


