# ClipSync

一款可以帮助您同时同步剪贴板的小程序，通过python语言编写

### 前言

当您在一台计算机上复制了一条连接或讯息需要在另一台计算机上黏贴，你是否觉得十分繁琐、苦恼。如果您是苹果用户，您一定知道剪切板共享这个功能。当您在Macbook上复制一个链接，可以很轻松的在Iphone手机上黏贴出来。而这款程序，就可以实现类似功能，不过这款程序不仅限于苹果，可以用于任何配置python的环境中

### 开始使用

在使用这款软件之前，希望您已经正确的安装了python环境并且配置了环境变量

首先，需要您用pip命令安装本程序唯一一个第三方模块 `pyperclip` 

`pip install pyperclip`

接下来，使用Config_Creater.py文件，创建配置文件。如果以后不更改共享剪切板的计算机，您只需要配置一次

`python Config_Creater.py`

当您连接互联网时，会自动获取本机ip，否则需要手动输入.

配置完成，文件目录下的config.json里应该有内容了

接下来，运行程序

`python ClipSync.py`

没有报错就成功了！

### 提醒

本程序仅仅支持复制内容大学在4096kb之内，否则无法共享

程序出现问题请重新配置文件，遇到端口占用请手动修改端口(默认2024)

请确认两端电脑都开启程序在进行复制
