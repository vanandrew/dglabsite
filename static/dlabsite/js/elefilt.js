// Simple Element Filter
// Hides/Shows element based on input string and data attributes
// Usage:
// JS
// $(selector).Elefilt('string', ['data1','data2',...])
//
// HTML
// <element data-data1="..." data-data2="...">...</element>

(function($) {
	$.fn.Elefilt = function(match_string,data_array) {
   		// Loop over all selectors
      	this.each(function () {
	   		// Get the data tags of the element
	      	stored_data = $(this).data();
	        // Access each data tag based on input data_array
			var match = 0; //Track # of matches in each field
	        for (var i = 0; i < data_array.length; i++) {
	        	if (stored_data[data_array[i]].match(RegExp(match_string,'i'))) {
	          		match++;
	        	}
	        }
			if (match > 0) {
				$(this).show();
			}
			else {
				$(this).hide();
			}
		});
   }; 
})( jQuery );