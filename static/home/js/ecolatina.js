$(document).ready(function() {
  $(".especialista-hover-text").css({width: "0px" });
  $("#send-budget-form .one-dude").mouseover(function(){
    var target_id = $(this).attr("id");
    if( !$("#" + target_id + "-text").is(':animated') ) {
      $("#especialistas").addClass("grayscaled");
      $("#" + target_id + "-hover").addClass("hovered");
      $("#" + target_id + "-text").animate({width: '270px'}, 200);
    }
  })
  .mouseout(function(){
    var target_id = $(this).attr("id");
    $("#" + target_id + "-text").animate({width: '0px'}, 200, function(){
      $(this).removeClass("hovered");
      $("#" + target_id + "-hover").removeClass("hovered");
      if( $(".especialista-hover-bg.hovered").length == 0 ) 
        $("#especialistas").removeClass("grayscaled");
    })
  });
  $("#about-link").on('click', function(event) {
    event.preventDefault();
    if($(window).width() <= 768){
      $('html,body').animate({scrollTop: $(event.target.hash).offset().top - 130 }, 300, function(){
        $(".navbar-toggle").trigger("click");
      });
    }else{
      $('html,body').animate({scrollTop: $(event.target.hash).offset().top }, 300);
    }
    return false;
  });
  
  $('body').scrollspy({ target: "#ecolatina-nav", offset: 150 });
  
  $('.modal-budget').on('shown.bs.modal', function () {
    $('#budget-form #name').focus();
  });
  
  var hide_form_notification;
  $("#budget-form").submit(function(e){
    e.preventDefault();
    clearTimeout(hide_form_notification);
    $("#budget-notification").hide();
    fullname = $(this).find('#name');
    phone = $(this).find('#phone');
    email = $(this).find('#email');
    company = $(this).find('#company');
    description = $(this).find('#details');
    captcha = $(this).find("#captcha-form");
    
    fullname.removeClass('alert-danger');
    phone.removeClass('alert-danger');
    email.removeClass('alert-danger');
    description.removeClass('alert-danger');
    captcha.removeClass('alert-danger');
    error = "false";
    
    
    if( fullname.val().trim().length == 0 ){
      fullname.addClass("alert-danger"); error = "true";
    }
    if( phone.val().trim().length == 0 ){
      phone.addClass("alert-danger"); error = "true";
    }
    if( description.val().trim().length == 0 ){
      description.addClass("alert-danger"); error = "true3";
    }
    if( email.val().trim().length == 0 ){
      email.addClass("alert-danger"); error = "true";
    }
    

    if (error == "false"){
      $.post('ajax/send_budget_form.php', { captcha: captcha.val(), fullname: fullname.val(), description: description.val(), phone: phone.val(), email: email.val(), company: company.val() }, function(data){
        if ( data.error == "false" ){
          // formulario enviado!
          $("#budget-notification").removeClass("alert-danger").addClass("alert-success").html(data.message).slideDown('fast');
          $('.modal-budget').animate({scrollTop: 200 }, 300);
          // $("#budget-form input, #budget-form textarea").val("");

          $('#captcha').attr("src", 'captcha.php?'+Math.random())
          // aca redirige
          window.location ="../gracias.html";
        }else{
          // algún error raro pasó
          if( data.error_type == "captcha")
            captcha.focus();
          $("#budget-notification").removeClass("alert-success").addClass("alert-danger").html(data.message).slideDown('fast');
          $('.modal-budget').animate({scrollTop: 200 }, 300);
        }
      }, 'json');
    }else{
      $("#budget-notification").removeClass('alert-success').addClass('alert-danger').html('Todos los campos deben estar completados.' ).slideDown('fast');
      $('.modal-budget').animate({scrollTop: 200 }, 300, function(){
        if (email.hasClass("alert-danger"))
          email.focus(); 
        if (phone.hasClass("alert-danger"))
          phone.focus(); 
        if (fullname.hasClass("alert-danger"))
          fullname.focus();
      });
    }
    hide_form_notification = setTimeout(function(){
      $("#budget-notification").slideUp('slow');
    }, 5000)
    
    
    return false;
  });
});
