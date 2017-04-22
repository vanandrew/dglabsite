// Check if came from sibling pages
function sibling(a,b,c,d,e,f)
{
	document.addEventListener('DOMContentLoaded', function() {
		previous_page = document.referrer.split('/');
		page = '/' + previous_page[previous_page.length-1];
		switch(page) {
			case a:
				var sibling = 1;
				break;
			case b:
				var sibling = 1;
				break;
			case c:
				var sibling = 1;
				break;
			case d:
				var sibling = 1;
				break;
			case e:
				var sibling = 1;
				break;
			case f:
				var sibling = 1;
				break;
			default:
				var sibling = 0;
		}
		if(sibling == 1) {
			document.querySelector('.navbar').classList.remove('animated');
			document.querySelector('.navbar').classList.remove('fadeIn');
		}
	});
}
