from django.urls import path
from myapp import views
urlpatterns = [
    #path('<top_name>/',views.index,name="index"),
    path('image/',views.image_upload,name="forms"),
]
