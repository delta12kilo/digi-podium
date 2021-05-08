
from django.contrib import admin
from django.urls import path, include
from blog import views
from products import views as p_views
from sophomore import views as s_views
from django.conf.urls.static import static
from django.conf import settings
from enroll import views as e_views


urlpatterns = [
    path('admin-login/', admin.site.urls),    
    path('',views.about,name='about'),
    path('payment/',views.testform, name='payment'),
    path('confirm/<int:pay_id>/',views.post, name ='post'),
    # path('test/',p_views.testp, name='test'),
    path('test/',include('products.urls', namespace='npro')),
    path('sophomore/',s_views.sopoh, name='sophomore'),
    path('test-view/',e_views.test_view, name='test-view')  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
    