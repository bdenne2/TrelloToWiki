from django.http import HttpResponse
import TrelloToWiki.management.commands.commands

def index(request):
    return HttpResponse(TrelloToWiki.management.commands.commands.GetBoardTasks(), content_type='text/plain')
