import asyncio


def consumer():
    deal = False
    while True:
        price = yield deal
        if price < 500:
            print('[卖家]呵呵')
            deal = False
        else:
            print('[卖家]哈哈')
            deal = True


def produce(c):
    c.send(None)
    price_list = [10, 20, 30, 40, 100, 500, 10000]
    for price in price_list:
        print('[买家]出价：{}'.format(price))
        deal = c.send(price)
        if deal:
            print('达成买卖')
            return
    print('不欢而散')

# c = consumer()
# produce(c)


@asyncio.coroutine
def wait(n):
    print('waiting')
    yield from asyncio.sleep(n)
    print('ok go')

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([wait(10), wait(5)]))
loop.close()