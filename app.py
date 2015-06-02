from flask import Flask,render_template
from helpers import assets_pipeline
import random
import markdown
import HTMLParser
import os

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
env = assets_pipeline.load_paths(app)
env = assets_pipeline.register_js_components(env)
env = assets_pipeline.register_css_components(env)
h = HTMLParser.HTMLParser()
global data
global lorem
global projects
global lorem_markdown

print "variables"

lorem = """
Lorem ipsum dolor sit amet, consectetur adipisicing elit.
Accusantium quod rem odio.
Repudiandae aliquam non vel voluptatibus,
ullam ipsum illo a.
Quos ut, eos libero pariatur optio reiciendis nam molestiae.
"""

lorem_markdown = """ 
# Gladios aguntur cuspide

## Austro eburno Themin

Lorem markdownum et [minus](http://www.reddit.com/r/haskell) conceperat multos
aspera Cyclopum peraget Iphin est Phoebus cum sed nuribusque viscera loqui Quid.
*Movit dare volucrum* aeratis. Tuae dirae Nam facta oppida vidimus fratrem
vastat Amphitrite umbra commota Lethes quaerit, fletumque prementem moly. Et
agmina [et](http://hipstermerkel.tumblr.com/), sustinet, tenens carpis pudorem
ignibus, Nonacrina Hippodamen alis perfusam! Erit patent optasse, motibus
tenebat cum omne patetis, tetigere Palladaque si addunt, sub.

## Precibus eiaculatus venatu

Comae *remissos* triumphos sagittas cumque! Patientia ad feror eiusdem, est,
cura nonne sequentes. Suo flentes non; *carentia properant* in miseram monte, ut
in pendentibus haec, nato, in. Saecula adspexit! **Et** Maeandros flenti
remissis reseratque, dea instabilemque [neve](http://www.uselessaccount.com/)
intexto colla, si substitit lumina.

1. Ore absit conditor
2. Alis sors sagitta gemitus enim mansit formam
3. Idem aditu
4. Fulvo constitit tibi postulat
5. Et tenetur in ingenua purpureum temerare latet

## Adspiciens coronant ramos

Dicta non, et **Atrides vulnus** Alcithoe Atlantis; puppim suas caelum. Aliter
non bacis fessos summo longa contra arte oculos modo ora sceleratae specus, dat
trabes. Vinclis qua prima coepit inmissos et primus at quae; erat gravitate
carina et tunc dives dissiluit gurgite [ut](http://www.wtfpl.net/) cernit. Canis
agat saxum neve bis tendo: et: erit, utque! Manus huc vos, animisque attonuit
munera; lumen *teneo*; cum et [oppida](http://eelslap.com/).

## Verba resonat huic dent iubet mihi signis

Corpore illius domitamque qualem de sui plaustri credis in, et audax quamquam
adhuc. Te genitor vernum! Restituit et nullo, in clivoque, nos verba, [exiluit
discordia](http://www.thesecretofinvisibility.com/) messes; est auctor. Veteres
abstulit serpens, ore cruentat cum pulchra altum fluminis forma excidit? Semine
rogos, ego non silentia frontes nubes Hyacinthe linguisque ensem.

## Iove exire sic non exspectatum et minores

**Adurat umbram** tunc nec virtute esses officio *potentia* agat, saxa est
sinit. Hac victor, legem iactu: ulla, cervice, omnes. Ignes non non nomine
stridit concepit mandata solum volucrisque floribus et linguam plumas, tum in.

> Adfuit dolentem Iuppiter fessa, et perde. Quia fuit triplices pendeat
> inritamen terrae illuc nitidaque, ergo parente sonus. Bis *custos*, Alba
> pastor **docendam**: nullus perque ardebant aliquid remansit sicut; te pennis.
> Tabellas sed *et illam lapillos* onus latique dea obliquo enim sed labefactus
> Cadmi non herbis levat fama regalia?

Quid tepentibus esse grata totidem enim subiti, nec Ityn demittere crimen
vetustis. Telaque sui clarum muneris adulterium figuris Andron ut ipsae et
castra ad Agenore. Manu **incubuit** Auguste gerenti ululatuque sensit habitura
idem! Nec passu, euntes, Nam longe ubi Iovis corporis mox succumbere
[illae](http://imgur.com/), bracchia nidus.

"""

print "Data"

lorem_markdown = h.unescape(markdown.markdown(lorem_markdown).replace('\n',''))

data = [
	{"title": "Overview"},
	{"title": "Education"},
	{"title": "Work Experience"},
	{"title": "Projects"},
	{"title": "Technical Skills"},
	{"title": "Contact"}
]

projects = [
	{"id": 1, "title": "Ovide", "description": lorem, "full_description": lorem_markdown},
	{"id": 2, "title": "The McCluskenator", "description": lorem, "full_description": lorem_markdown},
	{"id": 3, "title": "Comic Hunter", "description": lorem, "full_description": lorem_markdown},
	{"id": 4, "title": "Okay Lang", "description": lorem, "full_description": lorem_markdown},
	{"id": 5, "title": "Yo Cache", "description": lorem, "full_description": lorem_markdown},
	{"id": 6, "title": "Yo MIPS", "description": lorem, "full_description": lorem_markdown},
	{"id": 7, "title": "Custom Linux Distro", "description": lorem, "full_description": lorem_markdown}
	]

for item in data:
	item["text"] = lorem

print "begin app"

@app.route("/")
def index():
	print "root"
	return render_template('index.html')


@app.route("/bgcolor")
def get_background_color():
	r = lambda: random.randint(0,255)
	return '#%02X%02X%02X' % (r(),r(),r())

@app.route("/about")
def about_me():
	return render_template('about.html', data=data)


@app.route("/projects")
def projects_all():
	return render_template('projects.html', data=projects)

@app.route("/projects/<id>")
def projects_item(id):
	return render_template('project.html', data=projects[int(id)])


@app.route("/resume")
def get_resume():
	return render_template('resume.html')


if __name__ == "__main__":
    app.run(debug=True,port=int(os.environ['PORT']))
