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

for item in about_data:
	data_item = about.About(
		title=item['title'],
		description=item['description'],
		bullets=item['bullets']
	)
	data_item.save()

print "Saved Data"