from django.shortcuts import render_to_response
from django.views.generic import *
from .models import *

# Create your views here.
#def poll_list(req):
    #polls =poll.objects.all()
    #return render_to_response('poll_list.html', {'items':polls})

class PollList(ListView):
    model= poll

class PollDetail(DetailView):
    model = poll

    def get_context_data(self, **kwargs):
        cxt = super().get_context_data(**kwargs)
        cxt['options'] = Option.objects.filter(poll_id=self.kwargs['pk']) 
        return cxt

class PollVote(RedirectView): 
    def get_redirect_url(self, *args, **kwargs):
        item = Option.objects.get(id=self.kwargs['oid'])
        item.count += 1
        item.save()
        return '/poll/'+str(item.poll_id)+'/' 

class PollCreate(CreateView):
    model = poll
    fields = ['title']
    success_url = '/poll/'
    