import tornado.ioloop
import tornado.web
import random

class ItWorks(tornado.web.RequestHandler):
    def get(self):
        self.write("It Works!!")

class WEBTester(tornado.web.RequestHandler):
    def get(self):
        citaty =[]
        try:
            with open('web/citaty.txt', 'r', encoding='utf-8') as subor:
                for riadok in subor:
                    riadok = riadok.strip()
                    citat = riadok.split(':')
                    citaty.append(citat)

                random_citat = citaty[random.randrange(len(citaty))]
                citat = random_citat[0]
                citat_autor = random_citat.pop()

        except IOError:
            print('Subor "static/citaty.txt" sa nenasiel!!!')

        self.render('web/sign-in.html', title='sign-in')


application = tornado.web.Application([
    #(r"/", ItWorks),
    (r"/", WEBTester),
    (r"/web/(.*)", tornado.web.StaticFileHandler, {"path": "./web"},),
    (r"/jqvmap/(.*)", tornado.web.StaticFileHandler, {"path": "./jqvmap"},),
    (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "./css"},),
    (r"/fonts/(.*)", tornado.web.StaticFileHandler, {"path": "./fonts"},),
    (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "./js"},),
    (r"/img/(.*)", tornado.web.StaticFileHandler, {"path": "./img"},),
], debug=True)

if __name__ == "__main__":
    PortNumber = str(7777)
    print('Server Running at http://localhost:' + PortNumber + '/')
    print('To close press ctrl + c')
    application.listen(PortNumber)



tornado.ioloop.IOLoop.instance().start()


# ---------------------------------------



