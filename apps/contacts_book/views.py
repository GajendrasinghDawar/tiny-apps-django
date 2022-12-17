from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework import filters
from django.db.models import Q

from .models import Contact
from .serializers import ContactSerializer, ToggleFaveSerializer

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

class ToggleFaveComplete(generics.UpdateAPIView):
    serializer_class = ToggleFaveSerializer
    # queryset = Contact.objects.all()

    def get_queryset(self):
        print(self.request.query_params)
        # return Contact.objects.filter(pk=self.kwargs['pk'])
        return Contact.objects.filter(pk=self.kwargs.get('pk'))

    def perform_update(self, serializer):
        serializer.instance.favorite = not (serializer.instance.favorite)
        serializer.save()
