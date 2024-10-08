from django.contrib import admin
from django.urls import path

from drf_tutorial.user.views import UserViewSet
from drf_tutorial.memo.views import MemoViewSet

urlpatterns = [
    path('admin/', admin.site.urls),

    # User
    path('users', UserViewSet.as_view({'post': 'create'}), name='user-register'),  # 회원가입
    path('users/login', UserViewSet.as_view({'post': 'login'}), name='user-login'),  # 로그인
    path('users/<int:pk>', UserViewSet.as_view({'get': 'retrieve'}), name='user-retrieve'),  # 사용자 조회

    # Memo
    path('memos', MemoViewSet.as_view({'post': "create", "get": "list"})),  # 메모 생성 / 조회
    path('memos/<int:pk>', MemoViewSet.as_view({"put": "update", "delete": "destroy"}))  # 메모 업데이트 / 삭제
]
