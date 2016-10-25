# asyncio_signal.py


import asyncio
import functools
import os
import signal


def signal_handler(name):
    print('signal_handler({!r})'.format(name))


async def send_signals():
    pid = os.getpid()
    print('starting send_signals for {}'.format(pid))

    for name in ['SIGTERM', 'SIGINT']:
        print('sending {}'.format(name))
        os.kill(pid, getattr(signal, name))
        # Yield control to allow the signal handler to run,
        # since the signal does not interrupt the program
        # flow otherwise.
        print('yielding control')
        await asyncio.sleep(0.01)
    return


event_loop = asyncio.get_event_loop()

event_loop.add_signal_handler(
    signal.SIGBREAK,
    functools.partial(signal_handler, 'SIGBREAK'),
)
event_loop.add_signal_handler(
    signal.SIGTERM,
    functools.partial(signal_handler, 'SIGTERM'),
)
event_loop.add_signal_handler(
    signal.SIGINT,
    functools.partial(signal_handler, 'SIGINT'),
)

try:
    event_loop.run_until_complete(send_signals())
finally:
    event_loop.close()
