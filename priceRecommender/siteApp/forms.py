# coding=utf-8
from django import forms


class AirbnbRequestForm(forms.Form):
    #SelectorsValues
    apartmentValues = [('0','Selecciona'),('1','Apartamento'),('2','Casa'),('3','Bed and Breakfast'),('4','Adosado'),('5','Autocaravana'),('6','Barco'),('7','Bungalow'),('8','Cabaña'),('9','Chalet'),('10','Dormitorio compartido'),('11','Loft'),('12','Tienda de campaña'),('13','Villa'),('14','Otros')]
    neighborhoodsValues = [('0','Selecciona'),('1','Eixample'),('2','Ciutat Vella'),('3','Sants-Montjuic'),('4','Camp d\'en  Grassot i Gracia Nova'),('5','Can Baro'),('6','Diagonal Mar - La Mar Bella'),('7','Carmel'),('8','Dreta de l\'Eixample'),('9','El Baix Guinardó'),('10','El Besòs i el Maresme'),('11','El Born'),('12','El Camp de l\'Arpa del Clot'),('13','El Clot'),('14','El Coll '),('15','El Congres i els Indians'),('16','El Gótic'),('17','El Poble-Sec'),('18','El Poblenou'),('19','El Putget i Farró'),('20','El Raval'),('21','Glòries -El Parc'),('22','Gràcia'),('23','Guinardó'),('24','Horta'),('25','Horta-Guinardó'),('26','L\'Antiga Esquerra de l\'Eixample'),('27','La Barcelonet'),('28','La Font d\'en Fargues'),('29','La Maternitat i Sant Ramon'),('30','La Nova Esquerra de l\'Eixample'),('31','La Prosperitat'),('32','La Sagrada Familia'),('33','La Sagrera'),('34','La Salud'),('35','La Vall d\'Hebron'),('36','La Verneda i La Pau'),('37','La Vila Olímpica'),('38','Les Corts'),('39','Les Tres Torres'),('40','Navas'),('41','Nou Barris'),('42','Pedralbes'),('43','Porta'),('44','Provençals del Poblenou'),('45','Sant Andreu'),('46','San Andrés de Palomar'),('47','Sant Antoni'),('48','Sant Gervasi - Galvany'),('49','Sant Gervasi - La Bonanova'),('50','Sant Martí'),('51','San Martín de Provensals'),('52','Sant Pere/ Santa Caterina'),('53','Sarrià'),('54','Sarrià-Sant Gervasi'),('55','Turó de la Peira - Can Peguera'),('56','Vallarca y los Penitentes'),('57','Verdum - Los Roquetes'),('58','Villa de Gracia'),('59','Vilapicina i la Torre Llobeta'),('60','Fort Pienc')]
    roomTypeValues = [('0','Selecciona'),('1','Casa/Apto. entero'),('2','Habitación privada'),('3','Habitación compartida')]
    bedTypeValues = [('0','Selecciona'),('1','Real Bed'),('2','Pull-out Sofa'),('3','Futon'),('4','Couch'),('3','Airbed')]
    cancelationPolicyTypeValues = [('0','Selecciona'),('1','strict'),('2','moderate'),('3','flexible')]

    name = forms.CharField(max_length=200)

    latitude = forms.CharField(max_length=20)
    longitude = forms.CharField(max_length=20)

    accomodates = forms.IntegerField(min_value=1,max_value=12)
    bathrooms = forms.IntegerField(min_value=0,max_value=12)
    bedrooms = forms.IntegerField(min_value=1, max_value=12)
    beds = forms.IntegerField(min_value=1, max_value=22)
    guestsIncluded = forms.IntegerField(min_value=0, max_value=22)
    entireApartament = forms.BooleanField(required=False)


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


