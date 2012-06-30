import logging
from django.views.generic import TemplateView
from django.conf import settings
import pdb


class HelloWorld(TemplateView):
    template_name = "hello-world.html"
    
    def get(self, request, *args, **kwargs):
        self.request.session['message'] = 'Sessions seem okay!'
        return super(HelloWorld, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HelloWorld, self).get_context_data(**kwargs)
        context['message'] = self.request.session.get('message', None)
        return context


def exception_test(request):
    logging.debug('Debug log')
    logging.warn('Warn log')
    logging.error('Error log')
    raise Exception()
    


    
