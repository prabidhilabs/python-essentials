from rest_framework import serializers
from watchlist.models import Movie


#model serializer

class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    

    class Meta:
        model = Movie
        
        #for individual representation
        # fields = ['id', 'name', 'description']
        # exclude = ['active'] #exclude active and shows other things
        # exclude = ['name'] #exclude name and shows other
        fields = "__all__" #its represent all the element
        
    def get_len_name(self,object):
            length = len(object.name)
            return length
        
    
    def validate(self, data):
        if data['name']== data['description']:
            raise serializers.ValidationError("Title and description should be different")
        else:
            return data
    
    def validate_name(self, value):
        if len(value)<2:
            raise serializers.ValidationError("Name is too short!")
        else:
            return value
    
    
    
    
    
    
    

# #validators level validation
# def name_length(value):
#     if len(value)<2:
#         raise serializers.ValidationError("name is too short")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.data.get('name',instance.name)
#         instance.description = validated_data.data.get('description',instance.description)
#         instance.active = validated_data.data.get('active',instance.active)
#         instance.save()
#         return instance
        
#     #instance carries old values and validated_data 
#     #carries new values
    
#     #object level validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and description should be different")
#         else:
#             return data
    
    #field level validation
    # def validate_name(self, value):
    #     if len(value)<2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value