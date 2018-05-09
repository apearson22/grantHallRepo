from django.urls import path

from . import views

app_name='granthall'

urlpatterns = [
	path('', views.index, name='home'),
	#path('dataentry', views.dataEntry, name='dataEntry'),
	#path('dataquery', views.dataQuery, name='dataQuery'),
	#path('help', views.help, name='help'),
	path('additem', views.additem, name='additem'),
	path('showitems', views.showitems, name='showitems'),
]
