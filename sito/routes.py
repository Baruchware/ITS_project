
from flask import render_template, redirect, flash, url_for  #importo funzioni per gestire le routes
from flask_login import current_user, login_user, logout_user  #importo funzioni riguardanti il login
from sito import app, db , led #importo l'applicazione, l istanza del database e le funzioni del led
from sito.forms import LoginForm #importo il form del login scritto in python
from sito.models import Info, User #importo le tabelle del database





@app.route("/")
def homepage():
    return render_template("homepage1.html") 

@app.route("/table")
def table():
    a = Info.query.all()
    return render_template("table.html", a = a)

@app.route("/control/reset")
def tablereset():
    a = db.session.query(Info).delete()
    y = db.session.commit()
    return render_template("control.html", a = a, y = y)

@app.route("/control")
def control():

    return render_template("control.html")

@app.route("/control/accendi")
def controlon():
    on = led.accendi()

    return render_template("control.html", on=on)

@app.route("/control/spegni")
def controloff():
    off = led.spegni()

    return render_template("control.html",off=off)

@app.route("/control/analisi")
def controlanalisi():
    analisi= led.analisi()

    return render_template("control.html", analisi = analisi)


@app.route("/login", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:  #se un utente gia autenticato riprova a entrare nel login
        return redirect(url_for('homepage'))   #viene reindirizzato alla funzione homepage
    form = LoginForm()          #creo variabile chiamando la funzione LoginForm di froms.py
    if form.validate_on_submit():    #se il form e stato convalidato premendo ok
        user = User.query.filter_by(username=form.username.data).first()   # si crea variabile, nella quale si cerca nel DB se il suo username IDENTICO esiste, dovrebbe essere dato dal primo risultato se esiste!
        if user is None or not user.check_password(form.password.data): # se lo user non esiste (valore None) oppure se la password fornita non combacia
            flash('Username e password non combaciano!')   #stampa questa stringa nella pagina
            return redirect(url_for('login'))    #e rimanda l utente al login
        login_user(user, remember=form.remember_me.data) #possibilità di ricordare l utente
        return redirect(url_for('homepage'))  #MANDA ALL HOMEPAGE LOGGATO
    return render_template('login.html', form=form)  #se non sei autenticato vieni mandato qui, da notare render_template!



@app.route("/logout")
def logout():
    logout_user()   #disconnette l utente
    return redirect(url_for('homepage'))   #e lo rimanda alla fase di login ( magari per cambiare account)



@app.route("/AboutUs")
def about_us():
    return render_template('about_us.html')
