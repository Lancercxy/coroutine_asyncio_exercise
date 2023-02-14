import asyncio
import aiohttp

async def fetch(session,url):
    print("发送请求:", url)
    async with session.get(url,verify_ssl=False) as response:
        content = await response.content.read()
        file_name = url.rsplit('_')[-1]
        with open(file_name,mode='wb')as file_object:
            file_object.write(content)
        print("下载完成：", file_name)
async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
        'https://car2.autoimg.cn/cardfs/product/g28/M03/C4/13/1400x0_1_q95_autohomecar__ChxkmmOGyzCANKpyACu7-pKcLiQ979.jpg',
        'https://car3.autoimg.cn/cardfs/product/g28/M04/98/CA/1400x0_1_q95_autohomecar__ChsFWWOArA6AcN2gACNPTqN6Hmc959.jpg',
        'https://car2.autoimg.cn/cardfs/product/g30/M06/2D/DE/1400x0_1_q95_autohomecar__ChxknGJ7JuaAO2y6ACPujiLbiM0573.jpg'
        ]
        tasks = [asyncio.create_task(fetch(session,url))for url in url_list]
        await asyncio.wait(tasks)
if __name__=='__main__':
    asyncio.run(main())