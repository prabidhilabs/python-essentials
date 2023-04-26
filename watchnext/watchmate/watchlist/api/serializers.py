from rest_framework import serializers
from watchlist.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.data.get('name',instance.name)
        instance.description = validated_data.data.get('description',instance.description)
        instance.active = validated_data.data.get('active',instance.active)
        instance.save()
        return instance
        
    #instance carries old values and validated_data 
    #carries new values