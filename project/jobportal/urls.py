from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_login', views.admin_login, name="admin_login"),
    path('user_login', views.user_login, name='user_login'),
    path('recruiter_login', views.recruiter_login, name='recruiter_login'),
    path('user_signup', views.user_signup, name='user_signup'),
    path('user_home', views.user_home, name='user_home'),
    path('log_out', views.log_out, name='log_out'),
    path('recruiter_signup', views.recruiter_signup, name='recruiter_signup'),
    path('recruiter_home', views.recruiter_home, name='recruiter_home'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('view_users', views.view_users, name='view_users'),
    path('delete_user/<int:pid>', views.delete_user, name='delete_user'),
    path('recruiter_pending', views.recruiter_pending, name='recruiter_pending'),
    path('recruiter_accept/<int:pid>', views.recruiter_accept, name='recruiter_accept'),
    path('recruiter_reject/<int:pid>', views.recruiter_reject, name='recruiter_reject'),
    path('recruiter_accepted', views.recruiter_accepted, name='recruiter_accepted'),
    path('recruiter_rejected', views.recruiter_rejected, name='recruiter_rejected'),
    path('all_recruiters',  views.all_recruiters, name='all_recruiters'),
    path('accept_recruiter/<int:pid>', views.accept_recruiter, name='accept_recruiter'),
    path('reject_recruiter/<int:pid>', views.reject_recruiter, name='reject_recruiter'),
    path('delete_recruiter/<int:pid>', views.delete_recruiter, name='delete_recruiter'),
    path('admin_password', views.admin_password, name='admin_password'),
    path('recruiter_password', views.recruiter_password, name='recruiter_password'),
    path('user_password', views.user_password, name='user_password'),
    path('create_job', views.create_job, name='create_job'),
    path('created_jobs', views.created_jobs, name='created_jobs'),
    path('edit_job/<int:pid>', views.edit_job, name='edit_job'),
    path('delete_job/<int:pid>', views.delete_job, name='delete_job'),
    path('latest_jobs', views.latest_jobs, name='latest_jobs'),
    path('user_latest_jobs', views.user_latest_jobs, name='user_latest_jobs'),
    path('job_details/<int:pid>', views.job_details, name='job_details'),
    path('apply/<int:pid>', views.apply, name='apply'),
    path('applications_generated', views.applications_generated, name='applications_generated'),
    path('applications_received', views.applications_received, name='applications_received'),
    path('contactus', views.contactus, name='contactus'),
    path('newsletter_subscribers', views.newsletter_subscribers, name='newsletter_subscribers'),
    path('delete_sub/<int:pid>', views.delete_sub, name='delete_sub'),
    path('resume_matcher', views.resume_matcher, name='resume_matcher')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)