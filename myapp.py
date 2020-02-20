import urllib
from bs4 import BeautifulSoup
import json

from flask import Flask, url_for, Response
app = Flask(__name__)


def get_course_data():
    courses = {}
    url = "http://labfiles.linuxacademy.com/python/scraping/courses.html"
    html_data = urllib.urlopen(url).read()
    soup = BeautifulSoup(html_data,"lxml")
    sections = soup.find_all('a', attrs={'class':'col-xs-12 p-x-0 library-content-box-container content-aws'})
    for section in sections:
        title =  section.find('span', attrs={"class":"library-content-title"})
        length = section.find('span', attrs={"class":"library-content-length"})
        url = section['href']
        html_data = urllib.urlopen(url).read()
        instructor = BeautifulSoup(html_data,"lxml").find_all('span', attrs={"class":"instructor-name"})
        courses[title.text]={ 'intructor' : instructor[0].text,
                              'url' : url,
                              'length': length.text}
    return courses


courses = get_course_data()

@app.route('/')
def information():
    return """ This application gives information about the Linux Academy courses by webscraping and returning the output as JSON """

@app.route('/courses')
def all_courses():
    js = json.dumps(courses, sort_keys=True, indent=4,)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

@app.route('/course/<coursename>')
def course_detail(coursename):
    js = json.dumps(courses[coursename], sort_keys=True, indent=4,)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0')
