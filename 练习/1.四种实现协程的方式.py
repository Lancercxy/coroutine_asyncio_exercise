from greenlet import greenlet
import asyncio

# 1.greenlet:实现协程
def func1():
    print(1)        #第1步：输出1
    gr2.switch()    #第3步：切换到func2函数
    print(2)        #第6步：输出2
    gr2.switch()    #第7步：切换到fuc2函数，从上一次执行的位置继续向后执行
    
def func2():
    print(3)        #第4步：输出3
    gr1.switch()    #第5步：切换到fuc1函数，从上一次执行的位置继续向后执行
    print(4)        #第8步：输出4

gr1 = greenlet(func1)
gr2 = greenlet(func2)

# gr1.switch()#第1步：去执行func1函数

########################################################################

# 2.yield关键字
def funcl():
    yield 1
    yield from func2()
    yield 2
def func2():
    yield 3
    yield 4

# f1 = funcl()
# for item in f1:
#     print(item)

########################################################################
    
# 3. asyncio
# 在oython.3.4及之后的版本。

@asyncio.coroutine
def func1():
    print(1)
    yield from asyncio.sleep(2) #遇到Io耗时操作，自动化切换到tasks中的其他任务
    print(2)
@asyncio.coroutine
def func2():
    print(3)
    yield from asyncio.sleep(2) #遇到Io耗时操作，自动化切换到tasks中的其他任务
    print(4)
tasks =[
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
    ]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

########################################################################

# 4. async & await
# 在oython.3.5及之后的版本。

async def func1():
    print(1)
    await asyncio.sleep(2) #遇到Io耗时操作，自动化切换到tasks中的其他任务
    print(2)

async def func2():
    print(3)
    await asyncio.sleep(2) #遇到Io耗时操作，自动化切换到tasks中的其他任务
    print(4)
tasks =[
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
    ]
loop = asyncio.get_event_loop()                 #生成或获取一个事件循环
loop.run_until_complete(asyncio.wait(tasks))    #将任务放到任务列表