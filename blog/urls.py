from django.urls import path
from .views import PostDetailView

app_name = 'blog'

urlpatterns = [
    # The <slug:slug> part captures the text from the URL and passes it to the View
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]