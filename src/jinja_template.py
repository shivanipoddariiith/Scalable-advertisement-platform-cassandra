import jinja2
env = jinja2.Environment(loader=jinja2.FileSystemLoader(["/home/shivani/Desktop/Courses/Cloud_Computing/Major_project/Adv_platform/src"]))
template=env.get_template("temp.html")
print template.render( title="Scalable Advertisement Platform")

