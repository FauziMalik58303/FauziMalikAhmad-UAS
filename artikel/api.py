from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from artikel.models import ArtikelBlog
from artikel.serializers import ArtikelBlogSerializer

@api_view(['GET'])
def api_artikel_blog_list(request):
    artikel = ArtikelBlog.objects.all()
    serializer = ArtikelBlogSerializer(artikel, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def api_artikel_blog_tambah(request):
    data = request.data.copy()



    serializer = ArtikelBlogSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Artikel berhasil di tambahkan",
            "data": serializer.data
            }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            "message": "Gagal menambahkan artikel",
            "errors": serializer.error_messages
        }, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def api_artikel_blog_update(request, id_artikel):
    artikel = get_object_or_404(ArtikelBlog, id=id_artikel)

    data = request.data.copy()
    serializer = ArtikelBlogSerializer(isinstance=artikel, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Artikel berhasil di diperbarui",
            "data": serializer.data
            }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            "message": "Gagal memperbaruin artikel",
            "errors": serializer.error_messages
        }, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['DELETE'])
def api_artikel_blog_delete(request, id_artikel):
    try:
        artikel = get_object_or_404(ArtikelBlog, id=id_artikel)
        artikel.delete()
        content = {
            "message": "artikel succes didelete"
        }
        status_code = status.HTTP_200_OK
    except:
        content = {
            "message" : "artikel gagal didelete"
        }
        status_code = status.HTTP_400_BAD_REQUEST
        return Response(content, status=status_code)