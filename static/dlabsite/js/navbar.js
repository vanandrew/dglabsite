// Navbar click and fade
function navbar_click (selection,URL,selector){
	$(selection).click(function(){
		$(selector).removeClass('animated');
		$(selector).fadeOut();
		setTimeout(function(){window.location.assign(URL)},600);
	});
};

// check scroll
function checkScroll() {
    var startY = 60;

    if($(window).scrollTop() > startY) {
		$(".navbar").fadeOut();
    }
	else {
		$(".navbar").fadeIn();
    }
};

// only check scroll if navbar exists
if($(".navbar").length > 0) {
    $(window).on("scroll load resize", function() {
        checkScroll();
    });
}