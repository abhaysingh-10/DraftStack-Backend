from rest_framework import serializers
from .models import Notes,SubTask


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id','title','completed']
        
class NoteSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many= True,read_only=False) # nested Serializer subtask field 
    
    class Meta:
        model =Notes
        fields = ['id','title','content','created_at','subtasks']
        read_only_fields = ['id','created_at']
        
    
    def create(self,validated_data):
       
        # Step1  pull out subtasks data from validated_data
        subtasks_data = validated_data.pop('subtasks',[])
        
        # Step 2 create the Note first
        note =Notes.objects.create(**validated_data)
        
        #  Step 3 — loop through subtasks and create each one
        for subtask in subtasks_data:
            SubTask.objects.create(note=note,**subtask)
            
        return note
    


        
        
    
    