

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Notes
from .serializers import NoteSerializer
from rest_framework import status


# Create your views here.

@api_view(['GET','POST'])

def get_notes(request):
    
    
     # GET — fetch all notes
    
    if request.method == 'GET':
            notes = Notes.objects.all()
            serializer = NoteSerializer(notes,many = True)
            return Response(serializer.data)
        
     # POST — create a new note
     
    if request.method == 'POST':
         serializer = NoteSerializer(data = request.data) # Step 1 - receive data
         
         
         if serializer.is_valid():  # Step 2 - validate
             serializer.save()
             return Response(serializer.data,status= status.HTTP_201_CREATED)  # Step 3 - save to DB
         
         else:
             return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
         
         
         
@api_view(['GET'])

def note_detail(request, pk):
    
    # Step 1 Finding the note in url /api/notes/1 2 3 ..
    
    try:
        note = Notes.objects.get(pk = pk)
    except Notes.DoesNotExist:
        return Response({"Error: Note not Found "}, status= status.HTTP_404_NOT_FOUND)
    
    #Step 2 Serialize it
    
    serializer = NoteSerializer(note)
    
    # Step 3 Return it 
    
    return Response(serializer.data)
       
                 
    
    
        
        
         
         
         
         
    


    
    
