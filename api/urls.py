from django.urls import path
from . import views

urlpatterns = [
    # path('', views.apiView, name='views.apiView'),
    path('product-list/', views.showAll, name='product-list'),
    path('product-detail/<int:pk>/', views.viewProduct, name='product-detail'),
    path('product-create/', views.createProduct, name='product-create'),
    path('product-update/<int:pk>/', views.updateProduct, name='product-update'),
    path('product-delete/<int:pk>/',views.deleteProduct, name='product-delete')
]
