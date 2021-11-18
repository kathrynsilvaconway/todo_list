from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="list" ),
    path('update_job/<int:job_id>', views.update_job, name="update_job" ),
    path('delete_job/<int:job_id>', views.delete_job, name="delete_job" )
]
