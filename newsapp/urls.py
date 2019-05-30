from django.urls import path, include
from .views import *
from .models import *
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'newsapp'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
  	path('editorpanel/', EditorPanelView.as_view(), name='editorpanel'),
    path('editorpanel/news/list', EditorNewsListView.as_view(), name='editornewslist'),
    path('editorpanel/category/list', EditorCategoryListView.as_view(), name='editorcategorylist'),

    path('editorpanel/news/create',
         EditorNewsCreateView.as_view(), name='editornewscreate'),
    path('editorpanel/category/create',
         EditorCategoryCreateView.as_view(), name='editorcategorycreate'),
 #    path('adminpanel/news/<int:pk>/update',
 #         AdminPostUpdateView.as_view(), name='adminnewsupdate'),
 #    path('adminpanel/news/<int:pk>/delete',
 #         AdminPostDeleteView.as_view(), name='adminnewsdelete'),
	 path('editorpanel/category',
         EditorCategoryListView.as_view(), name='editorcategorylist'),
 #    path('adminpanel/category/create',
 #         AdminCategoryCreateView.as_view(), name='admincategorycreate'),
 #    path('adminpanel/category/<int:pk>/update',
 #         AdminCategoryUpdateView.as_view(), name='admincategoryupdate'),
 #    path('adminpanel/category/<int:pk>/delete',
 #         AdminCategoryDeleteView.as_view(), name='admincategorydelete'),
    path('news/create/', NewsCreateView.as_view(), name='newscreate'),
    path('news/<int:pk>/detail/', NewsDetailView.as_view(), name='newsdetail'),
    path('news/list/', NewsListView.as_view(),
         name='newslist'),
    path('api-token-auth/', obtain_auth_token, name= 'api_token_auth'),

    path('category/list/', CategoryListView.as_view(),
         name='categorylist'),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='newsupdate'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='newsdelete'),
    path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='categoryupdate'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='categorydelete'),
    path('category/<int:pk>/', CategoryDetailView.as_view(),
         name="categorydetail"),


    path('weather/', WeatherView.as_view(), name='weather'),
    path('addcity/', CityCreateView.as_view(), name='citycreate'),
    path('sample/', SampleView.as_view(), name='sample'),
    path('rest-auth/', include('rest_auth.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]