from sito import app, db
from sito.models import Info, User


@app.shell_context_processor
def make_shell_context():
    return {'db': db,'User': User}  #per evitare di importare ogni volta nella SHELL FLASK db Post e User, ho scritto queste 3 righe
                                     #la shell di flask lho usate per creare lo User nella tabella User per poter accedere al sito
