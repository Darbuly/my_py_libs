from py_email import DsendEmail

content = 'Python Send Mailsdfasdfad !'
title = 'Python SMTP Mail Testsdfasdfa'  # 邮件主题
receivers = ['970073804@qq.com']  # 接收人邮箱
print(DsendEmail(receivers,title,content)['code'])
