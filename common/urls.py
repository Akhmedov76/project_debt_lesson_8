from django.urls import path

urlpatterns = [
    path('login/', login_user_view, name='login_user'),
    path('logout/', logout_user_view, name='logout_user'),
    path('register/', register_user_view, name='register_user'),
    path('user-profile/', user_profile_view, name='user_profile'),
    path('user/<int:pk>/', user_profile_edit_view, name='user_profile_edit'),
]
