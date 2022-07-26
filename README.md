# djangoweb
web site use Django platform
### Steps to make Django project
<ul>
<li><code>pip install django</code></li>
<li><code>django-admin startproject taskmanager</code></li>
<li><code>cd taskmanager</code></li>
<li><code>python manage.py runserver</code> - runserver (127.0.0.1:8000)</li>
<li><code>python manage.py startapp main</code> - create main app
<pre>taskmanager->settings.py write 'main'
     <code>
     INSTALLED_APPS = [
          'django.contrib.admin',
          'django.contrib.auth',
          'django.contrib.contenttypes',
          'django.contrib.sessions',
          'django.contrib.messages',
          'django.contrib.staticfiles',
          'main'
      ]
      </code>
</pre></li>
<li><code>Write in 'taskmanager/urls.py'</code>
     <pre><code>
     from django.contrib import admin
     from django.urls import path,include
     urlpatterns = [
         path('admin/', admin.site.urls),
         path('', include('main.urls')),
     ]
     </code></pre></li>
<li><code>Create 'urls.py' in 'main'</code>
     <pre>taskmanager->main->urls.py
     <code>
          from django.urls import path
          from . import views
          urlpatterns = [
              path('',views.index)
          ]
      </code>
     </pre></li>
<li><code>Create folder 'templates/main' in main</code></li>
<li><code>Create file 'templates/main/index.html' in main</code></li>
<li><code>Write in 'main/views.py'</code>
     <pre><code>
     from django.shortcuts import render
          def index (request):
               return render (request,'main/index.html')
     </code></pre></li>
<li><code></code></li>
<li><code></code></li>
<li><code></code></li>
</ul>
