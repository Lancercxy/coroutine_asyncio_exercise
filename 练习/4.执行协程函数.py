import asyncio

async def func():
    print("hello, python")


# 注意：执行协程函数创建协程对象，函数内部代码不会执行。
# 如果想要运行协程函数内部代码，必须要讲协程对象交给事件循环来处理。
result = func()
# loop = asyncio.get_event_loop()    #生成或获取一个事件循环（3.7及以下版本写法）
# loop.run_until_complete(result)    #将任务放到任务列表

asyncio.run(result)                #3.7版本写法