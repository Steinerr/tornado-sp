import asyncio
import uuid
import tornado
from tornado import web
from tornado.escape import url_escape
from tornado.httpclient import AsyncHTTPClient
from tornado.options import parse_command_line, options
from tornado.web import RequestHandler

import settings


# Configure Tornado to use asyncio
tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOMainLoop')

# Configure Tornado to use CurlHttpClient
AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")


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


app_handlers = (
    (r"/", ProxyFile),
)

#
# class CustomSentryMixin(SentryMixin):
#     pass


class CustomApplication(web.Application):
    """
    Implement reusable http client.
    """

    def __init__(self, *args, **kwargs):
        super(CustomApplication, self).__init__(*args, **kwargs)
        # Http client
        self._http_client = None

    @property
    def http_client(self):
        if not self._http_client:
            self._http_client = AsyncHTTPClient()
        return self._http_client


application = CustomApplication(app_handlers, debug=True)


if __name__ == "__main__":
    if settings.DEBUG:
        # Set default logging level to debug
        options.logging = 'debug'
    # Parse tornado command line and set log formatting
    parse_command_line()
    application.listen(settings.PORT, settings.HOST)

    # tornado.ioloop.IOLoop.instance().start()

    loop = asyncio.get_event_loop()
    loop.run_forever()
