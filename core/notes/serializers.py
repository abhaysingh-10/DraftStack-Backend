from rest_framework import serializers
from .models import Notes,SubTask


class SubTaskSerializer(serializers.ModelSerializer):
    id =serializers.IntegerField(required = False)
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
    
    def update(self,instance,validated_data):
        
        # Step 1 — separate subtasks from note data
        subtasks_data = validated_data.pop('subtasks',[])
        
        # Step 2 — update the note fields
        instance.title = validated_data.get('title',instance.title)
        instance.content = validated_data.get('content',instance.content)
        instance.save()
        
        # Step 3 — get ids from request
        new_ids = [s.get('id')for s in subtasks_data if s.get('id')]
        
        # Step 4 — delete subtasks not in request
        for subtask in instance.subtasks.all():
            if subtask.id not in new_ids:
                subtask.delete()
        
        # Step 5 -  update or create subtasks
        for subtask_data in subtasks_data:
            subtask_id = subtask_data.get('id',None)
            if subtask_id:
                subtask = SubTask.objects.get(id = subtask_id,note=instance)
                subtask.title=subtask_data.get('title',subtask.title)
                subtask.completed =subtask_data.get('completed',subtask.completed)
                subtask.save()
            else:
                SubTask.objects.create(note =instance,**subtask_data)
        
        return instance
    
    
                
            

        
        
    
    