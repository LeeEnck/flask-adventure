from flask import (
    Blueprint, render_template, request, g, session
)

bp = Blueprint('stage', __name___)

@bp.route('game/<stage_name>')
def stage(stage_name):
    descriptions = {
        'hell': 'This is the hell stage.',
        'lavapit': 'This is the lavapit stage.',
        'graveyard': 'This is the graveyard stage.',
        'lavafalls': 'This is the lavafalls stage.',
        'luciferslair': 'This is the luciferslair stage.',
        'holygrail': 'This is the holygrail stage.'
    }

    return render_template('game/stage.html',
                title=stage_name,
                stage_description=descriptions[stage_name]
                )
