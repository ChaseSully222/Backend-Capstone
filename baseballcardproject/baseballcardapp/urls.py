from django.urls import include, path
from .views import *

app_name = "baseballcardapp"

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', home, name='home'),
    # path('main/', main, name='main'),
    path('players/', player_list, name='players'),
    path('sets/', set_list, name="sets"),
    # path('mycollection/', collection_list, name="mycollection"),
    path('logout/', logout_user, name='logout'),

]

