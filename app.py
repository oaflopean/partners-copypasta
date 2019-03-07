from flask import *
import ebooklib
from pymongo import MongoClient
from mongoengine import *
import json

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
app = Flask(__name__)
app.config["SECRET_KEY"]= 'my super secret key'.encode('utf8')

connect("partners", host='178.128.171.115', port=27017, username="oaflopean", password="99bananas", authentication_source="admin")
conn = MongoClient(host='178.128.171.115',port=27017)
db = conn['partners']
collection = db['Entries']

# Data to serve with our API
class Entry(Document):
    first=StringField()
    last=StringField()
    title=StringField()
    date=StringField(primary_key=True)
def read_all():
    return json.dumps(db.Entries.find())
    # Create the list of people from our data

class Name(FlaskForm):
    name = StringField('name', validators=[DataRequired()])


@app.route('/')
def home():
    form = Name()
    if form.validate_on_submit():
        return redirect('/hello/')
    json=[{"first":"Caesar","last":"Naples","title":"Shell", "desc":"We all live with inner demons; his are coming out."}]
    return render_template('home.html', entries=json, form=form)

@app.route('/header')
def index():
    return render_template('header.html')


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

@app.route('/hivemind23')
def hivemind():
    return render_template("m1Vr4.html")

@app.route('/projects/')
def projects():
    return render_template("selfpublishing.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/mcoaflopean')
def twitter_embed():
    return render_template("oaflopean.html")

@app.route('/hello/', methods=["GET"])
@app.route('/hello/<name>')
def hello(name=None):
    phrases = "alien dimension 2, mentally ill could possibly avoid, alien owner mind control abilities, pseudopod algae rippled eagerly, never became fully aware, mental powers beyond imagining, dimension 2 helped, skidded among ice, get regular people, fixed income due, entire situation completely, emotions ran high, constant existential crisis, mind control chemical, second alien hiding, successful man used, would never become, near bed time, boy would follow, substance never left, become successful like, dimension 2, man sought treatment, self control, mental caves, alien hid, alien continued, second chemical, never knew, never ate, could shoot, could see, could keep, different alien, powers kicked, highest powers, become rich, worked like, leg like, behave like, real man, man suspected, man insane, man continued, truck came, taking medication, suffered deeply, seek communion, quite entertained, leadership potential, godly path, french fries, eyes unless, every day, ever accept, eventually learn, dug deep, dim parts, different chemical, devilish predilection, deeply disturbed, commonly taxed, boy struggled, boy came, antennae stuck, affected strangely, 300 metres, 0clock news, lived like, private life, weak excuse, smoke tobacco, result encouraged, really wanted, made money, fractal design, coordination ability, business management, life pond, mind, effect allowed, alien, become, man, treatment, time, substance, boy, life, different, weak, tobacco, really, pond, made, lived, encouraged, effect, design, business, allowed, ability, writing, woods, wise, ways, understanding, truth, thought, target, supplied, success, stocks, spirits, soul, something, seemed, secretly, secret, revolutionary, reveal, results, psychotic, profit, prick, predict, power, point, order, notably, none, mysteriously, much, moments, met, mcdonald, marketplace, marijuana, managed, long, living, leader, impairment, however, house, home, hated, god, friends, forms, form, flew, field, father, explanation, expected, existence, entrap, enriching, enhance, encountering, efforts, easy, drawings, dosed, dominate, devoted, devil, despite, demons, deeper, dealer, creativity, controlled, consciousness, confused, conflict, children, child, cameras, calm, brain, bewildered, art, angels, aliens, age, advantages, 9, 5, 20, 18,".join(", ")
    json2={"first":"Caesar","last":"Naples","title":"Shell", "desc":"We all live with inner demons; his are coming out."}
    return render_template('hello.html', entries=json2,phrases=phrases, name=name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")



@app.route('/entries')
@app.route('/entries/all')
def entries():
    strange={"first":"Marc","last":"Shapiro","title":"Stories of High Strangeness", "desc":'<a href="https://www.copypastapublishing.com" class="black-text"> <img class="hoverable" style="height:50px; width:50px", src="{{url_for("static", filename="lowerlogo.png")}}"></img></a>'}

    return render_template('results.html', entry=strange)

if __name__ == '__main__':
    app.run(debug=True)