

from rest_framework.response import Response
from rest_framework.decorators import api_view #for function based views  
from .models import Notes
from .serializers import NoteSerializer
from rest_framework import status  # for status code 
from rest_framework.views import APIView # for class based  views



class NoteList(APIView):
    
    # GET - fetch all notes 
    def get(self,request):
        note = Notes.objects.all()
        serializer = NoteSerializer(note,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    #POST - Create a note. recieve data --> validate --> save in db 
    def post(self,request):
        serializer = NoteSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

# Handles - /api/notes/1 2 3../   
class NoteDetail(APIView):
    
    #helper function for finding note exists or not  used by all methods inside Note Detail
    def get_object(self,pk):
        try:
            return Notes.objects.get(pk = pk)
        except Notes.DoesNotExist:
            return None
        
    # GET - return single note
    
    def get(self,request,pk):
          note = self.get_object(pk) # helper function call
          if note == None:
              return Response({"Error ":"Note Not Found"},status=status.HTTP_404_NOT_FOUND)
          else:
              serializer = NoteSerializer(note)
              return Response(serializer.data,status=status.HTTP_200_OK)
    
    #PUT - update entire note 
    
    def put(self, request,pk):
        note = self.get_object(pk)
        if note ==None:
            return Response({"Error":"Note Not Found"},status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = NoteSerializer(note,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
            
    # PATCH - Partial Update 
    
    def patch(self,request,pk):
        note = self.get_object(pk)
        if note==None:
            return Response({"Error": "Note Not Found"},status = status.HTTP_404_NOT_FOUND)
        else:
            serializer = NoteSerializer(note,data = request.data,partial = True) 
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status = status.HTTP_200_OK)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
   
   # DELETE - Delete the note           
   
    def delete(self,request,pk):
        note = self.get_object(pk)
        if note == None:
            return Response({"Error":"Note not Found"},status=status.HTTP_404_NOT_FOUND)
        else:
            note.delete()
            return Response({"Message":"Note Delete Successfully"},status=status.HTTP_204_NO_CONTENT)     
            
            
            
             
            

            
        
        