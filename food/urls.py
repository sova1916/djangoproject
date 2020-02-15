from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('', views.IndexclassView.as_view(), name='index'),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    #add
    path('add',views.CreateItem.as_view(), name='create_item'),
    #edit
    path('update/<int:id>/',views.update_item, name="update_item"),
    path('delete/<int:id>/',views.delete_item, name="delete_item"),

]