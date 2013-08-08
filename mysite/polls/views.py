from django.http import HttpResponse, Http404

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")
def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p})
def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)
def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)

