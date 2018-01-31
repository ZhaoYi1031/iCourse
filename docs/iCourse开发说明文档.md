# iCourse开发说明文档

服务器及mysql的用户名及密码均为下表，具体登录方式可参考下文详细说明。

| 属性 | 值 |
| --- | --- |
| 服务器地址 | 60.205.211.127 |
| 用户名 | root |
| 密码 | buaa@Icourse |

## 连接到云服务器

我们平台的所有数据目前局放在阿里云服务器上。在终端输入命令如下：

```
ssh root@60.205.211.127
密码是buaa@Icourse
```

连接到服务器后，我们的用到的所有文件在/home/icourse下。其中iCourse文件夹的内容和GitHub终端保持一致，主要保存的是网站端的代码(包括前端和后端)，以及目前我们所有用户上传的文件在改文件夹下的media目录里。

apache-tomcat-8.0.49文件夹主要保存的是nginx-tomcat环境，在webapps的文件夹下保存了我们的安卓服务器端的class文件以及搜索引擎Solr的环境。

## 数据库端

数据库的各个表及字段的功能请见**数据库说明文档.md**

### 方式零(推荐)：连接到服务器端

先连接到服务器，然后执行mysql命令即可，无须输入数据库的用户名即密码。即：

```
ssh root@60.205.211.127
密码是buaa@Icourse
mysql
> use icourse; （我们的数据库名称）
```


### 方式一：不登录服务器直接连接服务器数据库
1. 在mysql安装目录下输入指令 mysql -h 60.205.211.127 -P 3306 -u root -p
2. 在弹出的password提示后面输入密码，密码与登录服务器的密码相同
3. 在mysql下输入指令 use icourse;（我们的数据库名称）

### 方式二：直接登录服务器(使用putty)

1. 远程连接60.205.211.127
2. 输入指令 `mysql -u root -p`
3. 在弹出的password提示后面输入密码，密码与登录服务器的密码相同
4. 在mysql下输入指令 use icourse;（咱们的数据库名称）


### 方式三：通过MySQL Workbench连接数据库

下图中的10.2.28.124更换成60.205.211.127

1. 点击红色“+”按钮
![](http://images2017.cnblogs.com/blog/1254668/201711/1254668-20171122001652946-1368640111.png)
2. 在弹出的窗口中设置相关信息
![](http://images2017.cnblogs.com/blog/1254668/201711/1254668-20171122002441899-6905030.png)
3. 点击“Store in Vault...”按钮设置密码
![](http://images2017.cnblogs.com/blog/1254668/201711/1254668-20171122001946165-2016837326.png)
4. 在弹出的窗口中输入密码，密码与登录服务器的密码相同
![](http://images2017.cnblogs.com/blog/1254668/201711/1254668-20171122002057758-1364763856.png)
5. 点击“OK”，就可以看到新建的连接，点击就可以访问数据库了
![](http://images2017.cnblogs.com/blog/1254668/201711/1254668-20171122002756305-364767091.png)
![](http://images2017.cnblogs.com/blog/1254668/201711/1254668-20171122002823555-1731561390.png)

## 安卓端

### 客户端

代码在https://github.com/kjgfcdb/iCourse_Main
git clone后用Android Studio打开即可，选择模拟器进行模拟即可看到安卓app。

### 服务器端

代码在https://github.com/ZhaoYi1031/iCourse_Network
在修改完后我们需要把build出的class文件push到服务器端。

```
cd iCourse_Network
cd build/classes/com/ftp/servlet
scp * root@60.205.211.127:/home/icourse/apache-tomcat-8.0.49/webapps/androidServer/WEB-INF/classes/com/ftp/servletls
```









