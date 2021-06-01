#### 1. Docker介绍

- [Docker中文社区文档](http://www.docker.org.cn/index.html)
- Docker 是一个开源的软件部署解决方案。
- Docker 也是轻量级的应用容器框架。
- Docker 可以打包、发布、运行任何的应用。
- Docker 就像一个盒子，里面可以装很多物件，如果需要某些物件，可以直接将该盒子拿走，而不需要从该盒子中一件一件的取。
- Docker 是一个`客户端-服务端(C/S)`架构程序。
  - 客户端只需要向服务端发出请求，服务端 处理完请求后会返回结果。

> Docker 包括三个基本概念:

- 镜像（Image）： 相当于 虚拟机的 iso 镜像
  - Docker的镜像概念类似于虚拟机里的镜像，是一个只读的模板，一个独立的文件系统，包括运行容器所需的数据，可以用来创建新的容器。
  - 例如：一个镜像可以包含一个完整的 centos操作系统环境，里面仅安装了MySQL或用户需要的其它应用程序。
- 容器（Container）
  - Docker容器是由Docker镜像创建的运行实例，类似VM虚拟机，支持启动，停止，删除等。
  - 每个容器间是相互隔离的，容器中会运行特定的应用，包含特定应用的代码及所需的依赖文件。
- [仓库（Repository）](https://hub.docker.com/)
  - Docker的仓库功能类似于Github，是用于托管镜像的。

#### 2. Docker安装（centos）

> **1.安装Docker**

```bash
# 安装docker的yum源
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

# 安装docker
yum install docker-ce
```

> **2.检查Docker CE是否安装正确**

```bash
$ docker version
```

> **3.启动与停止**

- 安装完成Docker后，默认已经启动了docker服务。

```bash
# 启动docker
$ service docker start
# 重启docker     
$ service docker restart
# 停止docker
$ service docker stop
```

#### 3. Docker镜像操作

> **1.镜像列表**

```bash
$ docker image ls
```

```
* REPOSITORY：镜像所在的仓库名称 
* TAG：镜像标签 
* IMAGEID：镜像ID 
* CREATED：镜像的创建日期(不是获取该镜像的日期) 
* SIZE：镜像大小
```

> **2.从仓库拉取镜像**

```bash
# 官方镜像
$ docker image pull 镜像名称 
$ docker image pull centos 
$ docker image pull centos:7
```

> **3.查看镜像**

```bash
$ docker image ls
```



> **4.删除镜像**

```bash
$  docker image rm 镜像名或镜像ID
$  docker image rm hello-world
$  docker image rm fce289e99eb9
```



#### 4. Docker容器操作

> **1.容器列表**

```bash
# 查看正在运行的容器
$  docker container ls   #  docker ps
# 查看所有的容器
$  docker container ls --all  #  docker ps -a
```



> **2.创建容器**

```bash
$  docker run [option] 镜像名 [向启动容器中传入的命令]
```

```
常用可选参数说明：
* -i 表示以《交互模式》运行容器。
* -t 表示容器启动后会进入其命令行。加入这两个参数后，容器创建就能登录进去。即分配一个伪终端。 /bin/bash
* --name 为创建的容器命名。
* -v 表示目录映射关系，即宿主机目录:容器中目录。注意:最好做目录映射，在宿主机上做修改，然后共享到容器上。 
* -d 会创建一个守护式容器在后台运行(这样创建容器后不会自动登录容器)。 
* -p 表示端口映射，即宿主机端口:容器中端口。
* --network=host 表示将主机的网络环境映射到容器中，使容器的网络与主机相同。
```

> **3.交互式容器**

```bash
$  docker run -it --name=centos1 centos:7 /bin/bash
```

```
在容器中可以随意执行linux命令，就是一个centos的环境。
当执行 exit 命令退出时，该容器随之停止。
```

> **4.守护式容器**

```bash
# 开启守护式容器
$  docker run -dit --name=centos2 centos:7
```

```bash
# 进入到容器内部交互环境
$  docker exec -it 容器名或容器id 进入后执行的第一个命令
$  docker exec -it centos2 /bin/bash
```

```
如果对于一个需要长期运行的容器来说，我们可以创建一个守护式容器。
在容器内部执行 exit 命令退出时，该容器也随之停止。
```

> **5.停止和启动容器**

```bash
# 停止容器
$  docker container stop 容器名或容器id
# kill掉容器
$  docker container kill 容器名或容器id
# 启动容器
$  docker container start 容器名或容器id
```

> **6.删除容器**

- 正在运行的容器无法直接删除。

```bash
$  docker container rm -f(强制删除) 容器名或容器id
```

> **7.容器制作成镜像**

- 为保证已经配置完成的环境可以重复利用，我们可以将容器制作成镜像。

```bash
# 将容器制作成镜像
$  docker commit 容器名 镜像名
```

```bash
# 镜像打包备份
$  docker save -o 保存的文件名 镜像名
```

```bash
# 镜像解压
$  docker load -i 文件路径/备份文件
```











# MySQL主从同步

### 1. 主从同步机制

> **1.主从同步介绍和优点**

- 在多台数据服务器中，分为主服务器和从服务器。一台主服务器对应多台从服务器。
- 主服务器只负责写入数据，从服务器只负责同步主服务器的数据，并让外部程序读取数据。
- 主服务器写入数据后，即刻将写入数据的命令发送给从服务器，从而使得主从数据同步。
- 应用程序可以随机读取某一台从服务器的数据，这样就可以分摊读取数据的压力。
- 当从服务器不能工作时，整个系统将不受影响；当主服务器不能工作时，可以方便地从从服务器选举一台来当主服务器
- 使用主从同步的优点：
  - 提高读写性能
    - 因为主从同步之后，数据写入和读取是在不同的服务器上进行的，而且可以通过增加从服务器来提高数据库的读取性能。
  - 提高数据安全
    - 因为数据已复制到从服务器，可以在从服务器上备份而不破坏主服务器相应数据。

> **2.主从同步机制**

> MySQL服务
>
> <img src="C:\Users\apple\AppData\Roaming\Typora\typora-user-images\image-20210413210843620.png" alt="image-20210413210843620" style="zoom:40%;" align='left'/>
>
> 器之间的主从同步是基于**二进制日志机制**，主服务器使用二进制日志来记录数据库的变动情况，从服务器通过读取和执行该日志文件来保持和主服务器的数据一致。



### 2. 基于 Docker 来搭建 MySQL 的主从复制

1. 准备两台 MySQL 服务器
2. 配置主服务器（Master）
3. 配置从服务器（Slave）
4. 完成Master和Slave链接
5. 测试配置是否成功

####  2.1.准备两台 MySQL 服务器

- 使用 Docker 创建 MySQL 的master服务器：

  ```bash
  docker run --name mysql_master -p 3307:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7.22
  ```

- 使用同样的方式创建 Slave 服务器：

  ```bash
  docker run --name mysql_slave -p 3308:3306 -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7.22
  ```

- 使用 ` docker ps` 查看当前运行的容器

#### 2.2 配置主服务器（Master）

- 首先，进入到 Master 服务器

  ```bash
   docker exec -it mysql_master /bin/bash
  ```

- 修改配置文件/etc/mysql/mysql.conf.d/mysqld.cnf

  ```bash
  # 在末尾加上两个配置
  
  ## 设置server_id，一般设置为IP的最后一位，同一局域网内注意要唯一
  server_id = 3
  
  ## 开启二进制日志功能，可以随便取，最好有含义（关键就是这里了）
  log-bin = edu-mysql-bin
  ```

- 配置完成后重启 mysql

  ```bash
  service mysql restart
  docker container start
  ```

  > 注意：这个命令会使得容器停止，重新启动就可以了。

- 重启容器进入mysql数据库中创建数据同步用户

  ```bash
  mysql -u root -p 
  Enter password:
  ```

- 创建数据同步用户

  ```bash
  mysql> CREATE USER 'slave'@'%' IDENTIFIED BY '123456';
  mysql> GRANT REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'slave'@'%'; 
  ```

#### 2.3 配置从服务器（Slave）

- 首先，进入到 Master 服务器

  ```bash
   docker exec -it mysql_slave /bin/bash
  ```

- 修改配置文件/etc/mysql/mysql.conf.d/mysqld.cnf

  ```bash
  # 在末尾加上两个配置
  
  ## 设置server_id，一般设置为IP的最后一位，同一局域网内注意要唯一
  server_id = 4
  
  ## 开启二进制日志功能，以备Slave作为其它Slave的Master时使用
  log-bin=edu-mysql-slave-bin  
  ```

- 配置完成后重启mysql，和配置 Master 一样，会使容器停止，需要启动容器。

  ```bash
  service mysql restart
  ```

#### 2.4 完成Master和Slave链接

- 在 Master 进入 MySQL， 然后执行命令：

  ```bash
  mysql -u root -p
  Enter password:
  
  mysql> show master status;
  ```

  结果如下：

  ![image-20210413213229777](C:\Users\apple\AppData\Roaming\Typora\typora-user-images\image-20210413213229777.png)

  记录下 File 和 Position 字段的值，后面会用到。

- 然后到 Slave 中进入 mysql，执行命令：

  ```bash
  mysql -u root -p
  Enter password:
  
  mysql> change master to master_host=' 172.17.0.1 ', master_user='slave', master_password='123456', master_port=3307, master_log_file='edu-mysql-bin.000001', master_log_pos=34659, master_connect_retry=30;
  ```

  命令解释：

  ```bash
  master_host: Master 的IP地址
  master_user: 在 Master 中授权的用于数据同步的用户
  master_password: 同步数据的用户的密码
  master_port: Master 的数据库的端口号
  master_log_file: 指定 Slave 从哪个日志文件开始复制数据，即上文中提到的 File 字段的值
  master_log_pos: 从哪个 Position 开始读，即上文中提到的 Position 字段的值
  master_connect_retry: 当重新建立主从连接时，如果连接失败，重试的时间间隔，单位是秒，默认是60秒。
  ```

- 在 Slave 的 MySQL 终端执行查看主从同步状态

  ```bash
  show slave status \G;
  ```

  <img src="C:\Users\apple\AppData\Roaming\Typora\typora-user-images\image-20210413213602291.png" alt="image-20210413213602291" style="zoom:50%;" align='left'/>

> SlaveIORunning 和 SlaveSQLRunning 是No，表明 Slave 还没有开始复制过程。相反 SlaveIORunning 和 SlaveSQLRunning 是Yes表明已经开始工作了，因为我已经运行过了，所以我的显示的都是 Yes。

- 执行以下命令，开始开启主从同步：

  ```bash
  start slave;
  ```

  







查看容器的ip：` docker inspect 容器名称`

注意：如果停止容器后，在启动。启动不成功，说明容器中的配置文件有语法错误

- 怎么检查配置文件的语法错误？

  ```python
   docker logs 不能启动容器的id
  ```

- 怎么修改配置文件

  - 把容器中错误的配置文件，复制到宿主机

    ```python
     docker cp 容器名称:配置文件的位置 宿主机保存文件的位置
            
          /etc/mysql/mysql.conf.d/mysqld.cnf
    docker cp mysql_master:/etc/mysql/mysql.conf.d/mysqld.cnf /
  ```
  
  - 复制完后，修改配置文件。然后在 复制回容器原来的位置
  
  ```python 
     docker cp 宿主机保存文件的位置 容器名称:配置文件的位置
            
    docker cp /mysqld.cnf mysql_master:/etc/mysql/mysql.conf.d
        docker cp /mysqld.cnf mysql_slave:/etc/mysql/mysql.conf.d
    ```
    
    