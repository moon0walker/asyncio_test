# asyncio_wait_timeout.py


import asyncio
import functools


async def phase(i):
    print('in phase {}'.format(i))
    try:
        await asyncio.sleep(0.2 * i)
    except asyncio.CancelledError:
        print('phase {} cancelled'.format(i))
        raise
    else:
        print('done with phase {}'.format(i))
        return 'phase {} result'.format(i)


async def main(num_phases):
    print('starting main')
    phases = [
        phase(i)
        for i in range(num_phases)
    ]
    print('waiting 0.2 for phases to complete')
    completed, pending = await asyncio.wait(phases, timeout=0.2)
    print( '{} completed and {} pending'.format( len(completed), len(pending) ) )
    # Cancel remaining tasks so they do not generate errors
    # as we exit without finishing them.

    print(10*'*', len(pending))
    for t in pending: print(t.done())
    print('start asyncio.sleep(1)')
    await asyncio.sleep(1)
    print('end  asyncio.sleep(1)')
    for t in pending: print(t.done())
    print(10*'*', len(pending))

    # if pending:
    #     print('cancelling tasks')
    #     for t in pending:
    #         t.cancel()
    print('exiting main')


event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(3))
finally:
    event_loop.close()