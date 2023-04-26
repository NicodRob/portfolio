from flask import Flask, render_template, request, redirect
import os
import csv

app = Flask(__name__)

def write_in_txtfile(data):
	with open('database.txt', mode='a') as database:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n {email},{subject},{message}')


def write_in_csvfile(data):
	with open('database.csv', mode='a') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csvfile = csv.writer(database2,delimiter=';',quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csvfile.writerow([email,subject,message])

@app.route("/")
def hello_world():
#	print(url_for('static', filename='ninjafavicon.ico'))
    return render_template('index.html')

@app.route("/<string:name_page>")
def genericpage(name_page):
    return render_template(name_page)

@app.route('/form-completed', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_in_csvfile(data)
		return redirect('/thankyou.html')
	else:
	    return 'Something went wrong, try again!'


# @app.route("/index.html")
# def index():
#     return render_template('index.html')

# @app.route("/works.html")
# def works():
#     return render_template('works.html')


# @app.route("/about.html")
# def about():
#     return render_template('about.html')

# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')

# @app.route("/components.html")
# def components():
#     return render_template('components.html')

# @app.route("/work.html")
# def work():
#     return render_template('work.html')