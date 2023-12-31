from django.urls import path 
from study_spaces_app import views



app_name = 'study_spaces_app'

urlpatterns = [
    path('', views.HomePage, name='HomePage'),
    path('login',views.login_user,name = "Login"),
    path('signup',views.register,name = "Signup"),
    path('logout', views.logout_view, name='Logout'),
    path('user-management',views.user_management,name="userManagement"),
    path('change-details',views.change_account_details,name="changeDetails"),
    path('addPost', views.create_post, name="createPost"),
    path('Library', views.category_library, name='category_library'),
    path('Cafe', views.category_cafe, name='category_cafe'),
    path('Other Place', views.category_other, name='category_other'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),




    
]
