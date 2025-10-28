from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['who'] = 'World'
        return context




def about(reuqest):
    return render(
        reuqest,
        'about.html',
    )