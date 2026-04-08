from django.urls import path

from . import  views

urlpatterns = [
    
    path('notes/', views.NoteList.as_view(), name= 'get-notes'),
    path('notes/<int:pk>/', views.NoteDetail.as_view(), name = 'note-detail')  # name = "note-detail" is a nickname used in place of the url 
   
    
]