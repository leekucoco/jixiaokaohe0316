layui.use(['form'], function() {
	var form = layui.form;
	var $ = layui.jquery;
	checkLogin();
	//提交
	form.on('submit(LAY-user-login-submit)', function(obj) {
		// obj.field.verkey = codeKey;
		layer.load(1);
		console.log(obj.field)
		$.post("/login/", obj.field, function(data) {
			console.log(data)
			if (data) {
				layer.msg(data.msg,{icon: 1});
				localStorage.setItem("token", data.token);
				//localStorage.setItem("user", JSON.stringify(data.user));
				setTimeout(function() {
					location.replace("/laybackground/");
				}, 2000);
			} else {
				layer.closeAll('loading');
				layer.msg(data.msg,{icon: 2});
			}
		}, "json");
	});

	// getCode();  //获取验证码
	// $("#LAY-user-get-vercode").click(function(){
	// 	getCode();
	// });
});

//获取验证码
// var codeKey = null;
// function getCode(){
// 	if(codeKey==null){
// 		codeKey = guid();
// 	}
// 	$("#LAY-user-get-vercode").attr("src","image/captcha?codeKey="+codeKey+"&n="+Math.random());
// }

//检查是否登录
function checkLogin(){
	var token = localStorage.getItem("token");
	if (token != null) {
		location.replace("/index/");
	}
}

//生成uuid
// function guid() {
//     function S4() {
//        return (((1+Math.random())*0x10000)|0).toString(16).substring(1);
//     }
//     return (S4()+S4()+"-"+S4()+"-"+S4()+"-"+S4()+"-"+S4()+S4()+S4());
// }