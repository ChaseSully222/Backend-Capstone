from django.urls import include, path
from .views import *

app_name = "baseballcardapp"

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/form', register_form, name='register_form'),
    path('home/', home, name='home'),
    path('main/', main, name='main'),
    path('players/', player_list, name='players'),
    path('players/form', player_form, name='player_form'),
    path('players/<int:playerId>/', player_details, name='players'),
    path('sets/', set_list, name="sets"),
    path('sets/form', set_form, name='set_form'),
    path('sets/<int:set_id>/', set_details, name='set'),
    path('card/', card_list, name="card"),
    path('card/form', card_form, name='card_form'),
    path('card/<int:card_id>/', card_details, name='card'),
    path('mycollection/', collection_list, name="mycollection"),
    path('mycollection/<int:collection_id>/', collection_details, name="collection_details"),
    path('mycollection/<int:collection_id>/form/', collection_edit_form, name="collection_edit_form"),
    path('logout/', logout_user, name='logout'),
    

]

