import gkeepapi
import os
from trello import TrelloApi

username = os.getenv('GUSERNAME')
password = os.getenv('GPASSWORD')
noteId = os.getenv('GNOTEID')
trelloApiToken = os.getenv('TAPITOKEN')
trelloApikey = os.getenv('TAPIKEY')
trelloBoardId = os.getenv('TBOARDID')


# Google kepp connections
keep = gkeepapi.Keep()
keep.login(username, password)


# Trello connection
trello = TrelloApi(trelloApikey)
trello.set_token(trelloApiToken)

# Get note
note = keep.get(noteId)
items = note.text.replace('☐ ', '')

# No content? Exit
if len(note.items) == 0:
    exit(0)
else:
    for index in range(len(note.items)):
        task = note.items.pop()
        newCard = trello.cards.new(task.text, idList=trelloBoardId)
        task.delete()

    keep.sync()

exit(0)
