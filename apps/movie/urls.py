from django.urls import path
from . import views as movieViews

urlpatterns = [
    path('', movieViews.home, name='home'),
    path('<int:movie_id>/', movieViews.detail, name='detail'),
    path('<int:movie_id>/create', movieViews.createreview, name='createreview'),
    path('review/<int:review_id>', movieViews.updatereview, name='updatereview'),
    path('review/<int:review_id>/delete', movieViews.deletereview, name='deletereview')]
