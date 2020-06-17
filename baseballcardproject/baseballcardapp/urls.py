from django.urls import include, path
from .views import *

app_name = "baseballcardapp"

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('cards/', card_list, name='cards'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),

]

