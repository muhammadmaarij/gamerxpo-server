from xpoarena.views import booth, stripe_webhook_view, create_checkout_session, update_booth, games, theme, customizedBooth, user_details, update_booth_customization, update_game, login_view, signup, google_login, update_user_and_profile, register_organization, verify_auth, user_information, get_usernames, update_user_details, get_organization_details, update_organization, get_user_id, update_user_profile_with_organization, get_organization_id_from_userprofile, get_user_organization_id, get_organization_details_by_id, join_organization, update_organization_in_user_profile, get_developers, remove_user_from_organization, get_games_by_booth_and_genre
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('booth/', booth),
    path('booth/<int:booth_id>', update_booth),
    path('games/<str:title>', update_game),
    path('games/', games),
    path('theme/', theme),
    path('customizedbooth/', customizedBooth),
    path('customizedbooth/<int:pk>/', update_booth_customization),
    path('login/', login_view, name='custom_login'),
    path('signup/', signup, name='custom_signup'),
    path('google_login/', google_login, name='google_login'),
    path('userdetails/', user_details, name='user_details'),
    path('setprofile/', update_user_and_profile, name='update_user_profile'),
    path('registerorganization/', register_organization, name='register_organization'),
    path('verify/', verify_auth, name='verify'),
    path('userinformation/', user_information, name='user_information'),
    path('usernames/', get_usernames, name='get_usernames'),
    path("updateuser/", update_user_details, name='update_user_details'),
    path("organization/", get_organization_details, name='get_organization_details'),
    path("updateorganization/", update_organization, name='update_organization'),
    path("getuserid/", get_user_id, name='user_id'),
    path("updateuserprofilewithorganization/<int:user_id>/", update_user_profile_with_organization, name='update_organization'),
    path("getorganizationid/<int:user_id>/", get_organization_id_from_userprofile, name='get_organization'),
    path("userorganization/", get_user_organization_id, name='update_organization'),
    path("organizationbyid/<int:org_id>/", get_organization_details_by_id, name='organizationbyid'),
    path('joinorganization/', join_organization, name='join-organization'),
    path('updateorganizationinuserprofile/', update_organization_in_user_profile, name='update-organization-in-user-profile'),
    path('getdevelopers/', get_developers, name='get-developers'),
    path('removeuserfromorg/<int:user_id>/', remove_user_from_organization , name='remove-user-from-organization'),
    path('webhook/', csrf_exempt(stripe_webhook_view),
         name='stripe-webhook'),
   
    path('create-checkout-session/<int:pk>/',
         csrf_exempt(create_checkout_session), name='create-checkout-session'),
     
     path('getgamesbybooth/', get_games_by_booth_and_genre, name='get-gamesby-booth-and-genre'),





]
