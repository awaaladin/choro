from django.urls import path
from . import views


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('cart/', include('cart.urls', namespace='cart')),
#     path('', include('shop.urls', namespace='shop')),
# ]


app_name = 'shop'
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
    name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
    name='product_detail')]






