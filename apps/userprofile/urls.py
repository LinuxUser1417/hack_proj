from django.urls import path
from . import views

urlpatterns = [
    path('user-profiles/', views.UserProfileListView.as_view(), name='user-profile-list'),
    path('user-profiles/<int:pk>/', views.UserProfileDetailView.as_view(), name='user-profile-detail'),

    path('carts/', views.CartListView.as_view({'get': 'list', 'post': 'create'}), name='cart-list'),
    path('carts/<int:pk>/', views.CartDetailView.as_view(), name='cart-detail'),

    path('favorites/', views.FavoriteListView.as_view({'get': 'list', 'post': 'create'}), name='favorite-list'),
    path('favorites/<int:pk>/', views.FavoriteDetailView.as_view(), name='favorite-detail'),

    path('order-history/', views.OrderHistoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='order-history-list'),
    path('order-history/<int:pk>/', views.OrderHistoryDetailView.as_view(), name='order-history-detail'),

]
