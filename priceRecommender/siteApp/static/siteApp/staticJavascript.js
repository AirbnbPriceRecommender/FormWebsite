/**
 * Created by miquel.puigdomenech on 05/07/2016.
 */

$(document).ready(function () {
    var values =['TV', 'Wireless Internet', 'Air Conditioning', 'Kitchen', 'Smoking Allowed', 'Hot Tub', 'Heating',
    'Family/Kid Friendly', 'Suitable for Events', 'Dryer', 'Smoke Detector', 'Shampoo', 'Internet', 'Elevator in Building',
    'Washer', 'Buzzer/Wireless Intercom', 'Essentials', 'Lock on Bedroom Door', '24-Hour Check-in', 'Hangers',
    'Laptop Friendly Workspace', 'Hair Dryer', 'Iron', 'First Aid Kit', 'Cable TV', 'Indoor Fireplace', 'Fire Extinguisher',
    'Breakfast', 'Pets live on this property', 'Pets Allowed', 'Other pet(s)', 'Free Parking on Premises', 'Safety Card',
    'Doorman', 'Cat(s)', 'Wheelchair Accessible', 'Dog(s)', 'Carbon Monoxide Detector', 'Gym', 'Washer / Dryer', 'Pool'];
    $('#amenities').append("<table>");
    $.each(values,function(index,value){
        if(index%5== 0){
            $('#amenities').append("<td>");
        }
        var item = value;
        var $newInput = "<input id='"+item+"-input' type='checkbox' value='"+item+"'>"+item+"</input>   " ;

        $('#amenities').append($newInput);
        if(index%5== 0){
            $('#amenities').append("</td>");
        }
    });
    $('#amenities').append("</table>");

    var values =['email','phone','facebook','linkedin','google','jumio','reviews','manual'];
    $('#verifications').append("<table>");
    $.each(values,function(index,value){
        var item = value;
        var $newInput = "<input id='"+item+"-input' type='checkbox' value='"+item+"'>"+item+"</input>   " ;
        $('#verifications').append($newInput);
    });
    $('#verifications').append("</table>");

});




var runFunction = function (){
    var amenities = [];
    $('#amenities > input').each(function(){
        if(this.checked){
            amenities+="["+this.value+"],"
        }
    });
    $('#valuesAmenities').val(amenities);//.toJSON());

    var verifications = [];
    $('#verifications > input').each(function(){
        if(this.checked){
            verifications+="["+this.value+"],"
        }
    });
    $('#valuesVerifications').val(verifications);//.toJSON());
}
