from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    avatar_image = serializers.ImageField(required=False)

    class Meta:
        model = Contact
        fields = '__all__'
        # fields = ['id','first_name','last_name','avatar_image','twitter_handle','avatar_url','note','created']


# toggle fave
class ToggleFaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['favorite']
        read_only_fields = ['id', 'first_name', 'last_name',
                            'avatar_image', 'twitter_handle', 'avatar_url', 'note', 'created', 'avatar_image']
