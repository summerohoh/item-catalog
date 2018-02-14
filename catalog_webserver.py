from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

# import CRUD Operations from Database
from catalog_dbsetup import Base, Brand, Category, Item
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///clothingcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/catalog"):
                categories = session.query(Category).all()
                output = ""
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output += "<html><body>"
                for category in categories:
                    output += category.name
                    output += "<br>"
                    output += "<a href='/catalog/%s/edit'> Edit</a> <br>" %category.id
                    output += "<a href='/catalog/%s/delete'> Delete</a> <br>" %category.id
                    output += "<br>"
                output += "<a href='/catalog/new'> Add a new category </a><br>"
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/catalog/new"):
                output = ""
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output += "<html><body>"
                output += "<h1> Add a new category </h1>"
                output += "<form method='POST' enctype='multipart/form-data' action='/catalog/new'>"
                output += "<input name='newCategoryName' type ='text' placeholder='new category name'>"
                output += "<input type='submit' value='Create'>"
                output += "</form>"
                output += "</body></html>"
                self.wfile.write(output)
                return

            if self.path.endswith("/edit"):
                output = ""
                categoryIDPath = self.path.split("/")[2]
                myCategoryQuery = session.query(Category).filter_by(id = categoryIDPath).one()

                if myCategoryQuery !=[]:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    output += "<html><body>"
                    output += "<h1>"+ myCategoryQuery.name + "</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action='/catalog/%s/edit'>" %categoryIDPath
                    output += "<input name='newCategoryName' type ='text' placeholder='%s'>" %myCategoryQuery.name
                    output += "<input type='submit' value='Rename'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)
                return

            if self.path.endswith("/delete"):
                output = ""
                categoryIDPath = self.path.split("/")[2]
                myCategoryQuery = session.query(Category).filter_by(id = categoryIDPath).one()

                if myCategoryQuery !=[]:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()

                    output += "<html><body>"
                    output += "<h1>"+ myCategoryQuery.name + "</h1>"
                    output += "<form method='POST' enctype='multipart/form-data' action='/catalog/%s/delete'>" %categoryIDPath
                    output += "<p> Delete this item? </p>"
                    output += "<input type='submit' value='Delete'>"
                    output += "</form>"
                    output += "</body></html>"
                    self.wfile.write(output)
                return



        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


    def do_POST(self):
        try:
            if self.path.endswith("/catalog/new"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == "multipart/form-data":
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get("newCategoryName")

                    #Create new category
                    newCategory = Category(name = messagecontent[0])
                    session.add(newCategory)
                    session.commit()

                    self.send_response(301)
                    self.send_header("content-type", "text/html")
                    self.send_header("Location", "/catalog")
                    self.end_headers()

            if self.path.endswith("/edit"):
                ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
                if ctype == "multipart/form-data":
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    messagecontent = fields.get("newCategoryName")
                    categoryIDPath = self.path.split("/")[2]

                    #update category name
                    myCategoryQuery = session.query(Category).filter_by(id=categoryIDPath).one()

                    if myCategoryQuery !=[]:
                        myCategoryQuery.name = messagecontent[0]
                        session.add(myCategoryQuery)
                        session.commit()
                        self.send_response(301)
                        self.send_header("content-type", "text/html")
                        self.send_header("Location", "/catalog")
                        self.end_headers()

            if self.path.endswith("/delete"):
                    categoryIDPath = self.path.split("/")[2]

                    #delete category name
                    myCategoryQuery = session.query(Category).filter_by(id=categoryIDPath).one()

                    if myCategoryQuery !=[]:
                        session.delete(myCategoryQuery)
                        session.commit()
                        self.send_response(301)
                        self.send_header("content-type", "text/html")
                        self.send_header("Location", "/catalog")
                        self.end_headers()

        except:
            pass


def main():
    try:
        server = HTTPServer(('', 8080), webServerHandler)
        print 'Web server running...open localhost:8080/catalog in your browser'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()