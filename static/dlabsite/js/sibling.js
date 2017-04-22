// Check if came from sibling pages
function sibling(mypages)
{
	document.addEventListener('DOMContentLoaded', function() {
		var previous_page = document.referrer.split('/');
		var page = '/' + previous_page[previous_page.length-1];
		var sibling = 0;
		for (var i = 0; i < mypages.length; i++) {
			if (page == mypages[i]) {
				var sibiling = 1;
			}
		}
		
		if(sibling == 1) {
			document.querySelector('.navbar').classList.remove('animated');
			document.querySelector('.navbar').classList.remove('fadeIn');
		}
	});
}
