
from django.urls import path
from . import views
from .views import (
    MyTokenObtainPairView,
    AuthUserRegistrationView,
    AuthUserLoginView,
    CompanyView,
    CompanyViewDetail,
    DepartmentView,
    DepartmentViewDetail,
    EmployeeView,
    EmployeeViewDetail,
    FileUploadView,
    UserListView,
    EmployeeUploadView
)

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    #path('profile/', views.get_profile),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('company/', CompanyView.as_view()),
    path('company/<int:pk>/', CompanyViewDetail.as_view()),

    path('departments/', DepartmentView.as_view()),
    path('departments/<int:pk>/', DepartmentViewDetail.as_view()),

    path('files/', FileUploadView.as_view()),
    path('emp-files/', EmployeeUploadView.as_view()),


    path('employees/', EmployeeView.as_view()),
    path('employees/<int:pk>/', EmployeeViewDetail.as_view()),

    path('users/', UserListView.as_view()),

    path('register', AuthUserRegistrationView.as_view(), name='register'),
    path('login', AuthUserLoginView.as_view(), name='login'),
    # path('users', UserListView.as_view(), name='users')
]


