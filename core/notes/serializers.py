from rest_framework import serializers
from .models import Notes,SubTask


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ['id','title','completed']
        
class NoteSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many= True,read_only=True) # nested Serializer subtask field 
    
    class Meta:
        model =Notes
        fields = ['id','title','content','created_at','subtasks']
        read_only_fields = ['id','created_at']
        
    
    