//function to navigate the navbar
$(".nav a").on("click", function(){
    var href = $(this).attr('href');
    $(".nav").find(".active").removeClass("active");
    $("body").find(".content").addClass("hidden");
    $(this).parent().addClass("active");
    $("body").find(href).fadeIn().removeClass("hidden");
});