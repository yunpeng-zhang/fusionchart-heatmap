https://www.fusioncharts.com/dev/getting-started/django/your-first-chart-using-django

https://www.fusioncharts.com/django-charts?framework=django

1 django create project
2 cd project folder
3 django create app
4 create app/static/app folder and copy over fusioncharts.py from the fusionchart package
5 update settings.py to include djangoapp
6 update settings.py to include static path
7 views.py to prepare the data
8 create app/urls.py
9 update project/urls.py
10 in views.py
make sure of using the following
from .static.heatmapchart.fusioncharts import FusionCharts
11 python manage.py runserver
no need of the following as the data is static not from database
python manage.py makemigrations
python manage.py migrate


