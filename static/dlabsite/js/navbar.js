// Navbar click and fade
function navbar_click (selection,URL,selector){
	$(selection).click(function(){
		$(selector).removeClass('animated');
		$(selector).fadeOut();
		setTimeout(function(){window.location.assign(URL)},600);
	});
};