#Description

So, it handles all of examples.

It saves results in the script directory as a json - "host: list of ports"
```json
{"192.168.1.1": [22, 23, 53, 80]}
```

Usage:

```bash
$ ./scanner.py 192.168.1.1

or

$ ./scanner.py 192.168.1.1/24
```

#Execrise 2

**Programming**

Build a program (in any language) for repetitive network scans displaying differences between
subsequent scans.

- scan can be executed either using external tools or using dedicated libraries of selected
programming language
- target of the scan must be parametrized as CLI argument
- target can be single IP address as well as network range

Example of expected result:

Initial scan:
```
$ ./scanner 10.1.1.1
*Target - 10.1.1.1: Full scan results:*
Host: 10.1.1.1 Ports: 22/open/tcp////
Host: 10.1.1.1 Ports: 25/open/tcp////
```

Repetitive scan with no changes on target host:
```
$ ./scanner 10.1.1.1
*Target - 10.1.1.1: No new records found in the last scan.*
```

Repetitive scan with changes on target host:
```
$ ./scanner 10.1.1.1
*Target - 10.1.1.1: Full scan results:*
Host: 10.1.1.1 Ports: 22/open/tcp////
Host: 10.1.1.1 Ports: 25/open/tcp////
Host: 10.1.1.1 Ports: 80/open/tcp////
```
