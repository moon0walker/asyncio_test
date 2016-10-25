#asyncio_getaddrinfo.py


import asyncio
import socket


targets = [
    ('redmine.test', 'http'),
    ('gitlab.test', 'http'),
    ('gitlab.lab', 'http'),
]

event_loop = asyncio.get_event_loop()
try:
    for target in targets:
        info = event_loop.run_until_complete(
            event_loop.getaddrinfo(
                *target,
                proto=socket.IPPROTO_TCP,
            )
        )

        for host in info:
            print('{:20}: {}'.format(target[0], host[4][0]))
finally:
    event_loop.close()

