from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('',views.home, name="Home"),
	path('Home',views.home, name="Home"),
	path('counterText/',views.counterTxt , name="countTxt"),
	path('counterFile/',views.counterFile , name="countFile"),
]
