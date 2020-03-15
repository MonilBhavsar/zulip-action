import json
import requests
import os
import zulip

def main():
    client = zulip.Client(config_file="~/zuliprc")
	# Send a private message
	request = { "type": "private","to": ['monilbhavsar.england99@gmail.com'],"content": "Hello!!"
	}
	result = client.send_message(request)
	print(result)

if __name__ == "__main__":
    main()