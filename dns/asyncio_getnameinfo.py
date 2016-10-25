# asyncio_getnameinfo.py


import asyncio


targets = [
    ('10.1.0.7', 80),
    ('10.1.0.4', 80)
]

event_loop = asyncio.get_event_loop()
try:
    for target in targets:
        info = event_loop.run_until_complete(
            event_loop.getnameinfo(target)
        )

        print('{:15}: {} {}'.format(target[0], *info))
finally:
    event_loop.close()

