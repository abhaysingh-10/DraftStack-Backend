from django.urls import path

from . import  views

urlpatterns = [
    
    path('notes/', views.get_notes, name= 'get-notes'),
    path('notes/<int:pk>', views.note_detail, name = 'note-detail')  # name = "note-detail" is a nickname used in place of the url 
   
    
]