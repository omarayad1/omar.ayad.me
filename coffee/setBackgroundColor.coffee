$ ->
	$.get '/bgcolor', (data) ->
		$('html').css 'background-color', data
		$('body').css 'background-color', data