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

     /*$( "#datepicker" ).datepicker({
      numberOfMonths: 3,
      showButtonPanel: true,
      createButton:false,
      displayClose:false,
      closeOnSelect:false,
      selectMultiple:true
    });*/

     /*$( "#datepicker" ).multiDatesPicker({
         minDate: 0,
         numberOfMonths: 2,
         inline: true,
         dayNamesMin: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun'],
         beforeShow: function(){
           $(".ui-datepicker").css('font-size', 12)
         },
         onSelect: function(dateText, inst) {
             var value = $('#datepickerValues').val();
             value = value + "[" + dateText +"],"
             $("input[name='datepickerValues']").val(value);
         },
         dateFormat: "dd-mm-yy",
         multiple : true
     });*/
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

    var output = 0;
    if($('#id_apartmentDeposit').checked) {
        output = 1;
    }
    $('#valueApartamentDeposit').val(output);//.toJSON());

    output = 0;
    if($('#id_hostAbout').checked) {
        output = 1;
    }
    $('#valuehostAbout').val(output);

    output = 0;
    if($('#id_hostIdentityVerified').checked) {
        output = 1;
    }
    $('#valuehostIdentityVerified').val(output);

    output = 0;
    if($('#id_extraPeople').checked) {
        output = 1;
    }
    $('#valueExtraPeople').val(output);
}
