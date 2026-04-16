

from rest_framework.response import Response
from rest_framework.decorators import api_view #for function based views  
from .models import Notes
from .serializers import NoteSerializer
from rest_framework import status  # for status code 
from rest_framework.views import APIView # for class based  views
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner # Custom Permissions








            
            
            
class NoteViewSet(viewsets.ViewSet):
    

    authentication_classes =[TokenAuthentication]
    permission_classes =[IsAuthenticated , IsOwner] # custom permission 
    
   
        
   
        
    
    # GET get all notes /api/notes
    def list(self,request):
        note = Notes.objects.filter(user=request.user) # filter by logged in user 
        
        # Filtering the notes
        
        #request.query_params → this is a dictionary of everything after ? in the URL
        # .get look for a key called search, if not found return None

        search = request.query_params.get('search',None)
        
        # if search → only filter if user actually sent a search word
        # title__icontains=search → this is a Django ORM lookup __ double underscore
        if search:
            # | OR checking if the title contains or the content contains the value 
            note = note.filter(title__icontains=search) | note.filter(content__icontains=search) 
         
         #Adding the date field for Filtering    
        date = request.query_params.get('date',None)
        
        if date:
            note = note.filter(created_at__date=date)
            
            
        serializer = NoteSerializer(note,many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    
    # POST create note /api/notes
    def create(self,request):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user) # automatically set owner
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    # GET single note /api/notes/1 2 3 4...
    def retrieve(self,request,pk = None):
        try:
            # note = Notes.objects.get(pk = pk,user = request.user) #check user owner
            note = Notes.objects.get(pk =pk)
            self.check_object_permissions(request,note) #check user 
        except Notes.DoesNotExist:
            return  Response({"error ":"Note Not Found"},status=status.HTTP_404_NOT_FOUND)
        serializer = NoteSerializer(note)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
     # PUT update note  /api/notes/1/
    def update(self,request,pk=None):
        try:
            #custom permission
            note = Notes.objects.get(pk=pk)
            self.check_object_permissions(request,note) 
        
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
            #custom permission 
            note = Notes.objects.get(pk=pk)
            self.check_object_permissions(request,note)
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
            #custom permission
            note = Notes.objects.get(pk=pk)
            self.check_object_permissions(request,note)
        except Notes.DoesNotExist:
            return Response({"Error":"Note Not Found"},status= status.HTTP_404_NOT_FOUND)
        note.delete()
        return Response({"Message":"Note Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)
    
    
         
'''
     #helper function for custom permissions 
    
    def get_object(self,request,pk):
        try:
            note = Notes.objects.get(pk=pk)
            self.check_object_permissions(note)
            return note
        except Notes.DoesNotExist:
            return None
    now in the retrieve update partial update and destroy function 
    we can use instead of 
    this -> note = Notes.objects.get(pk =pk)
            self.check_object_permissions(request,note) #check user 
            
    to this -> def retrieve(self, request, pk=None):
                   note = self.get_object(request, pk)
                   if not note:
                   return Response({"error": "Note Not Found"}, status=404)

                   serializer = NoteSerializer(note)
                   return Response(serializer.data)
'''    
        
    
    
    
    
             

            
        
        