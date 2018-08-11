
$(document).ready(function() {

    $('#slides').superslides({
        animation: 'fade',
        animation_speed: 1000,
        play: 5000,
        pagination: false
    });
});
$(document).ready(function(){
    $('#inputBtn').hover(function(){
        $('#inputBtn').val('Click Me!!')
    });
})