import jinja2
from wsgiref.simple_server import make_server
from webob import Request,Response,exc
from tempita import HTMLTemplate
import os
import re
import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
#The schema name here is Keyspace2
#The tables are Item, User, Location, Categories
pool = ConnectionPool('Keyspace2', server_list=['localhost:9160'])
item = ColumnFamily(pool, 'Item')
user = ColumnFamily(pool, 'Category')
location = ColumnFamily(pool, 'Location')

VIEW_TEMPLATE = HTMLTemplate("""\
<html>
<head>
</head>
<body>
<h1>title</h1>
</body>
</html>
""")
import jinja2
class WikiApp():
	path = "/home/shivani/Desktop/Courses/Cloud_Computing/Major_project/Adv_platform/src"
	view_template = VIEW_TEMPLATE	
	def __init__(self):
		self.application="Project";
	def __call__(self,environ,start_response):
        	req = Request(environ)
        #	resp = Response(
	#	'Hello %s!' % req.params.get('name', 'World'))
		action = req.params.get('action')
		print action
		try:
            		try:
                		meth = getattr(self, 'action_%s_%s' % (action, req.method))
            		except AttributeError:
                		raise exc.HTTPBadRequest('No such action %r' % action)
            		resp = meth(req)
        	except exc.HTTPException, e:
            		resp = e
        	return resp(environ, start_response)		

		env = jinja2.Environment(loader=jinja2.FileSystemLoader([self.path]))
		template=env.get_template("tmp1.html")
		start_response('200 OK', [('Content-Type', 'text/html')])
		temp = template.render().encode('ascii','ignore')
		return temp


	def action_view_GET(self,req):
		env = jinja2.Environment(loader=jinja2.FileSystemLoader([self.path]))
		template=env.get_template("form.html")
		temp = template.render().encode('ascii','ignore')
		return Response(temp);


	def action_view_POST(self,req):
		itemName=req.params['item_name'];
		itemLoc=req.params['item_loc'];
		itemPrice=req.params['item_price'];
		category=req.params['item_cat'];
		sellerName=req.params['seller_name'];
		sellerNo=req.params['seller_no'];
		sellerEmail=req.params['seller_email'];
		sellerAdd=req.params['seller_add'];
		id_ = 0
		#Insert Item in table 'Item'
		item.insert(id_, {'Name':itemName,
				  'Location':itemLoc, 
				  'Price':itemPrice, 
				  'Category':category})
		#Insert user info in table 'User'
		
		
		env = jinja2.Environment(loader=jinja2.FileSystemLoader([self.path]))
		template=env.get_template("tmp.html")
				
		temp = template.render(title="Recorded successfully").encode('ascii','ignore')
		return Response(temp);


if __name__ == '__main__':
    app=WikiApp()
    httpd = make_server('localhost', 8000, app)
    try:
    	httpd.serve_forever()
    except KeyboardInterrupt:
    	print '^C'
