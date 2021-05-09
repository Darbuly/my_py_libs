from configparser import ConfigParser
import os

# 读取ini配置文件 v1.0.0
# file_path string 配置文件路径 相对脚本执行文件
 
def read_config(file_path):
	if file_path is None:
		raise FileNotFoundError("路径不能为空")
	conn = ConfigParser()
	if not os.path.exists(file_path):
		raise FileNotFoundError("配置文件不存在")

	conn.read(file_path)
	
	url = conn.get('api','url')
	method = conn.get('api','method')
	header = conn.get('api','header')
	data = conn.get('api','data')
	resp_code = conn.get('api','resp_code')
	resp_json = conn.get('api','resp_code')

	return conn;


