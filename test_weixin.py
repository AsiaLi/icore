# -*- coding: utf-8 -*-
__author__ = 'Asia'

import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print 'got=====', msg
    return 'heheheda'

if __name__ == '__main__':

    itchat.auto_login()
    itchat.run()
