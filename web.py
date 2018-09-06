# # imports
# import tornado.ioloop
# import tornado.web
# #https://gist.github.com/cjgiridhar/3205067
# # write to screen
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.render('web/index.html')
#
# # r"/" == root website address
# #application = tornado.web.Application([(r"/", MainHandler)])
# application = tornado.web.Application([
#     (r'/', MainHandler),
#     (r'/js/(.*)', tornado.web.StaticFileHandler, {'path': './static/js'}),
#     (r'/css/(.*)', tornado.web.StaticFileHandler, {'path': './static/css'}),
#     (r'/fonts/(.*)', tornado.web.StaticFileHandler, {'path': './static/fonts'}),
#     (r'/images/(.*)', tornado.web.StaticFileHandler, {'path': './static/images'}),
# ])
#
# # Start the server at port 7777
# if __name__ == "__main__":
#     PortNumber = str(7777)
#     print('Server Running at http://localhost:' + PortNumber + '/')
#     print('To close press ctrl + c')
#     application.listen(PortNumber)
#     tornado.ioloop.IOLoop.instance().start()


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
    (r"/", Transcend),      # ('web/index.html')
    (r"/images/(.*)",tornado.web.StaticFileHandler, {"path": "./images"},),
    (r"/images/(style.\css)",tornado.web.StaticFileHandler, {"path": "./images/css"},),
],debug=True)

if __name__ == "__main__":
    PortNumber = str(7777)
    print('Server Running at http://localhost:' + PortNumber + '/')
    print('To close press ctrl + c')
    application.listen(PortNumber)
tornado.ioloop.IOLoop.instance().start()
