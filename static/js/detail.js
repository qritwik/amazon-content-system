$(document).ready(function() {






$("#btn_click").click(function(){


//-----------------------------------------------------------------------------------------------

  // Resolution->Bullet Point 1

  var resolution = $('#resolution').val();
  var refresh = $('#refresh').val();
  var view = $('#view').val();


  if (($.trim($('#resolution').val()) != '') && ($.trim($('#refresh').val()) == '') && ($.trim($('#view').val()) == '')) {
    var bp1_f = "Resolution: "+resolution
  }
  else if (($.trim($('#resolution').val()) != '') && ($.trim($('#refresh').val()) != '') && ($.trim($('#view').val()) == '')) {
    var bp1_f = "Resolution: "+resolution+" | "+"Refresh Rate: "+refresh
  }
  else if (($.trim($('#resolution').val()) != '') && ($.trim($('#refresh').val()) == '') && ($.trim($('#view').val()) != '')) {
    var bp1_f = "Resolution: "+resolution+" | "+"Viewing angle: "+view
  }

  else if (($.trim($('#resolution').val()) == '') && ($.trim($('#refresh').val()) == '') && ($.trim($('#view').val()) == '')) {
    var bp1_f = ""
  }

  else {
    var bp1_f = "Resolution: "+resolution+" | "+"Refresh Rate: "+refresh+" | "+"Viewing angle: "+view

  }
  $('#bp1').val(bp1_f);

//-----------------------------------------------------------------------------------------------



//-----------------------------------------------------------------------------------------------

  // Display->Bullet Point 2

  var ds1 = $('#ds1').val();
  var ds2 = $('#ds2').val();
  var ds3 = $('#ds3').val();
  var ds4 = $('#ds4').val();
  var ds5 = $('#ds5').val();

  if (($.trim($('#ds1').val()) != '') && ($.trim($('#ds2').val()) == '') && ($.trim($('#ds3').val()) == '') && ($.trim($('#ds4').val()) == '') && ($.trim($('#ds5').val()) == '')){
    var bp2_f = "Display: "+ds1

  }
  else if (($.trim($('#ds1').val()) != '') && ($.trim($('#ds2').val()) != '') && ($.trim($('#ds3').val()) == '') && ($.trim($('#ds4').val()) == '') && ($.trim($('#ds5').val()) == '')){
    var bp2_f = "Display: "+ds1+" | "+ds2

  }
  else if (($.trim($('#ds1').val()) != '') && ($.trim($('#ds2').val()) != '') && ($.trim($('#ds3').val()) != '') && ($.trim($('#ds4').val()) == '') && ($.trim($('#ds5').val()) == '')){
    var bp2_f = "Display: "+ds1+" | "+ds2+" | "+ds3

  }

  else if (($.trim($('#ds1').val()) != '') && ($.trim($('#ds2').val()) != '') && ($.trim($('#ds3').val()) != '') && ($.trim($('#ds4').val()) != '') && ($.trim($('#ds5').val()) == '')){
    var bp2_f = "Display: "+ds1+" | "+ds2+" | "+ds3+" | "+ds4

  }
  else if (($.trim($('#ds1').val()) != '') && ($.trim($('#ds2').val()) != '') && ($.trim($('#ds3').val()) != '') && ($.trim($('#ds4').val()) != '') && ($.trim($('#ds5').val()) != '')){
    var bp2_f = "Display: "+ds1+" | "+ds2+" | "+ds3+" | "+ds4+" | "+ds5

  }

  else if (($.trim($('#ds1').val()) == '') && ($.trim($('#ds2').val()) == '') && ($.trim($('#ds3').val()) == '') && ($.trim($('#ds4').val()) == '') && ($.trim($('#ds5').val()) == '')){
    var bp2_f = ""

  }

  else{
    var bp2_f = "Display: "+ds1+" | "+ds2+" | "+ds3+" | "+ds4+" | "+ds5


  }




  $('#bp2').val(bp2_f);

//-----------------------------------------------------------------------------------------------



//-----------------------------------------------------------------------------------------------

  // HDMI,USB,VGA->Bullet Point 4

  var hdmi = $('#hdmi').val();
  var usb = $('#usb').val();
  var vga = $('#vga').val();


  if (($.trim($('#hdmi').val()) != 0) && ($.trim($('#usb').val()) == 0) && ($.trim($('#vga').val()) == 0)) {
    var bp4_f = "Connectivity: "+ hdmi + " HDMI ports to connect set top box, Blu Ray players, gaming console"
  }
  else if (($.trim($('#hdmi').val()) != 0) && ($.trim($('#usb').val()) != 0) && ($.trim($('#vga').val()) == 0)) {
    var bp4_f = "Connectivity: " +hdmi+ " HDMI ports to connect set top box, Blu Ray players, gaming console | "+usb+" USB ports to connect hard drives and other USB devices"
  }
  else if (($.trim($('#hdmi').val()) != 0) && ($.trim($('#usb').val()) == 0) && ($.trim($('#vga').val()) != 0)) {
    var bp4_f = "Connectivity: " +hdmi+ " HDMI ports to connect set top box, Blu Ray players, gaming console | "+vga+" VGA Port to connect laptops"
  }
  else if (($.trim($('#hdmi').val()) == 0) && ($.trim($('#usb').val()) != 0) && ($.trim($('#vga').val()) == 0)) {
    var bp4_f = "Connectivity: "+usb+" USB ports to connect hard drives and other USB devices"
  }
  else if (($.trim($('#hdmi').val()) == 0) && ($.trim($('#usb').val()) == 0) && ($.trim($('#vga').val()) != 0)) {
    var bp4_f = "Connectivity: "+vga+" VGA Port to connect laptops"
  }
  else if (($.trim($('#hdmi').val()) == 0) && ($.trim($('#usb').val()) != 0) && ($.trim($('#vga').val()) != 0)) {
    var bp4_f = "Connectivity: " +usb+" USB ports to connect hard drives and other USB devices | "+vga+" VGA Port to connect laptops"
  }
  else if (($.trim($('#hdmi').val()) == 0) && ($.trim($('#usb').val()) == 0) && ($.trim($('#vga').val()) == 0)) {
    var bp4_f = ""
  }

  else{
    var bp4_f = "Connectivity: "+ hdmi + " HDMI ports to connect set top box, Blu Ray players, gaming console | "+usb+" USB ports to connect hard drives and other USB devices | "+vga+" VGA Port to connect laptops"

  }

  $('#bp4').val(bp4_f);

//-----------------------------------------------------------------------------------------------


//-----------------------------------------------------------------------------------------------

  // Sound->Bullet Point 5

  var s1 = $('#s1').val();
  var s2 = $('#s2').val();
  var s3 = $('#s3').val();
  var s4 = $('#s4').val();
  var s5 = $('#s5').val();

  if (($.trim($('#s1').val()) != '') && ($.trim($('#s2').val()) == '') && ($.trim($('#s3').val()) == '') && ($.trim($('#s4').val()) == '') && ($.trim($('#s5').val()) == '')){
    var bp5_f = "Sound: "+s1

  }
  else if (($.trim($('#s1').val()) != '') && ($.trim($('#s2').val()) != '') && ($.trim($('#s3').val()) == '') && ($.trim($('#s4').val()) == '') && ($.trim($('#s5').val()) == '')){
    var bp5_f = "Sound: "+s1+" | "+s2

  }
  else if (($.trim($('#s1').val()) != '') && ($.trim($('#s2').val()) != '') && ($.trim($('#s3').val()) != '') && ($.trim($('#s4').val()) == '') && ($.trim($('#s5').val()) == '')){
    var bp5_f = "Sound: "+s1+" | "+s2+" | "+s3

  }

  else if (($.trim($('#s1').val()) != '') && ($.trim($('#s2').val()) != '') && ($.trim($('#s3').val()) != '') && ($.trim($('#s4').val()) != '') && ($.trim($('#s5').val()) == '')){
    var bp5_f = "Sound: "+s1+" | "+s2+" | "+s3+" | "+s4

  }
  else if (($.trim($('#s1').val()) != '') && ($.trim($('#s2').val()) != '') && ($.trim($('#s3').val()) != '') && ($.trim($('#s4').val()) != '') && ($.trim($('#s5').val()) != '')){
    var bp5_f = "Sound: "+s1+" | "+s2+" | "+s3+" | "+s4+" | "+s5

  }

  else if (($.trim($('#s1').val()) == '') && ($.trim($('#s2').val()) == '') && ($.trim($('#s3').val()) == '') && ($.trim($('#s4').val()) == '') && ($.trim($('#s5').val()) == '')){
    var bp5_f = ""

  }

  else{
    var bp5_f = "Sound: "+s1+" | "+s2+" | "+s3+" | "+s4+" | "+s5


  }




  $('#bp5').val(bp5_f);

//-----------------------------------------------------------------------------------------------



//-----------------------------------------------------------------------------------------------

  // Warranty->Bullet Point 7

  var year = $('#year').val();
  var brand = $('#brand').val();



    var bp7_f = "Warranty: "+year+" year standard manufacturer warranty from "+ brand


  $('#bp7').val(bp7_f);

//-----------------------------------------------------------------------------------------------







//-----------------------------------------------------------------------------------------------

  // Installation->Bullet Point 6

  var brand6 = $('#brand6').val();
  var contact6 = $('#contact6').val();



    var bp6_f = "Installation: For installation/wall mounting/demo of this product once delivered,  directly contact "+brand6+" at "+contact6+" and provide product's model name and seller's details mentioned on your invoice. The service center will allot you a convenient slot for the service"


  $('#bp6').val(bp6_f);

//-----------------------------------------------------------------------------------------------




//-----------------------------------------------------------------------------------------------

  // Additional Info->Bullet Point 8

  var a1 = $('#a1').val();
  var a2 = $('#a2').val();
  var a3 = $('#a3').val();
  var a4 = $('#a4').val();
  var a5 = $('#a5').val();

  if (($.trim($('#a1').val()) != '') && ($.trim($('#a2').val()) == '') && ($.trim($('#a3').val()) == '') && ($.trim($('#a4').val()) == '') && ($.trim($('#a5').val()) == '')){
    var bp8_f = "Additional Information: "+a1

  }
  else if (($.trim($('#a1').val()) != '') && ($.trim($('#a2').val()) != '') && ($.trim($('#a3').val()) == '') && ($.trim($('#a4').val()) == '') && ($.trim($('#a5').val()) == '')){
    var bp8_f = "Additional Information: "+a1+" | "+a2

  }
  else if (($.trim($('#a1').val()) != '') && ($.trim($('#a2').val()) != '') && ($.trim($('#a3').val()) != '') && ($.trim($('#a4').val()) == '') && ($.trim($('#a5').val()) == '')){
    var bp8_f = "Additional Information: "+a1+" | "+a2+" | "+a3

  }

  else if (($.trim($('#a1').val()) != '') && ($.trim($('#a2').val()) != '') && ($.trim($('#a3').val()) != '') && ($.trim($('#a4').val()) != '') && ($.trim($('#a5').val()) == '')){
    var bp8_f = "Additional Information: "+a1+" | "+a2+" | "+a3+" | "+a4

  }
  else if (($.trim($('#a1').val()) != '') && ($.trim($('#a2').val()) != '') && ($.trim($('#a3').val()) != '') && ($.trim($('#a4').val()) != '') && ($.trim($('#a5').val()) != '')){
    var bp8_f = "Additional Information: "+a1+" | "+a2+" | "+a3+" | "+a4+" | "+a5

  }

  else if (($.trim($('#a1').val()) == '') && ($.trim($('#a2').val()) == '') && ($.trim($('#a3').val()) == '') && ($.trim($('#a4').val()) == '') && ($.trim($('#a5').val()) == '')){
    var bp8_f = ""

  }

  else{
    var bp8_f = "Additional Information: "+a1+" | "+a2+" | "+a3+" | "+a4+" | "+a5


  }




  $('#bp8').val(bp8_f);

//-----------------------------------------------------------------------------------------------







//-----------------------------------------------------------------------------------------------

  // Smart TV Optional->Bullet Point 3

  var st1 = $('#st1').val();
  var st2 = $('#st2').val();
  var st3 = $('#st3').val();
  var st4 = $('#st4').val();
  var st5 = $('#st5').val();
  var st6 = $('#st6').val();
  var st7 = $('#st7').val();
  var st8 = $('#st8').val();
  var st9 = $('#st9').val();
  var st10 = $('#st10').val();

  if (($.trim($('#st1').val()) != '') && ($.trim($('#st2').val()) == '') && ($.trim($('#st3').val()) == '') && ($.trim($('#st4').val()) == '') && ($.trim($('#st5').val()) == '') && ($.trim($('#st6').val()) == '') && ($.trim($('#st7').val()) == '') && ($.trim($('#st8').val()) == '') && ($.trim($('#st9').val()) == '') && ($.trim($('#st10').val()) == '')){
    var bp3_f = "Smart TV Features: "+st1

  }
  else if (($.trim($('#st1').val()) != '') && ($.trim($('#st2').val()) != '') && ($.trim($('#st3').val()) == '') && ($.trim($('#st4').val()) == '') && ($.trim($('#st5').val()) == '') && ($.trim($('#st6').val()) == '') && ($.trim($('#st7').val()) == '') && ($.trim($('#st8').val()) == '') && ($.trim($('#st9').val()) == '') && ($.trim($('#st10').val()) == '')){
    var bp3_f = "Smart TV Features: "+st1+" | "+st2

  }
  else if (($.trim($('#st1').val()) != '') && ($.trim($('#st2').val()) != '') && ($.trim($('#st3').val()) != '') && ($.trim($('#st4').val()) == '') && ($.trim($('#st5').val()) == '') && ($.trim($('#st6').val()) == '') && ($.trim($('#st7').val()) == '') && ($.trim($('#st8').val()) == '') && ($.trim($('#st9').val()) == '') && ($.trim($('#st10').val()) == '')){
    var bp3_f = "Smart TV Features: "+st1+" | "+st2+" | "+st3

  }

  else if (($.trim($('#st1').val()) != '') && ($.trim($('#st2').val()) != '') && ($.trim($('#st3').val()) != '') && ($.trim($('#st4').val()) != '') && ($.trim($('#st5').val()) == '') && ($.trim($('#st6').val()) == '') && ($.trim($('#st7').val()) == '') && ($.trim($('#st8').val()) == '') && ($.trim($('#st9').val()) == '') && ($.trim($('#st10').val()) == '')){
    var bp3_f = "Smart TV Features: "+st1+" | "+st2+" | "+st3+" | "+st4

  }
  else if (($.trim($('#st1').val()) != '') && ($.trim($('#st2').val()) != '') && ($.trim($('#st3').val()) != '') && ($.trim($('#st4').val()) != '') && ($.trim($('#st5').val()) != '') && ($.trim($('#st6').val()) == '') && ($.trim($('#st7').val()) == '') && ($.trim($('#st8').val()) == '') && ($.trim($('#st9').val()) == '') && ($.trim($('#st10').val()) == '')){
    var bp3_f = "Smart TV Features: "+st1+" | "+st2+" | "+st3+" | "+st4+" | "+st5

  }

  else if (($.trim($('#st1').val()) != '') && ($.trim($('#st2').val()) != '') && ($.trim($('#st3').val()) != '') && ($.trim($('#st4').val()) != '') && ($.trim($('#st5').val()) != '') && ($.trim($('#st6').val()) != '') && ($.trim($('#st7').val()) == '') && ($.trim($('#st8').val()) == '') && ($.trim($('#st9').val()) == '') && ($.trim($('#st10').val()) == '')){
    var bp3_f = "Smart TV Features: "+st1+" | "+st2+" | "+st3+" | "+st4+" | "+st5+" | "+st6

  }
  else if (($.trim($('#st1').val()) != '') && ($.trim($('#st2').val()) != '') && ($.trim($('#st3').val()) != '') && ($.trim($('#st4').val()) != '') && ($.trim($('#st5').val()) != '') && ($.trim($('#st6').val()) != '') && ($.trim($('#st7').val()) != '') && ($.trim($('#st8').val()) == '') && ($.trim($('#st9').val()) == '') && ($.trim($('#st10').val()) == '')){
    var bp3_f = "Smart TV Features: "+st1+" | "+st2+" | "+st3+" | "+st4+" | "+st5+" | "+st6+" | "+st7

  }
  else if (($.trim($('#st1').val()) != '') && ($.trim($('#st2').val()) != '') && ($.trim($('#st3').val()) != '') && ($.trim($('#st4').val()) != '') && ($.trim($('#st5').val()) != '') && ($.trim($('#st6').val()) != '') && ($.trim($('#st7').val()) != '') && ($.trim($('#st8').val()) != '') && ($.trim($('#st9').val()) == '') && ($.trim($('#st10').val()) == '')){
    var bp3_f = "Smart TV Features: "+st1+" | "+st2+" | "+st3+" | "+st4+" | "+st5+" | "+st6+" | "+st7+" | "+st8

  }
  else if (($.trim($('#st1').val()) != '') && ($.trim($('#st2').val()) != '') && ($.trim($('#st3').val()) != '') && ($.trim($('#st4').val()) != '') && ($.trim($('#st5').val()) != '') && ($.trim($('#st6').val()) != '') && ($.trim($('#st7').val()) != '') && ($.trim($('#st8').val()) != '') && ($.trim($('#st9').val()) != '') && ($.trim($('#st10').val()) == '')){
    var bp3_f = "Smart TV Features: "+st1+" | "+st2+" | "+st3+" | "+st4+" | "+st5+" | "+st6+" | "+st7+" | "+st8+" | "+st9

  }
  else if (($.trim($('#st1').val()) != '') && ($.trim($('#st2').val()) != '') && ($.trim($('#st3').val()) != '') && ($.trim($('#st4').val()) != '') && ($.trim($('#st5').val()) != '') && ($.trim($('#st6').val()) != '') && ($.trim($('#st7').val()) != '') && ($.trim($('#st8').val()) != '') && ($.trim($('#st9').val()) != '') && ($.trim($('#st10').val()) != '')){
    var bp3_f = "Smart TV Features: "+st1+" | "+st2+" | "+st3+" | "+st4+" | "+st5+" | "+st6+" | "+st7+" | "+st8+" | "+st9+" | "+st10

  }

  else if (($.trim($('#st1').val()) == '') && ($.trim($('#st2').val()) == '') && ($.trim($('#st3').val()) == '') && ($.trim($('#st4').val()) == '') && ($.trim($('#st5').val()) == '') && ($.trim($('#st6').val()) == '') && ($.trim($('#st7').val()) == '') && ($.trim($('#st8').val()) == '') && ($.trim($('#st9').val()) == '') && ($.trim($('#st10').val()) == '')){
    var bp3_f = ""

  }



  else{
    var bp3_f = "Smart TV Features: "+st1+" | "+st2+" | "+st3+" | "+st4+" | "+st5


  }




  $('#bp3').val(bp3_f);

//-----------------------------------------------------------------------------------------------













});


});
