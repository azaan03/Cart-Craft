from django.urls import path,reverse_lazy
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm,ChangePasswordForm,CustomPasswordResetForm,CustomSetPasswordForm

urlpatterns = [
    path('', views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>', views.Product_detail.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    #password change URL
    path('changepassword/', auth_views.PasswordChangeView.as_view(
        template_name='app/changepassword.html',
        form_class=ChangePasswordForm,
        success_url=reverse_lazy('password_change_done')
    ), name='changepassword'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(
        template_name='app/passwordchangedone.html'
    ), name='password_change_done'),
    #password reset URL
    path('password-reset/', auth_views.PasswordResetView.as_view(
             template_name='app/password_reset.html',
             form_class=CustomPasswordResetForm
        ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
    template_name='app/password_reset_done.html'
        ), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    template_name='app/password_reset_confirm.html',
    form_class=CustomSetPasswordForm
        ), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
    template_name='app/password_reset_complete.html'
        ), name='password_reset_complete'),

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>/', views.mobile, name='mobiledata'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<str:data>/', views.laptop, name='laptopdata'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),    
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
