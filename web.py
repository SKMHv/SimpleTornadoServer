import tornado.ioloop
import tornado.web
import time

class ItWorks(tornado.web.RequestHandler):
    def get(self):
        self.write("It Works!!")

class Transcend(tornado.web.RequestHandler):
    def get(self):
        self.render('web/index.html')


application = tornado.web.Application([
    #(r"/", ItWorks),
    (r"/", Transcend),
    (r"/images/(.*)",tornado.web.StaticFileHandler, {"path": "./web/static/images"},),
    (r"/css/(.*)",tornado.web.StaticFileHandler, {"path": "./web/static/css"},),
    (r"/fonts/(.*)", tornado.web.StaticFileHandler, {"path": "./web/static/fonts"},),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "./web/static/js"},),
],debug=True)

if __name__ == "__main__":
    PortNumber = str(7777)
    print('Server Running at http://localhost:' + PortNumber + '/')
    print('To close press ctrl + c')
    application.listen(PortNumber)
tornado.ioloop.IOLoop.instance().start()
