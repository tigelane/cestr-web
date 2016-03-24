#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

import menu_items
import sys, re, requests, json, os
from datetime import datetime

# Blue - color:#2C63D5
# Bright Green - color:#00FC00

headers = {'Content-type': 'application/json'}
app_port = '5000'
app_addr = os.getenv('APP_SERVER_IPADDR', '127.0.0.1')
print " * APP Server: {0}".format(app_addr)

def build_menu():
	menu_info = my_menu()
	html = screen_header(menu_info['width'])
	html += menu_info['menu']
	return html

def screen_header(width):

	html = menu_items.complex_black_style(width)

	html += '''
		<head>
		<meta charset="utf-8">
		<center>
			<img src="http://tigelane.com/graphics/blue_space-header3.jpg">
			<title style="color:#BDBDBD">
			Simple three tier blog program</title>
		</center>
		</head>

		<body>
			<center>
			<style>
				body {background-color:#000000;}
				br {style-color:#BDBDBD"}
			</style>
			<h2 style="color:#BDBDBD">
			Simple three tier blog program</h2>
			</center>
			<br>
		'''

	return html

def my_menu():
	html = '''
			<center>
			<ul id="menu">
				<li><a href="/">Home</a></li>
				<li><a href="server_info">Server Test</a></li>
				'''

	html += '<li><a href="/initialize_db">Initialize DB</a></li>'
	html += '<li><a href="/show_all_records">Show Records</a></li>'
	html += '<li><a href="/add_record">Add a Record</a></li>'
	html += '<li><a href="/remove_db">Remove Database</a></li>'

	html += '''

				</li>
			</ul>
			</center>
		'''


    # Manual length of all the letters in the menu (including spaces) 
    # multiplied by "16" to give us a decent length for the menu
	width = 52.0 * 16
	return {'menu': html, 'width': width}


@app.route('/initialize_db')
def initialize_db():
	html = build_menu()
	html += '''<center>
		<BODY style="color:#BDBDBD"><H3>--Initializing the Database--</H3>
		<br>
		'''

	url = 'http://{0}:{1}/initialize_db'.format(app_addr, app_port)

	try: 
		result = requests.get(url)
	except:
		html += '''	<H3>Application Server Failure</H3>
					<p>
					'''
		html += 'Not able to communicate with Application Server at {0}.<b><br>'.format(app_addr)
		return html

	if (result.status_code == 200):
		decoded_json = json.loads(result.text)
		if decoded_json['status']== 'FAIL':
			html += '''<H3>Database Failure</H3>
					<p>
					Response from Application Server: <b>
					'''
			html += decoded_json['results']
			return html

		elif decoded_json['status']== 'OK':
			html += '''	<H3>Success</H3>
					<p>
					Response from Application Server: <b>
					'''
			html += decoded_json['results']

	else:  
		html += '''	<H3>Application Server Failure</H3>
					<p>
					We did not recieve a proper response from the application server.  Status Code != 200<b>
					<br>'''
		html += result.text

	return html

@app.route('/show_all_records')
def show_all_records():
	html = build_menu()
	html += '''<center>
		<body style="color:#BDBDBD"><H3>--Showing All records--</H3>
		<br>
		'''

	url = 'http://{0}:{1}/show_all_records'.format(app_addr, app_port)

	try: 
		result = requests.get(url)
	except:
		html += '''	<H3>Application Server Failure</H3>
					<p>
					'''
		html += 'Not able to communicate with Application Server at {0}.<b><br>'.format(app_addr)
		return html

	if (result.status_code == 200):
		decoded_json = json.loads(result.text)
		if decoded_json['status']== 'FAIL':
			html += '''	<H3>Database Failure</H3>
					<p>
					Response from Application Server: <b>
					'''
			html += decoded_json['results']
			return html

		if len(decoded_json['results']) == 0:
			html += '<font color="#2C63D5">'
			html += "No records found."
			return html

		else:
			html += '''<table style="color:#00FC00" border="1">
				<thead><tr>
				'''

			html += "<th>Name</th><th>Entry</th><th>Date</th>"
			html += "</tr></thead>"
					
			for line in range(len(decoded_json['results'])):
				name = decoded_json['results'][line]['name']
				entry = decoded_json['results'][line]['entry']
				date = decoded_json['results'][line]['date']
				html += "<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>".format(name, entry, date)

			html += "</table></body></html>"

	else:   
		html += '''	<H3>Application Server Failure</H3>
					<p>
					We did not receive a proper response from the application server.  Status Code != 200<b>
					<br>'''
		html += result.text

	return html

@app.route('/remove_db')
def remove_db():
	html = build_menu()
	html += '''<center>
		<BODY style="color:#BDBDBD"><H3>--Removing the Database--</H3>
		<br>
		'''

	url = 'http://{0}:{1}/remove_db'.format(app_addr, app_port)

	try: 
		result = requests.get(url)
	except:
		html += '''	<H3>Application Server Failure</H3>
					<p>
					'''
		html += 'Not able to communicate with Application Server at {0}.<b><br>'.format(app_addr)
		return html

	if (result.status_code == 200):
		decoded_json = json.loads(result.text)
		if decoded_json['status']== 'FAIL':
			html += '''	<H3>Database Failure</H3>
					<p>
					Response from Application Server: <b>
					'''
			html += decoded_json['results']
			return html

		elif decoded_json['status']== 'OK':
			html += '''	<H3>Success</H3>
					<p>
					Response from Application Server: <b>
					'''
			html += decoded_json['results']

	else:
		html += '''	<H3>Application Server Failure</H3>
					<p>
					We did not receive a proper response from the application server.  Status Code != 200<b>
					<br>'''
		html += result.text

	return html

@app.route('/server_info')
def server_info():
	menu_info = my_menu()
	html = screen_header(menu_info['width'])
	html += menu_info['menu']

	html += '''
		<center>
		<BODY style="color:#BDBDBD"><H3>Python test script</H3>
		'''
	html += "Python Version information:  {}".format(sys.version_info)
	html += '''
		<p>
		Current date and time for this server: 
		'''
	html += datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	html += '''
		<p>
		</BODY></HTML>
		'''

	return html

@app.route('/')
@app.route('/index')
def index():
	menu_info = my_menu()
	html = screen_header(menu_info['width'])
	html += menu_info['menu']

	html += '<h3 style="color:#2C63D5"><br><br>'

	html += '''
		<center><br>
		Please use the menu to select items.
		</h3>
		</center>
		</body>
		'''

	return html

def main(): 
	index()

if __name__ == '__main__':
	app.config.update(
		DEBUG = True)

	app.run(host='0.0.0.0', port=80)




