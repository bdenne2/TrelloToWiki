from django.core.management.base import BaseCommand, CommandError
import trello 
from TrelloToWiki.models import Token

def GetBoardTasks():
    #get authorized, and grab board tasks
    apiKey = Token.objects.filter(name='apiKey')[0]
    userToken = Token.objects.filter(name='bryUserToken')[0]

    trelloClient = trello.TrelloClient(api_key=apiKey.token,token=userToken.token)
    boardBoard = trelloClient.get_board('6UJ7RvZg')

    lists = boardBoard.open_lists()
    dictionary = dict()
    wikiMarkup = ''

    for trelloList in lists:
        taskNames = []
        wikiMarkup +=  '* Trello {0} \n'.format(trelloList.name)

        for x in trelloList.list_cards():
            taskNames.append(x.name)
            wikiMarkup += '** {0} - \n'.format(x.name)
        dictionary[trelloList.name] = taskNames
        wikiMarkup += '\n'
    return wikiMarkup

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'


        #get the list name, put in as key
        #get this list's list of task names, put in as value

#    def ConvertTasksToWiki(self, dictionary):
#        wikimarkup = ''
#        for k,v in dictionary.iteritems():
#            listOf
#            wikiMarkup = '{0} \n * {1} \n ** {2}'.format()
        #get the Tasks, iterate to convert to wiki, output
        #TrelloClient.get_Board(). Just hard code the board id.
        #Board.get_lists(). Iterate over all of the boards and print out ("Trello {0}", boardName ).
        #List.list_cards(). Iterate over all of the cards and print out the ("{0} - ", cardName).
