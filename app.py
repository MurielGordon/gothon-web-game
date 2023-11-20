from flask import Flask, session, redirect, url_for, request 
from flask import render_template
from gothonweb import planisphere



app = Flask(__name__)

@app.route("/")
def index():
    session['room_name'] = planisphere.START
    session['count'] = 0
    return redirect(url_for("game"))

@app.route("/game", methods=['GET', 'POST'])
def game():
    room_name = session.get('room_name')

    if request.method == "GET":
        if room_name:
            room = planisphere.load_room(room_name)
            return render_template("show_room.html", room=room)
    
    else: 
        action = request.form.get('action')    
    
        if room_name and action:
            room = planisphere.load_room(room_name)
            next_room = room.go(action)

        if not next_room and action == '':
            session['room_name'] = planisphere.name_room(room)

        #elif not next_room and room_name == 'laser_weapon_armory' and session['count'] < 9:
        #    session['count'] += 1
            #stay = (request.form.get('action') != '666')
        #    next_room = room.go('stay')
        #    session['room_name'] = planisphere.name_room(next_room)

        elif not next_room:
            next_room = room.go('*')
            session['room_name'] = planisphere.name_room(next_room)    

        else:
            session['room_name'] = planisphere.name_room(next_room)
        
    return redirect(url_for("game"))    
    

# DELETE BEFORE PUSH
app.secret_key = '*****'

if __name__ == "__main__":
    app.debug = True
    app.run()