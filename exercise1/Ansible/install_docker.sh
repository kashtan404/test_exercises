#!/usr/bin/env bash

ansible-playbook -i "localhost," -c local site.yml -K
