import aiohttp
import asyncio

async def fetch(session, url):
    print("发送请求:", url)
    async with session.get(url,verify_ssl=False) as response:
        text = await response.text()
        print("得到结果:", url, len(text))
        return text
    
async def main():
    async with aiohttp.ClientSession() as session:
        url_list =["https://python.org", "https://www.baidu.com", "https://www.pythonav.com"]
        #添加任务
        tasks = [ asyncio.create_task(fetch(session, url)) for url in url_list]
        #执行事件循环，等待结果
        done,pending = await asyncio.wait(tasks)
        
if __name__ == '__main__':
    asyncio.run( main())