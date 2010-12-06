var search_term = "{{ keyword }}";
args = {'email' : 'abhishek.twr@gmail.com', 'db' : 'protein'};


$(document).ready(function() {	 
	$('div').mouseup(function() {
		search_term = getSelectedText()

		var loading_html = '<h2>Loading results ... </h2> <img src="{{ url_for('main.static', filename='images/loading.gif') }}">'
		$('#result').html(loading_html);

		var qurl  = "{{ url_for('jsonendpoint.ncbi_egquery', keyword = '') }}" + search_term + "?callback=?"
		$.getJSON(qurl, args, function(data) {
				var html_result = ''
				html_result += "<h3>Matching Results from MolSeek:</h3></br>"
				html_result += data.eGQueryResult[0].Count + '  ... ' + data.eGQueryResult[0].MenuName + ' entries' + '<br>'
				+  data.eGQueryResult[1].Count + '  ... ' + data.eGQueryResult[1].MenuName + ' entries' + '<br>'
				+  data.eGQueryResult[3].Count + '  ... ' + data.eGQueryResult[3].MenuName + ' entries' + '<br>'
				+  data.eGQueryResult[11].Count + '  ... ' + data.eGQueryResult[11].MenuName + ' entries' + '<br>'
				+  data.eGQueryResult[15].Count + '  ... ' + data.eGQueryResult[15].MenuName + ' entries' + '<br>'
				+  data.eGQueryResult[16].Count + '  ... ' + data.eGQueryResult[16].MenuName + ' entries' + '<br>'
				+  data.eGQueryResult[26].Count + '  ... ' + data.eGQueryResult[26].MenuName + ' entries' + '<br>'
				+  data.eGQueryResult[27].Count + '  ... ' + data.eGQueryResult[27].MenuName + ' entries' + '<br>'
				$('#result').html(html_result);
			});

		});

    function getSelectedText() {
		if (window.getSelection) {
			return window.getSelection().toString();
		} else if (document.selection) {
			return document.selection.createRange().text;
		}
		return '';
	}
});
