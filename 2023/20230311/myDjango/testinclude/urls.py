from django.urls import path
from . import views as testincludeview
urlpatterns =[
    path("testinclude/",testincludeview.useincludetest)
]