from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    avatar_image = serializers.ImageField(required=False)

    class Meta:
        model = Contact
        fields = '__all__'
        # fields = ['id','first_name','last_name','avatar_image','twitter_handle','avatar_url','note','created']

# toggle fave 


# class TodoToggleCompleteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Entry
#         fields = ['id']
#         read_only_fields = ['title', 'note', 'created_at', 'completed']
