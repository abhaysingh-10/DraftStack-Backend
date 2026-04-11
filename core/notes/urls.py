from django.urls import path ,include 
from rest_framework.routers import DefaultRouter # for the viewset class 
from . import views


# urlpatterns = [
    
#     path('notes/', views.NoteList.as_view(), name= 'get-notes'),
#     path('notes/<int:pk>/', views.NoteDetail.as_view(), name = 'note-detail')  # name = "note-detail" is a nickname used in place of the url 
   
    
# ]


# Step 1 creating object of DefaultRouter Class
router = DefaultRouter()

# Step 2 Register the ViewSet
router.register('notes',views.NoteViewSet,basename='notes')

# Step 3 Include router url
urlpatterns =[
    
    path('',include(router.urls))
    
]


