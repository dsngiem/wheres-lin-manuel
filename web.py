import linbot
import os
import tornado.httpserver
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		status = linbot.updateStatus()		
		self.write(status)

def main():
	application = tornado.web.Application([
		(r"/", MainHandler),
	])

	http_server = tornado.httpserver.HTTPServer(application)
	
	port = int(os.environ.get("PORT", 5000))
	http_server.listen(port)

	main_loop = tornado.ioloop.IOLoop.instance()

	#scheduler
	sched = tornado.ioloop.PeriodicCallback(linbot.updateStatus, 60000, io_loop=main_loop)
	sched.start()

	main_loop.start()

if __name__ == "__main__":
	main()