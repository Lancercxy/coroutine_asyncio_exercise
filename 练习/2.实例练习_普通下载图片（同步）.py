import requests
import aiohttp
import asyncio

#普通方式
def download_image(url):
    print("开始下载：" , url)
    #发送网络请求，下载图片
    response = requests.get(url)
    print("下载完成")
    #图片保存到本地文件
    file_name = url.rsplit('_')[-1]
    with open(file_name,mode='wb')as file_object:
        file_object.write(response.content)
if __name__=='__main__':
    url_list = [
    'https://car2.autoimg.cn/cardfs/product/g28/M03/C4/13/1400x0_1_q95_autohomecar__ChxkmmOGyzCANKpyACu7-pKcLiQ979.jpg',
    'https://car3.autoimg.cn/cardfs/product/g28/M04/98/CA/1400x0_1_q95_autohomecar__ChsFWWOArA6AcN2gACNPTqN6Hmc959.jpg',
    'https://car2.autoimg.cn/cardfs/product/g30/M06/2D/DE/1400x0_1_q95_autohomecar__ChxknGJ7JuaAO2y6ACPujiLbiM0573.jpg']
    for item in url_list:
        download_image(item)
        
        