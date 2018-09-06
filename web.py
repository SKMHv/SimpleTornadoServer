# imports
import tornado.ioloop
import tornado.web


# write to screen
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates\index.html')

# r"/" == root website address
application = tornado.web.Application([(r"/", MainHandler)])

# Start the server at port 7777
if __name__ == "__main__":
    PortNumber = str(7777)
    print('Server Running at http://localhost:' + PortNumber + '/')
    print('To close press ctrl + c')
    application.listen(PortNumber)
    tornado.ioloop.IOLoop.instance().start()