from django.conf.urls import url #新增
from login import views
from django.contrib.auth import views as auth_views  # 使用django 自訂的auth_views

# myapps 應用底下的urls (地方)
# 嚴格匹配開頭結尾
# 因採用django 內建的auth_views 因此不用再呼叫到login 的 views ，只需填妥template
urlpatterns = [
	# url(r'^login/$', views.login, name='login'),  # 給模板呼叫 login url 並對應views的login
	url(r'^login/$', auth_views.LoginView.as_view(
		template_name='login/login.html'
	), name='login'),  # 使用內建login views 去呼叫模板
	url(r'^login$', views.dashboard, name='dashboard'),
	url(r'^logout/$', auth_views.LogoutView.as_view(
		template_name='login/logout.html'
	), name='logout'),  # 使用內建logout views 去呼叫模板
	url(r'^registration/$', views.registration, name='registration'),  # 使用者申請表單頁面
	url(r'^register_done/$', views.registration, name='register_done'),  # 使用者完成表單頁面
	url(r'^password_change/$', auth_views.PasswordChangeView.as_view(
		template_name='login/password_change.html'
	), name='password_change'),  # 使用內建更改密碼 去呼叫模板
	url(r'^password_change_done/$', auth_views.PasswordChangeDoneView.as_view(
		template_name='login/password_change_done.html'
	), name='password_change_done'),  # 使用內建 views 去呼叫模板
]