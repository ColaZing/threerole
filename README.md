1.安装python环境，版本最好选择python3.8

2.安装pycharm专业版，直接官网下载即可，有30天试用，过后可以选择破解版或是学生认证用一年

3.在cmd/终端中执行以下命令：

​	pip install django==3.2.16 -i https://pypi.tuna.tsinghua.edu.cn/simple

​	pip install django-import-export -i https://pypi.tuna.tsinghua.edu.cn/simple

​	pip install django-simpleui -i https://pypi.tuna.tsinghua.edu.cn/simple

4.在pycharm的右下角选择解释器，然后选择刚刚安装的python路径（添加本地解释器，环境选现有，不要选新建）

5.在pycharm的右上方有运行配置/编辑配置（绿色三角形旁边），点开之后在右边右键--添加新配置--django服务器即可

6.后续启动，只要在pycharm里面打开项目，然后点那个绿色三角形就行

前端地址：http://127.0.0.1:8000/

管理端地址：http://127.0.0.1:8000/admin

管理员账户root 管理员密码123456