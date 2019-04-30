
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from service.models import services
from .serializers import servicesSerializer
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView



class servicesCreateListView(APIView):
    lookup_field = 'pk'
    serializer_class = servicesSerializer
    #queryset = services.object.all()

    def get(self,request):
        serviceslist = services.objects.all()
        serializer = servicesSerializer(serviceslist, many=True)
        return Response(serializer.data)

    def post(self,request):
        #serviceslist = services.objects.create()
        serializer = servicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response({'status': 'Servicio creado correctamente'})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class servicesRetrieveUpdateDestroyView(APIView):
    lookup_field = 'pk'
    serializer_class = servicesSerializer
    queryset = services.objects.all()

    def get(self,request,pk=None):
        servicesobj = services.objects.filter(pk=pk)[0]
        serializer = servicesSerializer(servicesobj)
        return Response(serializer.data)

    def delete(self,request,pk=None):
        servicesobj = services.objects.get(pk=pk)
        servicesobj.delete()
        return Response(status=204)

    def put(self,request,pk=None):
        servicesobj = services.objects.get(pk=pk)
        serializer = servicesSerializer(servicesobj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            #return Response({'status': 'Servicio actualizado correctamente'})
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #def list_queryset(self):
     #   list= services.objects.all()
      #  listserializer=servicesSerializer(list, many=True)
       # return Response(listserializer.data)

    #def get_object(self):
     #   pk= self.kwargs.get("pk")
      #  return services.objets.get(pk=pk)
