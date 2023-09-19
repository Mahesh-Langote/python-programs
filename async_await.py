import asyncio

async def example_async_function():
    print("Start")
    await asyncio.sleep(2)
    print("End")

asyncio.run(example_async_function())
