# -*- coding: utf8 -*-
# author： NJB 
# email ： mincau@163.com
import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    print("get connect {0}".format(host))

    print("*"*20, "before yield from connect", "*"*20, host)
    reader, writer = yield from connect
    print("*" * 20, "after yield from connect", "*" * 20, host)

    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    print(header)

    writer.write(header.encode('utf-8'))
    print("*" * 20, "before yield from writer", "*" * 20, host)
    yield from writer.drain()
    print("*" * 20, "after yield from writer", "*" * 20, host)
    while True:
        print("*" * 20, "before yield from line", "*" * 20, host)
        line = yield from reader.readline()
        print("*" * 20, "after yield from line", "*" * 20, host)
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
