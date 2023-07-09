from .models import Pupil
from django.views import generic
from django.views import generic

from .models import Pupil


class PupilListViews(generic.ListView):
    model = Pupil
    template_name = 'pupils/pupil_list.html'
    context_object_name = 'pupils'  # default: object_list


class PupilDetailView(generic.DetailView):
    model = Pupil
    template_name = 'pupils/pupil_detail.html'
    context_object_name = 'pupils'  # default: object_list
