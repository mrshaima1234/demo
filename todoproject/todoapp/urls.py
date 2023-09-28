from django.urls import path
from . import views

urlpatterns = [
    path('', views.add,name='add'),
   # path('details/', views.details,name='details'),
   path('delete/<int:taskid>', views.delete,name='delete'),
   path('update/<int:taskid>', views.update,name='update'),
   path('cdvhome/', views.TaskListview.as_view(),name='cdvhome'),
   path('cbvdetails/<int:pk>', views.TaskDetailstview.as_view(),name='cbvdetails'),
   path('cbvupdate/<int:pk>', views.TaskUpdatetview.as_view(),name='cbvupdate'),
   path('S/<int:pk>', views.TaskDeleteView.as_view(),name='cbvdelete'),


]