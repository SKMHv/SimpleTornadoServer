import tornado.ioloop
import tornado.web
import time
import time, random

class ItWorks(tornado.web.RequestHandler):
    def get(self):
        self.write("It Works!!")

class WEBTester(tornado.web.RequestHandler):
    def get(self):
        citaty =[]
        try:
            with open('web/static/citaty.txt', 'r', encoding='utf-8') as subor:
                for riadok in subor:
                    riadok = riadok.strip()
                    citat = riadok.split(':')
                    citaty.append(citat)

                random_citat = citaty[random.randrange(len(citaty))]
                citat = random_citat[0]
                citat_autor = random_citat.pop()




        except IOError:
            print('Subor "static/citaty.txt" sa nenasiel!!!')

        self.render('web/index.html', title='Home', citat=citat, citat_autor=citat_autor)


application = tornado.web.Application([
    #(r"/", ItWorks),
    (r"/", WEBTester),
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


# ---------------------------------------



