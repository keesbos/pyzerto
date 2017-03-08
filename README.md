
Zerto
=====

The Zerto module interfaces with the Zerto Api.

Zerto: Disaster Recovery & Virtual Data Replication - zerto.com

Api documentation: https://www.zerto.com/myzerto/technical-documentation/

License: Apache (http://www.apache.org/licenses/LICENSE-2.0)

Example usage:
```

from __future__ import print_function
try:
    import requests
    # Do this only in testing
    requests.packages.urllib3.disable_warnings()
except:
    pass

import zerto

zapi = zerto.Zerto('https://127.0.0.1:9669')
zapi.get_apis()
zapi.get_session('user', 'password')
print('VRAs')
for i in zapi.get_vra():
    print(i)
print('VPGs')
for i in zapi.get_vpg():
    print(i)
print('VMs')
for i in zapi.get_vm():
    print(i)
print('Events')
for i in zapi.get_event():
    print(i)
print('Tasks')
for i in zapi.get_task():
    print(i)
```

To install (preferably in virtualenv): easy_install https://github.com/keesbos/pyzerto/tarball/master
