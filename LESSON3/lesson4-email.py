#!/usr/bin/env python

import email_helper
recipient = 'skyraven@gmail.com'
subject = 'Nothing'
message = '''
This is nothing
but multiline
'''
sender = 'noone@yahoo.con'
email_helper.send_mail(recipient, subject, message, sender)
