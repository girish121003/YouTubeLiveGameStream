
$(document).ready(function() {
    $('#slides').superslides({
        animation: 'fade',
        animation_speed: 1000,
        play: 5000,
        pagination: false
    });
});
$(".btnQuit").click(function(){
    $('#divIframeVideo').attr('src', '');
    $(".inner").show();
    $("#divId1").hide();
});
$('.next').click(function() {
  $('.giru').animate({
    scrollLeft: "-=200px"
  }, "slow");
});
/*Everytime a thumnail of type input is clicked user will be redirected to the
  youtube vide contained inside the division with id divId1 */
$('input').on('click', function () {
     $(".inner").hide();
    $("#divId1").show();
    var x=$(this).attr('value')/*getting the video id stored as a value inside this input tag*/
    var urlVideo = 'https://www.youtube.com/embed/' + x+'?autoplay=1';
    var urlChat='https://www.youtube.com/live_chat?v='+x
    $('#divIframeVideo').attr('src', urlVideo)/* pass the video url to iframe as a src attribute */
    $('#divIframeChat').attr('src',urlChat)

});

$(function(){
 $("#divIframeVideo").hover(function(){
  $("#divIframeChat").css({opacity: 0.2});
 },function(){
$("#divIframeChat").css({opacity: 1});

});
});
$(function(){
 $("#divIframeChat").hover(function(){
  $("#divIframeVideo").css({opacity: 0.2});
 },function(){
$("#divIframeVideo").css({opacity: 1});

});
});









