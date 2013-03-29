function validateForm(){
			var page = document.forms["input"]["page"].value;
			if(!isNaN(page) && page > 0)
				return true;
			else{
				$(document).ready(function(){
				$(".open-pop").popover('destroy');
				$(".open-pop").popover('show');
				});
				return false;
			}
		}