$( "#id_s1_e1_comment" )
    .focusout(function() {
      // alert($( "#id_s1_e1_comment" ).val());
      if($( "#id_s1_e1_comment" ).val() !=1){
        $("#id_s1_e1_comment").css("background-color", "#f24858");
      $("#id_s1_e1_comment").css("color", "white");
      }
      else if($( "#id_s1_e1_comment" ).val() ==1){
        $("#id_s1_e1_comment").css("background-color", "white");
      $("#id_s1_e1_comment").css("color", "black");
      }
      
      // $( "#id_s1_e1_comment" ).text( "focusout fired: " + focus + "x" );
      // $( "#id_s1_e1_comment" ).css('background-color','red');
    });