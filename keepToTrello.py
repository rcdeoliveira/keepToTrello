import gkeepapi
import os
from trello import TrelloApi

username = os.getenv('GUSERNAME')
mtoken = os.getenv('GMTOKEN')
noteId = os.getenv('GNOTEID')
trelloApiToken = os.getenv('TAPITOKEN')
trelloApikey = os.getenv('TAPIKEY')
trelloListId = os.getenv('TLISTID')


# Google kepp connections
keep = gkeepapi.Keep()
keep.resume(username, mtoken, sync=True)


# Trello connection
trello = TrelloApi(trelloApikey)
trello.set_token(trelloApiToken)

# Get note
note = keep.get(noteId)

# No content? Exit
if len(note.items) == 0:
    exit(0)
else:
    for index in range(len(note.items)):
        task = note.items.pop()
        newCard = trello.cards.new(task.text, idList=trelloListId)
        task.delete()

    keep.sync()

exit(0)
