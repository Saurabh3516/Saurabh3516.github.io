from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('movies', views.movies, name="Movies"),
    path('cinemas', views.halls, name="Cinemas"),
    path('detail/<int:item>', views.detail, name="detail"),
    path('mysaved', views.mysaved, name="MyBucket"),
    path('register', views.register, name="Register"),
    path('login', views.login, name="Login"),
    path('logout', views.logout, name="Logout"),
    path('book/<int:item>', views.book, name='book'),
]