#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import requests
import os
import zulip


def main():
    client = zulip.Client(config_file='.zuliprc')

    # Send a private message

    request = {'type': 'private',
               'to': ['<EMAIL ID HERE>'],
               'content': 'Message From Github! Push Event is triggered in the master branch  '}
    result = client.send_message(request)
    print(result)


if __name__ == '__main__':
    main()