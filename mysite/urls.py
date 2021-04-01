
from django.contrib import admin
from django.urls import path, include
from blog import views
from products import views as p_views
from sophomore import views as s_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin-login/', admin.site.urls),    
    path('about/',views.about,name='about'),
    path('payment/',views.testform, name='payment'),
    path('confirm/<int:pay_id>/',views.post, name ='post'),
    path('test/',p_views.testp, name='test'),
    path('sophomore/',s_views.sopoh, name='sophomore')  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
    