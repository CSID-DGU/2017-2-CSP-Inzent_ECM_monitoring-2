var gr_cgi = 'inzent.cgi';
var free_cgi = 'pie.cgi';
var real_cgi = 'realtime.cgi';
function load_cgi(sy_, sm_, sd_, ey_, em_, ed_, file, id) {
	var jv = {sy : sy_, sm : sm_, sd : sd_, 
			  ey : ey_, em : em_, ed : ed_, fn : file};
	$.post(gr_cgi, jv, function(data,status) {
		$(id).html(data);
	});
}

function free() {
	var jv={kind : "pie"};
	$.post(free_cgi, jv, function(data, status) {
		$('#5').html(data);
	});
}

Date.prototype.addDays = function(days) {
    var dat = new Date(this.valueOf());
    dat.setDate(dat.getDate() + days);
    return dat;
}
function update(n) {
	$.get(real_cgi, function(data, status){});
	$('#0').css('background-image', "url('file/" + n + ".png')")
	.css('background-position', '12%')
	.animate({'background-position-x':'90%'}, 30000, 'linear', function() {
		update((n+1)%2);
	});
}
$(document).ready( function() {      
	var today=new Date();
	var ey = today.getFullYear();
	var em = today.getMonth();
	var ed = today.getDate();
	var prev = today.addDays(-30);
	var sy = prev.getFullYear();
	var sm = prev.getMonth();
	var sd = prev.getDate();
	load_cgi(ey-1, em, 0, ey, em, 0, '', '#1');//���� 12���������
	load_cgi(ey, em, 0, ey, em, 0, '', '#2');//�ݿ� �Ѵ�
	load_cgi(sy, sm, sd, ey, em, ed, '', '#3');//���� 30�ϰ� ���
	load_cgi(ey, em, ed, ey, em, ed, '', '#4');//����
	load_cgi(ey-2, em, 0, ey-1, em, 0, '', '#6');//����� ����
	load_cgi(ey-1, em, 0, ey, em, 0, '', '#7');
	free();
	//$.get(free_cgi, function(data) { });
	$('#kindd').change(function () {
		var jv2 = {kind: $(":selected").text()};
		$.post(free_cgi, jv2, function(data, status) {
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
		$.post(gr_cgi, jv2, function(data, status) {
			data += "<a href='file/1.xlsx'>���� ���� �ٿ�ε�</a>";
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
		$.post(gr_cgi, jv3, function(data, status) {
			data += "<a href='file/2.xlsx'>���� ���� �ٿ�ε�</a>";
			$('#7').html(data);
		})
	});
	//inzent_cgi();
	update(0);
});