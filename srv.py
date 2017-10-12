import tornado.ioloop
import tornado.web
from tornado.httpclient import AsyncHTTPClient
import uuid
from tornado.escape import url_escape
from tornado.web import RequestHandler


class ProxyFile(RequestHandler):
    async def get(self, *args, **kwargs):
        self.set_header('Content-Type', 'application/octet-stream')
        self.set_header('Content-Disposition', b'attachment; filename=%s;' % url_escape(
            '{}.jpg'.format(uuid.uuid4()),
            False
        ).encode())
        self.flush()

        def stream_callback(chunk):
            self.write(chunk)
            self.flush()

        def header_callback(head):
            if head.startswith('Content-Length'):
                self.set_header('Content-Length', head.strip().split(':')[1])
                self.flush()

        # url = 'https://upload.wikimedia.org/wikipedia/commons/d/db/Patern_test.jpg'
        url = 'http://speedtest.ftp.otenet.gr/files/test100Mb.db'
        client = AsyncHTTPClient()
        await client.fetch(
            url,
            streaming_callback=stream_callback,
            header_callback=header_callback,
        )
        self.finish()


application = tornado.web.Application([
    (r"/", ProxyFile),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
