

from rest_framework.response import Response
from rest_framework.decorators import api_view #for function based views  
from .models import Notes
from .serializers import NoteSerializer
from rest_framework import status  # for status code 
from rest_framework.views import APIView # for class based  views
from rest_framework import viewsets







            
            
            
class NoteViewSet(viewsets.ViewSet):
    
    # GET get all notes /api/notes
    def list(self,request):
        note = Notes.objects.all()
        serializer = NoteSerializer(note,many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    
    # POST create note /api/notes
    def create(self,request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    # GET single note /api/notes/1 2 3 4...
    def retrieve(self,request,pk = None):
        try:
            note = Notes.objects.get(pk = pk)
        except Notes.DoesNotExist:
            return  Response({"error ":"Note Not Found"},status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
     # PUT update note  /api/notes/1/
    def update(self,request,pk=None):
        try:
            note = Notes.objects.get(pk = pk)
        except Notes.DoesNotExist:
            return Response({"Error":"Note Not Found"},status = status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #PATCH update partial /ai/notes/1
    def partial_update(self,request,pk=None):
        try:
            note = Notes.objects.get(pk = pk)
        except Notes.DoesNotExist:
            return Response({"Error":"Note Not Found"},status = status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note,data = request.data ,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    #Delete delete the note /api/notes/1 2 3
    def destroy(self,request,pk = None):
        try:
            note = Notes.objects.get(pk = pk)
        except Notes.DoesNotExist:
            return Response({"Error":"Note Not Found"},status= status.HTTP_404_NOT_FOUND)
        note.delete()
        return Response({"Message":"Note Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
         
          
        
    
    
    
    
             

            
        
        