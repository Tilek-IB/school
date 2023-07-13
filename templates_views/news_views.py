from django.views import generic
from news.models import New
class NewsListView(generic.ListView):
    model = New
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 2

    def get_queryset(self):
        return New.objects.all().order_by('-created_at')