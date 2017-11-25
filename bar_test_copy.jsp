<%@page contentType="text/html; charset=euc-kr"%>
<html>
<head>
<title>Inzent bar test</title>
   <script src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
   <script src="http://code.highcharts.com/highcharts.js"></script>  
</head>
<body>
<div id="container" style="width: 550px; height: 400px; margin: 0 auto float:right"></div>
<script language="JavaScript">
$(document).ready(function() {  
   var chart = {
      type: 'column'
   };
   var title = {
      text: 'inzent archive'   
   };
   var subtitle = {
      text: null
   };
   var xAxis = {
      categories: ['1st archive', '2nd archive', 'total archive'],
      title: {
         text: null
      }
   };
   var yAxis = {
      min: 0,
      title: {
         text: 'archive space',
         align: 'middle'
      },
      labels: {
         overflow: 'justify'
      }
   };
   var tooltip = {
      valueSuffix: ' bytes'
   };
   var plotOptions = {
      column: {
         dataLabels: {
            enabled: true
         }
      },
	  series: {
	     stacking: 'percent'
	  }
   };
   var legend = {
      layout: 'vertical',
      align: 'right',
      verticalAlign: 'top',
      x: -40,
      y: 100,
      floating: true,
      borderWidth: 1,
      backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
      shadow: true
   };
   var credits = {
      enabled: false
   };
   
   var series= [{
         name: 'left',
            data: [${LEFT1}, ${LEFT2}, ${LEFT1+LEFT2}]
        }, {
            name: 'using',
            data: [${USING1}, ${USING2}, ${USING1+USING2}]
        }
   ];     
      
   var json = {};   
   json.chart = chart; 
   json.title = title;   
   json.subtitle = subtitle; 
   json.tooltip = tooltip;
   json.xAxis = xAxis;
   json.yAxis = yAxis;  
   json.series = series;
   json.plotOptions = plotOptions;
   //json.legend = legend;
   json.credits = credits;
   $('#container').highcharts(json);
  
});
</script>
</body>
</html>