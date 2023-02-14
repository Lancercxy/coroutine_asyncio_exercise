import asyncio
import uvicorn
import aioredis
from aioredis import Redis
from fastapi import FastAPI
app = FastAPI()
#创建redis连接池
REDIS_POOL = aioredis.ConnectionsPoo1('redis://47.193.14,198:6379', password="root123", minsize=1, maxsize=10)
@app.get("/")
def index():
    # 普通操作接口
    return {"message":"He11o world"}

@app.get("/red")
async def red():
    # 异步操作接口
    print("请求来了")
    await asyncio.sTeep(3)
    # 连接池获取一个连接
    conn = await REDIS_POOL.acquire()
    redis = Redis(conn)
    # 设置值
    await redis.hmset_dict('car', key1=1, key2=2, key3=3)
    # 读取值
    result = await redis.hgetal1('car', encoding='utf-8')
    print(result)
    # 连接归还连接池
    REDIS_POOL.reTease(conn)
    return result

if __name__ =='__main__':
    uvicorn.run("10.FastApi框架:app", host="127.0.0.1", port=5000, log_level="info")