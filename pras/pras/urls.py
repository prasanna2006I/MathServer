from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('surfaceareaofcylinder/',views.cylinarea,name="surfaceareaofcylinder"),
    path('',views.cylinarea,name="surfaceareaofcylinder")
]
