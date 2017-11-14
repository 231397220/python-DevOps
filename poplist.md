Python与邮件服务相关的模块主要有4个：poplib和imaplib主要提供从邮件服务器上下载邮件；smtplib主要提供发送邮件服务；email模块主要提供分析邮件和构建邮件功能。

    POP3全称'Post Office Protocol - Version 3',即邮局协议版本3.是TCP/IP协议簇中的一员，使用默认端口110.主要用于支持客户端远程管理服务器上的电子邮件。

import poplib    # 导入模块
server=poplib.POP3(mailserver)    #建立到邮件服务器的连接，如：pop.163.com
server.user(mailuser)    #连接并登入邮箱账户，如：test@163.com
server.pass_(mailpassword)  #输入登陆密码，主意pass后面有_,此处通常用getpass来输入密码
msgCount，msgBytes=server.stat()  #获取邮箱信息，包括邮件数目，邮件总字节数

header, message, octets=server.retr(N)   #获取第N封邮件信息，邮件从1开始排序。获取内容包括邮件头部，邮件内容，邮件字节数。
server.encoding='utf-8'   #可以自定义编解码方式
server.getwelcome()  #获取邮件服务器上的欢迎信息
server.list()      #获取服务器上的邮件列表，其中主要包含邮件编号（retr的时候用的N），邮件的大小（bytes）
server.dele(msgnum)   #在服务器上删除第msgnum封邮件
server.top(N,0)     #获得第N封邮件的头部信息，第二个数字表示除了头部信息外还额外取多少行内容
server.quit()      # 关闭连接
