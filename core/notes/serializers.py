from rest_framework import serializers

from .models import Notes

# Using .ModelSerializer
class NoteSerializer(serializers.ModelSerializer):
    
    id = serializers.IntegerField(read_only = True)
    title = serializers.CharField(max_length = 200)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    
    
    
    class Meta:
        model = Notes                                     # WHICH MODEL TO USE 
        fields = ['id','title','content','created_at']    # WHICH FIELD TO CHOOSE
        read_only_fields = ['id','created_at']
        
        
    
    

# another way to add  traditional method .Serializer
  
# class NoteSerializer(serializers.Serializer)
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=200)
#     content = serializers.CharField()
#     created_at = serializers.DateTimeField(auto_now_add=True)
    
