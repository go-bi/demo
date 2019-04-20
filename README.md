# 
## siteserver cms 5.X vuln demo
SiteServer CMS remote download getshell `demo.zip`下载的后门文件
## 修改OpenSSH源代码记录用户详细操作日志
openssh*.tar.gz 修改后的文件编译安装即可，*.docx为修改说明。
+ https://www.zhoufengjie.cn/?p=385
+ https://www.zhoufengjie.cn/?p=174

## dropbear
+ FAKE_ROOT: #define 强制伪"root"uid解析，即使目标系统无法解析用户名。
+ ALT_SHELL: #define 假冒root用户使用备用shell而不是/bin/sh登陆。
+ Server Master Password: 在dropbear命令行上指定-Y以指定要进行身份验证的“主”密码，当没有root用户时，对FAKE_ROOT很有用，因此没有root密码。
+ Forced Home Directory: 在dropbear命令行上指定-H，以使用户使用指定的主目录登录。当没有root用户时，对FAKE_ROOT很有用，因此没有root主目录。
```
wget https://matt.ucc.asn.au/dropbear/releases/dropbear-2018.76.tar.bz2
tar xjf dropbear-2018.76.tar.bz2
cd dropbear-2018.76
./configure --disable-zlib
make
make install
mkdir /etc/dropbear
/usr/local/bin/dropbearkey -t dss -f /etc/dropbear/dropbear_dss_host_key
/usr/local/bin/dropbearkey -t rsa -s 4096 -f /etc/dropbear/dropbear_rsa_host_key
/usr/local/sbin/dropbear -p 6666
```
