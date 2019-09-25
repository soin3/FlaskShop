/**
 * Created by solin on 2019/9/24.
 */

;
var user_login_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $("#jsLoginBtn").click( function(){
            var btn_target = $(this);
            if( btn_target.hasClass("disabled") ){
                common_ops.alert("正在处理!!请不要重复提交~~");
                return;
            }

            var login_name = $("#login_name").val();
            var login_pwd = $("#login_pwd").val();
            console.log(login_name,login_pwd)

            if( login_name == undefined || login_name.length < 1){
                common_ops.alert( "请输入正确的登录用户名~~" );
                return;
            }
            if( login_pwd == undefined || login_pwd.length < 1){
                common_ops.alert( "请输入正确的密码~~" );
                return;
            }
            btn_target.addClass("disabled");
            $.ajax({
                url:common_ops.buildUrl("/user/login"),
                type:'POST',
                data:{ 'login_name':login_name,'login_pwd':login_pwd },
                dataType:'json',
                success:function(res){
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if( res.code == 200 ){
                        callback = function(){
                            window.location.href = common_ops.buildUrl("/");
                        }
                    }
                    common_ops.alert( res.msg,callback );
                }
            });
        } );
    }
};

$(document).ready( function(){
    user_login_ops.init();
} );
