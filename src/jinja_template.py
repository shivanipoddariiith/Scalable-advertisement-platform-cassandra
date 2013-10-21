import jinja2
env = jinja2.Environment(loader=jinja2.FileSystemLoader(["/home/shivani/jinja"]))
template=env.get_template("temp.html")
print template.render( title="Scalable Advertisement Platform")

