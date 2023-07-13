from django.views import generic

from pupils.models import Pupil


class PupilListView(generic.ListView):
    model = Pupil
    template_name = 'pupil/pupil_list.html'
    context_object_name = 'pupils'

class PupilDetailView(generic.DetailView):
    model = Pupil
    template_name = 'pupil/pupil_detail.html'
    context_object_name = 'pupil' # ну
