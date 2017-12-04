function load_cgi(sy_, sm_, sd_, ey_, em_, ed_, file, id) {
	var jv = {sy : sy_, sm : sm_, sd : sd_, 
			  ey : ey_, em : em_, ed : ed_, fn : file};
	$.post('inzent.cgi', jv, function(data,status) {
		$(id).html(data);
	})
}
Date.prototype.addDays = function(days) {
    var dat = new Date(this.valueOf());
    dat.setDate(dat.getDate() + days);
    return dat;
}
$(document).ready( function() {      
	var today=new Date();
	var ey = today.getFullYear();
	var em = today.getMonth();
	var ed = today.getDate();
	var prev = today.addDays(-60);
	var sy = prev.getFullYear();
	var sm = prev.getMonth() + 1;
	var sd = prev.getDate();
	load_cgi(ey-1, em, 0, ey, em, 0, '', '#1');//지난 12개월간통계
	load_cgi(ey, em, 0, ey, em, 0, '', '#2');//금월 한달
	load_cgi(sy, sm, sd, ey, em, ed, '', '#3');//지난 30일간 통계
	load_cgi(ey, em, ed, ey, em, ed, '', '#4');//금일
//	load_cgi(ey-1, em, 0, ey, em, 0, '', '#6');//사용자 설정
//	load_cgi(ey-1, em, 0, ey, em, 0, '', '#7');
	var jv={kind : "pie"};
	$.post('pie.cgi', jv, function(data, status) {
		$('#5').html(data);
	});
	$('#kindd').change(function () {
		var jv2 = {kind: $("#kindd").text()};
		$.post('pie.cgi', jv2, function(data, status) {
			$('#5').html(data);
		})
	});
	$('#daterange1').daterangepicker(null, function(start, end, label) {
		console.log(start.toISOString(), end.toISOString(), label);
		var jv2 = {sy : String(start).split(" ")[3],
			sm : String(start).split(" ")[1],
			sd : String(start).split(" ")[2],
			ey : String(end).split(" ")[3],
			em : String(end).split(" ")[1],
			ed : String(end).split(" ")[2],
			file : "1.xlsx"};
		$.post('inzent.cgi', jv2, function(data, status) {
			data += "<a href='file/1.xlsx'>엑셀 파일 다운로드</a>";
			$('#6').html(data);
		})
	});
	$('#daterange2').daterangepicker(null, function(start, end, label) {
		console.log(start.toISOString(), end.toISOString(), label);
		var jv3 = {sy : String(start).split(" ")[3],
			sm : String(start).split(" ")[1],
			sd : String(start).split(" ")[2],
			ey : String(end).split(" ")[3],
			em : String(end).split(" ")[1],
			ed : String(end).split(" ")[2],
			file : "2.xlsx"};
		$.post('inzent.cgi', jv3, function(data, status) {
			data += "<a href='file/2.xlsx'>엑셀 파일 다운로드</a>";
			$('#7').html(data);
		})
	});
});

