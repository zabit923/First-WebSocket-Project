from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from users.views import profile_view
from chat.views import chat_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', chat_view, name="home"),
    path('profile/', include('users.urls')),
    path('@<username>/', profile_view, name="profile"),
    path('chat/', include('chat.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
