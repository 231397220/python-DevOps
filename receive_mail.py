#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys
import time
import poplib
import time
import datetime
import string
import StringIO,rfc822
import smtplib
from datetime import datetime
import codecs
import chardet
import email
import base64
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
from email.mime.text import MIMEText
import re

# username = ""
username = "@163.com"
password = ""
host = "pop.163.com"
# host = ""

port = "995"

server = poplib.POP3(host)
server.user(username)
server.pass_(password)
# (mail_count, mail_total_size) = p.stat()  # 返回一个元组:(邮件数,邮件尺寸)
# print p.list() + "返回邮件数量和每个邮件的大小"
# print p.retr()

print('Messages: %s. Size: %s' % server.stat())   #打印有多少封邮件,总共大小是多少

resp, mails, octets = server.list()

print(mails)     #以列表显示没封邮件的大小

index = len(mails)    #取最后一封邮件

resp, lines, octets = server.retr(3)

msg_content = '\r\n'.join(lines)

msg = Parser().parsestr(msg_content)

# print "msg是:" ,msg
# value = msg.get_payload()
# value = value[0]
# value = msg.get("X-Coremail-Antispam",'')
# value = value.find('charset=')
# value = email.Header.Header(value)
# value = email.Header.decode_header(value)
# value = value[0][0]
# value = base64.b64decode(value)
# value = value.decode('UTF-8','strict')
# # value =
# value = re.split("[,+]", value)

# print value
# print type(value)


#获取邮件证明编码方法
def guess_charset(msg):
    # 先从msg对象获取编码:
    charset = msg.get_charset()
    if charset is None:
        # 如果获取不到，再从Content-Type字段获取:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        #判断如果找到charset相关字,按照相关字的位置取出字符编辑类型
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    print charset
    return charset


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


# 显示邮件头部的信息方法:
def print_info(msg, indent=0):
    if indent == 0:
        # 邮件的From, To, Subject存在于根对象上:
        for header in ['From', 'To', 'Message-ID', 'Date', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header == 'Subject':
                    # 需要解码Subject字符串:
                    value = email.Header.decode_header(email.Header.Header(value))
                    value = value[0][0].decode(value[0][1],'strict')
                elif header == 'Date':
                    # 取日期,后进行分割
                    value = re.split("[,+]",email.Header.decode_header(email.Header.Header(value))[0][0])[1]
                else:
                    # 需要解码Email地址:
                    hdr, addr = parseaddr(value)
                    name = str.decode(hdr)
                    value = u'%s %s' % (name, addr)
                    # print 2
            print('%s%s: %s' % ('  ' * indent, header, value))
    if (msg.is_multipart()):
        # 如果邮件对象是一个MIMEMultipart,
        # get_payload()返回list，包含所有的子对象:
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            # 递归打印每一个子对象:
            print_info(part, indent + 1)
    else:
        # 邮件对象不是一个MIMEMultipart,
        # 就根据content_type判断:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            # 纯文本或HTML内容:
            content = msg.get_payload(decode=True)
            # 要检测文本编码:
            charset = guess_charset(msg)
            print charset
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            # 不是文本,作为附件处理:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

print_info(msg)



