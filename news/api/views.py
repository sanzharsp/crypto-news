from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from news import models
from news.api import serializers

class ArticleListCreateAPIVew(APIView):
    
    def get(self, request):
        articles = models.Article.objects.filter(active=True)
        serializer = serializers.ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailView(APIView):
    
    def get_object(self, pk):
        article = get_object_or_404(models.Article, pk=pk)
        return article

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = serializers.ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = serializers.ArticleSerializer(article, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class JournalistListCreateAPIView(APIView):

    def get(self, request):
        journalist = models.Journalist.objects.all()
        serializer = serializers.JournalistSerializer(journalist,
                                                    many=True,
                                                    context={'request':request})
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.JournalistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JournalistDetaliAPIView(APIView):

    def get(self, request, pk):
        journalist = get_object_or_404(models.Journalist, pk=pk)
        serializer = serializers.JournalistSerializer(journalist,
                                                    context={'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        journalist = get_object_or_404(models.Journalist, pk=pk)
        serializer = serializers.JournalistSerializer(journalist, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        journalist = get_object_or_404(models.Journalist, pk=pk)
        journalist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','POST'])
# def article_list_create_api_view(request):
    
#     if request.method == "GET":
#         articles = models.Article.objects.filter(active=True)
#         serializer = serializers.ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = serializers.ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def article_detail_api_view(request, pk):
#     try:
#         article = models.Article.objects.get(id=pk)
#     except models.Article.DoesNotExist:
#         return Response({"error":{
#             "code": 404,
#             "message": "Article not found!"
#         }}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = serializers.ArticleSerializer(article)
#         return Response(serializer.data)

#     elif request.method == "PUT":
#         serializer = serializers.ArticleSerializer(article, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == "DELETE":
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)