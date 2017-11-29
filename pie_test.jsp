<%@page contentType="text/html; charset=euc-kr"%>

<html>
<head>
<title>inzent pie test</title>
   <script src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
   <script src="http://code.highcharts.com/highcharts.js"></script>  
</head>
<body>
<div id="container" style="width: 300px; height:400px; float:left; margin:0"></div>
<!--style="width: 50%; height: 400px; margin: 0 auto"-->
<div id="container2" style="width: 300px; height:400px; float:left; margin:0"></div>
<div id="container3" style="width: 300px; height:400px; float:left; margin:0"></div>
<script language="JavaScript">
$(document).ready(function() {  
   var chart = {
       plotBackgroundColor: null,
       plotBorderWidth: null,
       plotShadow: false
   };
   var title = {
      text: '1st archive'   
   };      
   var credits={
    enabled: false
  };
   var tooltip = {
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
   };
   var plotOptions = {
      pie: {
         allowPointSelect: true,
         cursor: 'pointer',
         dataLabels: {
            enabled: false           
         },
         showInLegend: false
      }
   };
   var series= [{
      type: 'pie',
      name: 'archive space',
      data: [
         ['using',   ${USING1}],
         ['left',   ${LEFT1}]
      ]
   }];     
      
   var json = {};   
   json.chart = chart; 
   json.title = title;     
   json.credits=credits;
   json.tooltip = tooltip;  
   json.series = series;
   json.plotOptions = plotOptions;
   $('#container').highcharts(json);
});

$(document).ready(function() {  
   var chart = {
       plotBackgroundColor: null,
       plotBorderWidth: null,
       plotShadow: false
   };
   var title2 = {
      text: '2nd archive'   
   };      
   var credits={
    enabled: false
  };
   var tooltip = {
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
   };
   var plotOptions2 = {
      pie: {
         allowPointSelect: true,
         cursor: 'pointer',
         dataLabels: {
            enabled: false           
         },
         showInLegend: false
      }
   };
   var series2= [{
      type: 'pie',
      name: 'archive space',
      data: [
         ['using',   ${USING2}],
         ['left',   ${LEFT2}]
      ]
   }];     
      
   var json = {};   
   json.chart = chart; 
   json.title = title2;  
   json.credits=credits;  
   json.tooltip = tooltip;  
   json.series = series2;
   json.plotOptions = plotOptions2;
   $('#container2').highcharts(json);
});

$(document).ready(function() {  
   var chart = {
       plotBackgroundColor: null,
       plotBorderWidth: null,
       plotShadow: false
   };
   var title3 = {
      text: 'total archive'   
   };      
   var credits={
    enabled: false
  };
   var tooltip = {
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
   };
   var plotOptions = {
      pie: {
         allowPointSelect: true,
         cursor: 'pointer',
         dataLabels: {
            enabled: false           
         },
         showInLegend: true
      }
   };
   var series3= [{
      type: 'pie',
      name: 'archive space',
      data: [
         ['using',   ${USING1+USING2}],
         ['left',   ${LEFT1+LEFT2}]
      ]
   }];     
      
   var json = {};   
   json.chart = chart; 
   json.title = title3;     
   json.credits=credits;
   json.tooltip = tooltip;  
   json.series = series3;
   json.plotOptions = plotOptions;
   $('#container3').highcharts(json);
});
</script>
</body>
</html>