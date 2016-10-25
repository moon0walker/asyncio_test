import asyncio
import functools


async def task_func():
    print('in task_func, sleeping')
    try:
        await asyncio.sleep(1)
    except asyncio.CancelledError:
        print('task_func was cancelled')
    return 'wrapped result'


async def task_canceller(t):
    print('in task_canceller')
    t.cancel()
    print('cancelled the task')


event_loop = asyncio.get_event_loop()
try:
    print('creating task')
    task = event_loop.create_task(task_func())

    event_loop.run_until_complete(task_canceller(task))
finally:
    event_loop.close()
