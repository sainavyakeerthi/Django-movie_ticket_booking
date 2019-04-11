from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from movietickets import views
app_name='accounts'
app_name='home'
urlpatterns = [
    url(r'^$',views.Login_redirect,name='login_redirect'),
    url('admin/', admin.site.urls),
    url(r'^accounts/',include(('accounts.urls'),namespace='accounts'),name='accounts'),
    url(r'^home/',include(('home.urls'),namespace='home'),name='home'),


    url(r'^', include('django.contrib.auth.urls'))
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
