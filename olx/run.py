from flask import Flask
app = Flask(__name__)


from flask import render_template


from flask import make_response,request,redirect,url_for
@app.route('/index/')
@app.route('/index/<name>')
def index(name=None):
#	response.url_for('static', filename='style.css')
	print request.method
	if request.method == 'POST':
		print "here"
		
	else:
		if name == 'Add':
			 return redirect(url_for('Add'))
#		userlist={1:'cat1',2:'cat2',3:'cat3'}
		catlist=['cat1','cat2','cat3']
		subcatlist=['scat1','scat2','scat3','scat3','scat3','scat3','scat3','scat3','scat3']
		return render_template('index.html',catlist=catlist,subcatlist=subcatlist)

@app.route('/Add/')
def Add():
	if request.method == 'POST':
		print "df"
	else:
#		userlist={1:'cat1',2:'cat2',3:'cat3'}
		
		return render_template('Add.html')

	
if __name__ == '__main__':
    app.run(debug=True)
