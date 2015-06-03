import markdown
import HTMLParser

def convert(markdown_data):
	h = HTMLParser.HTMLParser()
	return h.unescape(markdown.markdown(markdown_data).replace('\n',''))
