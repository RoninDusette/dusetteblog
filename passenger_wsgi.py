import sys, os
INTERP = "/home/djyoshabyd/Django/envs/DusetteBlog/bin/python"
#INTERP is present twice so that the new Python interpreter knows the actual executable path
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/blog.dusette.net')  #You must add your project here

os.environ['DJANGO_SETTINGS_MODULE'] = "dusetteblog.settings_production"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()