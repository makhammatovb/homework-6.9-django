from django.urls import path
from .views import pupils_list, pupils_detail

urlpatterns = [
    path('pupils/', pupils_list, name='pupils_list'),
    path('pupils/<int:id>/', pupils_detail, name='pupil_detail')
]