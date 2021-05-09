import smtplib
from email.mime.text import MIMEText
from py_readConfigFile import read_config  
 
# 发送邮件函数封装
# mail_honst SMTP 邮件
def DsendEmail(receivers,title,content,t_format='plain'):

	config = read_config("./config.email.ini");
	
	# 第三方 SMTP 服务
	mail_host = config.get('email','mail_host')  # SMTP服务器
	mail_user = config.get('email','mail_user')  # 用户名
	mail_pass = config.get('email','mail_pass')  # 密码
	sender = config.get('email','sender')  # 发件人邮箱

	message = MIMEText(content, t_format, 'utf-8')  # 内容, 格式, 编码
	message['From'] = "{}".format(sender)
	message['To'] = ",".join(receivers)
	message['Subject'] = title
	
	try:
		smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
		smtpObj.login(mail_user, mail_pass)  # 登录验证
		smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
		return {"code":200,"msg":"发送成功"}
	except smtplib.SMTPException as e:
		return {"code":400,"msg":e}

#content = 'Python Send Mailsdfasdfad !'
#title = 'Python SMTP Mail Testsdfasdfa'  # 邮件主题
#receivers = ['970073804@qq.com']  # 接收人邮箱
#print(DsendEmail(receivers,title,content)['code'])
