# zulip-action 🚀

A GitHub Action to send a private message to the specified user generally a repository owner or mantainer to notify when a code is pushed in the master branch

![alt text](https://github.com/MonilBhavsar/zulip-action/blob/master/ss.png "Screenshot")
## Configuration 

1. Edit the ```.zuliprc``` file by adding your API KEY, EMAIL ADDRESS and ZULIP WORKSPACE URI.
2. Message to be triggered can be edited in ```main.py``` file.
3. Messages can be sent to multiple users by appending email address in the list in ```main.py``` file.

## Future Scope

This action can keep the channel or stream up to date with the master branch and users(contributors) can know the status of their master branch.

[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/MonilBhavsar/zulip-action/blob/master/LICENSE)
