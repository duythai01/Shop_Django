from django.urls import path, include
from rest_framework import routers

from product import views

router = routers.DefaultRouter()
router.register("categories", views.CategoryViewSet, 'category')
router.register("products", views.ProductViewSet, 'product')
router.register("products", views.ProductDetailViewSet, 'tag')
router.register("search", views.SearchViewSet, 'search')



urlpatterns = [
    path('', include(router.urls)),

]