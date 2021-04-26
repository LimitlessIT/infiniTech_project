from django.http import Http404
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product, Category, Mark
from .serializers import ProductSerializers, CategorySerializers, MarkSerializers

class LatestProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[:4]
        serializers = ProductSerializers(products, many=True)
        return Response(serializers.data)

class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.get(category__slug=category_slug,slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializers(product)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug):
        category = self.get_object(category_slug)
        serializer = CategorySerializers(category)
        return Response(serializer.data)

class MarkDetail(APIView):
    def get_object(self, mark_slug):
        try:
            print(mark_slug)
            return Mark.objects.get(slug=mark_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, mark_slug):
        print(mark_slug)
        mark = self.get_object(mark_slug)
        serializer = MarkSerializers(mark)
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    print('tt')
    query = request.data.get('query', '')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializers = ProductSerializers(products, many=True)
        return Response(serializers.data)
    else:
        return Response({'products': []})
