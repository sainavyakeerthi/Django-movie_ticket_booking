from django.conf.urls import url
from home import views
app_name='home'
urlpatterns =[
    url(r'^$',views.homeview,name='home'),
    url(r'^movieview/(?P<pk>\d+)/$',views.movie_view,name='movie_view_pk'),

    url(r'^movieview/(?P<pk>\d+)/first/$',views.first_show_view,name='first_show'),
    url(r'^movieview/(?P<pk>\d+)/first/book/(?P<theat>\D+)/$',views.book_first,name='book_first'),


    url(r'^movieview/(?P<pk>\d+)/second/$',views.second,name='second_show'),
    url(r'^movieview/(?P<pk>\d+)/second/book/(?P<theat>\D+)/$',views.book_second,name='book_second'),


    url(r'^movieview/(?P<pk>\d+)/third/$',views.third,name='third_show'),
    url(r'^movieview/(?P<pk>\d+)/third/book/(?P<theat>\D+)/$',views.book_third,name='book_third'),



]