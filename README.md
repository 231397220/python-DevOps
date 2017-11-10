# python-DevOps
目的:
  - 接收报警邮件,并根据邮件内容做后续逻辑处理

使用方法:
  - 使用python的poplib接收163上的邮件
  - 解决中文编码问题
  - 需要设置好用户名密码,pop邮件服务器地址.
  - 直接调用 print_info(msg)    msg是邮件的body,    msg= Parser().parsestr(\r\n'.join(server.retr(3))

