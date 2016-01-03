from django.utils import timezone
from django.views import generic
from .models import Question


class IndexView(generic.ListView):
    template_name = 'questions/index.html'
    context_object_name = 'latest_questions'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            created__lte=timezone.now()
        ).order_by('-created')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'questions/detail.html'
