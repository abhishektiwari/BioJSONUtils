var search_term = "{{ keyword }}";

var qurl  = "http://preview.ncbi.nlm.nih.gov/portal/utils/autocomp.fcgi?dict=pm_related_queries_2&callback=?&q=" + search_term

$(document).ready(function() {	
	$.getJSON(qurl,function(data) {
		alert("JSON Data: " + data);
		var html_result = '<h2>Matching Results from MolSeek:</h2></br>'
		html_result += "<ul>"
		$.each(data.items, function(i,item}{
      			html_result.append($("<li/>").text(item));
    		});
		html_result+'</ul>';
		$('#result').html(html_result);

	});
});


<form id="search" action="search">
  <input name="q" id="q">
  <input type="submit" value="search">
</form>

<ul id="results"></ul>

<script>
  $("#search").submit(function(){
    $.getJSON("http://preview.ncbi.nlm.nih.gov/portal/utils/autocomp.fcgi?dict=pm_related_queries_2&callback=?&q=" + encodeURIComponent($("#q").val()), NSuggest_CreateData);
    return false;
  });

  function NSuggest_CreateData(q, data){
    var ul = $("#results");
    ul.empty();
    $.each(data, function(i, text){
      ul.append($("<li/>").text(text));
    });
  }
</script>
