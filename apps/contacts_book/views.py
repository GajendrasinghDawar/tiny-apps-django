from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework import filters
from django.db.models import Q

from .models import Contact
from .serializers import ContactSerializer

class ContactsList(generics.ListCreateAPIView):
    search_fields = ['first_name', 'last_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # parser_classes = (MultiPartParser, FormParser,JSONParser)
    parser_classes = [MultiPartParser, FormParser,JSONParser]

    # def get_queryset(self):
    #     queryset = Contact.objects.all()
    #     search = self.request.query_params.get('search')
    #     print(search)
    #     if search is not None:
    #         print('searchig ')
    #         queryset = queryset.filter(Q(first_name=search) | Q(last_name=search) )
    #     return queryset


class ContactsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    # parser_classes = (MultiPartParser, FormParser,JSONParser)
    parser_classes = [MultiPartParser, FormParser,JSONParser]


# make toggle for fave button 

# class TodoToggleComplete(generics.UpdateAPIView):
#     serializer_class = TodoToggleCompleteSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user
#         return Entry.objects.filter(user=user)

#     def perform_update(self, serializer):
#         serializer.instance.completed = not (serializer.instance.completed)
#         serializer.save()
