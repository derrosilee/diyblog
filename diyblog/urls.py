from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [
    path('blog/', include('blog.urls'))
]
