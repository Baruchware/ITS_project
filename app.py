from sito import app, db
from sito.models import Info, User


@app.shell_context_processor
def make_shell_context():
    return {'db': db,'User': User}