from django.contrib import admin
from django.urls import path

from drf_tutorial.user.views import UserViewSet

urlpatterns = [
    path('admin/', admin.site.urls),

    # User
    path('users', UserViewSet.as_view({'post': 'create'}), name='user-register'),  # 회원가입
    path('users/login', UserViewSet.as_view({'post': 'login'}), name='user-login'),  # 로그인
    path('users/<int:pk>', UserViewSet.as_view({'get': 'retrieve'}), name='user-retrieve'),  # 사용자 조회
]
