import asyncio

async def func1():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return"返回值1"
async def func2():
    print(3)
    await asyncio.sleep(2)
    print(4)
    return"返回值2"
async def main():
    print("main开始")
    #创建Task对象，将当前执行func函数任务添加到事件循环。
    task_list = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2())
                ]
    print("main结束")
    #当执行某协程遇到I0操作时，会自动化切换执行其他任务。
    #此处的await是等待相对应的协程全都执行完毕并获取结果
    done, pending = await asyncio.wait(task_list, timeout = None)
    print(done)
asyncio.run(main())