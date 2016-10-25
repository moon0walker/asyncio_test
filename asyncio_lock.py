# asyncio_lock.py


import asyncio
import functools
from random import randint
from datetime import datetime

def unlock(lock):
    print('[{}] callback releasing lock'.format(datetime.now()))
    lock.release()


async def coro(id, lock):
    print('[{}] coro{} waiting for the lock'.format(datetime.now(), id))
    with await lock:
        print('[{}] coro{} acquired lock'.format(datetime.now(), id))
        asyncio.sleep(randint(0,5))
    print('[{}] coro{} released lock'.format(datetime.now(), id))


event_loop = asyncio.get_event_loop()
try:
    # Create and acquire a shared lock.
    lock = asyncio.Lock()
    print('acquiring the lock before starting coroutines')
    event_loop.run_until_complete(lock.acquire())
    print('[{}] lock acquired: {}'.format(datetime.now(), lock.locked()))

    # Schedule a callback to unlock the lock.
    event_loop.call_later(2, functools.partial(unlock, lock))

    # Run the coroutines that want to use the lock.
    print('entering event loop')
    event_loop.run_until_complete(
        asyncio.wait([coro(1, lock),
                      coro(2, lock)]),
    )
    print('exited event loop')

    print('lock status: {}'.format(lock.locked()))
finally:
    event_loop.close()
