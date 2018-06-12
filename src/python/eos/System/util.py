#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import subprocess

eos = os.path.expanduser('~/src/github.com/chainpool/eosdev')
cleos = eos + '/build/programs/cleos/cleos'

jp = 'http://13.231.129.154:8888'

url = jp

cleos = [cleos, '--url', url]

logging.basicConfig(
    filename='test.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s    %(message)s',
)


def cli(cmd):
    logging.info(cmd)
    try:
        out_bytes = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
    except Exception as e:
        out_bytes = e.output
    return out_bytes


def push_action(cmd):
    cmd = cleos + ['push', 'action', 'eosio'] + cmd
    out_bytes = cli(cmd)
    return out_bytes


def get_table(cmd):
    cmd = cleos + ['get', 'table', 'eosio'] + cmd
    out_bytes = cli(cmd)
    return out_bytes


def unlock_default_wallet(
        pwd='PW5Kc7w9n1yn6FZppV5kLzF54RQ3yUEQKp9gNGGLvEHBXHCTM2F6b'):
    cmd = cleos + ['wallet', 'list']
    out_bytes = cli(cmd)
    #  unlock wallet default if it hasn't been unlocked
    if b'default *' not in out_bytes:
        subprocess.check_call(cleos + ['wallet', 'unlock', '--password', pwd])
