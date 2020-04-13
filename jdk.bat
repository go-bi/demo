@echo 以管理员身份运行，否则会拒绝访问系统变量
 
setx /M JAVA_HOME "C:\Program Files\Java\jdk1.8.0_181"
 
setx /M CLASSPATH ".;%%JAVA_HOME%%\lib;%%JAVA_HOME%%\lib\tools.jar;"
 
setx /M PATH "%PATH%;%%JAVA_HOME%%\bin;%%JAVA_HOME%%\jre\bin;"
 
pause