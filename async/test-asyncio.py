# -*- coding: utf8 -*-
# author： NJB 
# email ： mincau@163.com
import asyncio
import threading


@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print(r)
    print("Hello again!")


@asyncio.coroutine
def hello2():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

thread = False

if thread:
    # 获取EventLoop:
    loop = asyncio.get_event_loop()
    # 执行coroutine
    loop.run_until_complete(hello())
    loop.close()
else:
    loop = asyncio.get_event_loop()
    tasks = [hello2(), hello2()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
