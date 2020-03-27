from flask import (
    Blueprint, render_template, request, g, session
)

bp = Blueprint('stage', __name__)

class Stage():
    stage_protocol = ' search, checkpoint/save, change current room, help'.upper()

    def __init__(self, name, desc, unique_command):
        self.name = name
        self.desc = desc
        self.unique_command = unique_command.upper()

@bp.route('/game/<stage_name>', methods=('GET', 'POST'))
def stage(stage_name):
    descriptions = {
        'hell': Stage('hell', """You have been sent to hell for your vulger and dispicable behavior.
               You can venture into the hellish boundaries.
               You can curl up into a ball and weep""", 'Venture or weep,'),

        'lavapit': Stage('lavapit', """You have now arrived at the lava pit, and see a
              giant plumbus levitating""", 'take it, leave it, punt it',),

        'graveyard': Stage('graveyard', """You have approached the graveyard of the banished
              and now you must choose what to do next. Either ignore
              the graveyard and continue on, or go into the undead land.""", 'Explore',),

        'lavafalls': Stage('lavafalls', """You feel the unwrenching heat of the lavafalls ahead and now have to overcome
               the largest obstacle that you have yet to discover. """, 'Build a Raft or alternate route',),

        'luciferslair': Stage('luciferslair', """You fought through much of what Hell has to offer but now you
              must approach the demonic entity himself. While feeling his presence
              since you have arrived you feel a cold touch to your shoulder.""", 'Attack Lucifer hand to hand combat or throw holy water',),

        'holygrail': Stage('holygrail', """You spoken his forsaken name and have also flipped the coin in the air.
              At first nothing happens, then all of a sudden you start falling into what seems like an endless black hole. Then
              you awake sweaty and cold in a hospital bed, free of the shackles of Hell.
              Congrats on proving your stoic perseverance as an individual especially
              against the cruel unwrenching being Lucifer!""", 'Flip the coin',)
        }

    if request.method == 'POST':
        action = request.form['action']

    return render_template('/game/stage.html',
                title=stage_name,
                stage_description=descriptions[stage_name].desc,
                stage_protocol=descriptions[stage_name].unique_command + descriptions[stage_name].stage_protocol
                )
