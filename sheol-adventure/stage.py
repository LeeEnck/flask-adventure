from flask import (
    Blueprint, render_template, request, g, session
)

bp = Blueprint('stage', __name__)

class Stage():
    stage_protocol = 'look around, save game, change current room, help'.upper()

    def __init__(self, name, desc, unique_command):
        self.name = name
        self.desc = desc
        self.unique_command = unique_command.upper()

@bp.route('/game/<stage_name>', methods=('GET', 'POST'))
def stage(stage_name):
    descriptions = {
        'hell': Stage('hell', 'This is the hell stage', 'Venture, '),
        'lavapit': Stage('lavapit', 'This is the lavapit stage', 'Spot the Plumbus',),
        'graveyard': Stage('graveyard', 'This is the graveyard stage', 'Explore',),
        'lavafalls': Stage('lavafalls', 'This is the lavafalls stage', 'Build a Raft',),
        'luciferslair': Stage('luciferslair','This is the luciferslair stage', 'Attack Lucifer',),
        'holygrail': Stage('holygrail', 'This is the holygrail stage', 'Flip the coin',)
        }

    if request.method == 'POST':
        action = request.form['action']

    return render_template('/game/stage.html',
                title=stage_name,
                stage_description=descriptions[stage_name].desc,
                stage_protocol=descriptions[stage_name].unique_command + descriptions[stage_name].stage_protocol
                )
