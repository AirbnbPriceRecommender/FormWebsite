/**
 * Created by miquel.puigdomenech on 05/07/2016.
 */

$(document).ready(function () {
    var values =['TV', 'Wireless Internet', 'Air Conditioning', 'Kitchen', 'Smoking Allowed', 'Hot Tub', 'Heating',
    'Family/Kid Friendly', 'Suitable for Events', 'Dryer', 'Smoke Detector', 'Shampoo', 'Internet', 'Elevator in Building',
    'Washer', 'Buzzer/Wireless Intercom', 'Essentials', 'Lock on Bedroom Door', '24-Hour Check-in', 'Hangers',
    'Laptop Friendly Workspace', '', 'Hair Dryer', 'Iron', 'First Aid Kit', 'Cable TV', 'Indoor Fireplace', 'Fire Extinguisher',
    'Breakfast', 'Pets live on this property', 'Pets Allowed', 'Other pet(s)', 'Free Parking on Premises', 'Safety Card',
    'Doorman', 'Cat(s)', 'Wheelchair Accessible', 'Dog(s)', 'Carbon Monoxide Detector', 'Gym', 'Washer / Dryer', 'Pool'];

    $(values.each(function(){
        var item = $(this);
        var $newInput = $( "<input id=",item,"-input type='checkbox' value=",item,">",item,"</input>" ), newinput2 = document.createElement( "input" );
        $('#amenities').append($newInput,[newinput2]);
    }));
});




var runFunction = function (){


}
