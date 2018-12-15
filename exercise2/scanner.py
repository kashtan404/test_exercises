#!/usr/bin/python3

import socket
import sys
from netaddr import IPNetwork
import json

target = sys.argv[1]

scan_list = []

if '/' in target:
    for ip in IPNetwork(target):
        scan_list.append(str(ip))
else:
    scan_list.append(target)


def scan(scan_list):
    """
    :param scan_list: list
    :return: dict
    """
    scan_results = {}
    for remote_host in scan_list:
        opened_ports = []
        try:
            for port in range(1,1025):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remote_host, port))
                if result == 0:
                    opened_ports.append(port)
                sock.close()

        except socket.error:
            print("Couldn't connect to server {}".format(remote_host))
            continue
        if opened_ports != []:
            scan_results[remote_host] = opened_ports
    return scan_results


def read_results():
    """
    :return: dict
    """
    data = {}
    try:
        with open('./scan_results.json', 'r') as file:
            data = json.load(file)
            file.close()
    # Handle situation while results are empty or not exist
    except:
        pass
    return data


def write_results(data):
    """
    :param data: dict
    :return: self
    """
    with open('./scan_results.json', 'w+') as file:
        json.dump(data, file)
        file.close()
    return

# Scan it
scan_results = scan(scan_list)

# Read previous results
previously = read_results()
if len(previously) > 0:
    scanned_before = True
else:
    scanned_before = False

for host in scan_results:
    if scanned_before and scan_results[host] == previously[host]:
        print('*Target - {}: No new records found in the last scan.*'.format(host))
    else:
        print('*Target - {}: Full scan results: *'.format(host))
        for port in scan_results[host]:
            print('Host: {} Ports: {}/open/tcp////'.format(host, port))

# Write new results
write_results(scan_results)
