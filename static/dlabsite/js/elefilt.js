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
			var omnistring = "";
	        for (var i = 0; i < data_array.length; i++) {
				// Create a long string out of each field
	        	omnistring = omnistring + " " + stored_data[data_array[i]];
	        }
			// Search long string using parsed match string
			parsed_string = match_string.split(" ");
			for (var i = 0; i < parsed_string.length; i++) {
				if (omnistring.match(RegExp(parsed_string[i],'i'))) {
					match++
				}
			}
			// show if matched both strings
			if (match == parsed_string.length) {
				$(this).show();
			}
			// hide otherwise
			else {
				$(this).hide();
			}
		});
   }; 
})( jQuery );