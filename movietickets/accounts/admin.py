from django.contrib import admin
from accounts.models import UserProfile,Movie,Theatre

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('user','user_info','city','website','phone','city',)
    def user_info(self,obj):
        return obj.description
    def get_queryset(self,request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('user')
        return queryset


class MovieAdmin(admin.ModelAdmin):
    list_display=('movie','image','sno','videofile')
    def get_queryset(self,request):
        queryset=super(MovieAdmin,self).get_queryset(request)
        return queryset


class TheatreAdmin(admin.ModelAdmin):
    list_display=('name','city','first','second','third')
    def get_queryset(self,request):
        queryset=super(TheatreAdmin,self).get_queryset(request)
        return queryset



admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Theatre,TheatreAdmin)