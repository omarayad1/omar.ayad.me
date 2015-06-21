from mongoengine import connect
from models import projects, about
from models.reference_fields import links, markdown_file, technologies
import os

connect(host=os.environ['MONGOLAB_URI'])

print "Connected"

print "Init About data"
about_data = [
	{
		"title":"Overview",
		"description":"Over 5 years of web developing/designing experience and"
					"strong technical and programming skills."
					" Fast learner with love of web application development,"
					" data analysis and classical music.",
		"bullets": [
			"Developed some open-source projects",
			"Contributed to several open-source projects",
			"Worked closely with several start-ups",
			"Developed full-stack web applications to several startups"
		]
	},
	{
		"title": "Education",
		"description": "I am currently studying for my Bachelor degree"
						" in Computer Science in The American University in Cairo"
						" and graduating in 2016",
		"bullets": [
			"The American University in Cairo . Class of 2016: B.Sc. Computer Science"
		]

	},
	{
		"title": "Work Experience",
		"description": "I have interned in several companies"
						" and freelanced with several companies. "
						"please see the resume for more info",
		"bullets": [
			"IBM . Software Engineering Intern . Jul 2014 - Aug 2014",
			"CivilSoft . Front-end Web Developer Intern . Nov 2013 - Feb 2014"
		]
	},
	{
		"title": "Projects",
		"description": "I developed several projects both "
						"University projects and independent open-source projects."
						" I also developed freelance projects for startups",
		"bullets": [
			"please visit the <a href='/projects'>projects</a> page to know more"
		]
	}
]

projects_data = [
		{
			"name": "Verilog Web IDE/Simulator",
			"link": "http://ovide.ayad.me",
			"github": [
				"http://github.com/omarayad1/ovide-core",
				"http://github.com/omarayad1/ovide-api",
				"http://github.com/omarayad1/ovide-web"
			],
			"technologies": [
				"Python 2.7",
				"RabbitMQ",
				"Node.js",
				"Sails.js",
				"Postgres",
				"Backbone.js:"
			],
			"description": "Experimental Verilog Web Editor and simulator divided into three main modules; the core module written in python and communicates with the api module (written in Node.js) through a message queue server which communicates with the frontend module (constructed with backbone.js)",
			"md": "mcclusky.md"
		},
		{
			"name": "Quine McCluskey Circuit Drawer",
			"link": "http://mcclusky.ayad.me/",
			"github": [
				"http://github.com/omarayad1/The-McCluskenator"
			],
			"technologies": [
				"Python 2.7",
				"Flask",
				"Coffeescript",
				"Backbone.js",
				"Joint.js"
			],
			"description": "Given the terms of the boolean function, minimizes the boolean function and draws the circuit."
		},
		{
			"name": "Cache Simulator",
			"github": [
				"http://github.com/omarayad1/Yo-Cache"
			],
			"technologies": [
				"Coffeescript",
				"Ember.js",
				"D3.js",
				"NodeWebkit",
				"Node.js"
			],
			"description": "Simulates User Defined Types of Caches and automatically presents live Graphs."
		},
		{
			"name": "MIPS Disassembler/Simulator",
			"github": [
				"http://github.com/omarayad1/Yo-MIPS"
			],
			"technologies": [
				"Python 2.74",
				"Qt4.8",
				"Pyside"
			],
			"description": " Disassembles Binary MIPS files and Simulates The Product."
		},
		{
			"name": "Linux CLI OS",
			"description": "Built and assembled a linux OS from source using existing open source packages (kernel, awk, glibc ... etc) without using existing Linux Distros."
		},
		{
			"name": "Comic Hunter",
			"github": [
				"http://github.com/omarayad1/Comic-Hunter"
			],
			"technologies": [
				"Python 2.7",
				"BeautifulSoup",
				"Requests"
			],
			"description": "Scrapes Popular web comic series like xkcd, cyanide & happiness and the oatmeal."
		},
		{
			"name": "Big Data Analysis",
			"technologies": [
 				"Hadoop",
 				"Mapreduce",
 				"Pig",
 				"Java",
 				"R",
 				"ggplot"
			],
			"description": "Using a Local installation of Hadoop and Pig analysed some properties of an approximately 375 GB of data and plotted it using R."
		},
		{
			"name": "Digit Recognizer",
			"technologies": ["R"],
			"description": "Using existing training datasets and K-Nearest Neighbours Algorithm, trained a model to recognize a handwritten digit with an average precision of 0.94."
		}
	]

for item in about_data:
	data_item = about.About(
		title=item['title'],
		description=item['description'],
		bullets=item['bullets']
	)
	data_item.save()

for item in projects_data:
	github_items = []
	technologies_items = []
	md = None
	link_item = None
	if 'link' in item:
		link_item = links.Links(link=item['link']).save()
	if 'github' in item:
		for link in item['github']:
			github_items.append(links.Links(link=link).save())
	if 'technologies' in item:
		for technology in item['technologies']:
			technologies_items.append(technologies.Technologies(technology=technology).save())
	if 'md' in item:
		md_doc = open('static/md/'+item['md'], 'rb')
		data = md_doc.read()
		data.replace('/n','//n')
		md = markdown_file.MarkdownFile(data)
		md.save()
	data_item = projects.Projects(
		name=item['name'],
		description=item['description'],
		link = link_item,
		github = None if github_items == [] else github_items,
		technologies = None if technologies_items == [] else technologies_items,
		markdown = [md]
	)
	data_item.save()
print "Saved Data"