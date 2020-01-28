from django.urls import path
from .import views


urlpatterns = [
    path('create/', views.create_student, name="create-student"),
    path('list/', views.student_list, name="student-list"),
    #path('search/', views.search_student, name="search-student"),
    path('sendall/', views.mailToall, name="send-all"),

    #path('edit/<int:student_id>', views.edit_student, name="edit-student"),

    path('edit/<int:student_id>/', views.edit_student, name="edit-student"),

    path('delete/<int:student_id>', views.delete_student, name="delete-student"),

    path('', views.home, name="home"),

    # account confirmation
    path('activate/<uid>/<token>/', views.activate, name='activate'),


]
