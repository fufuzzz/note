# Linux命令

####Linux常用命令

#####1.命令常用方法

Linux命令格式:

```shell
command  [-options]  [parameter1]  …
```

 说明：

command: 命令名,相应功能的英文单词或单词的缩写

[-options]：选项,可用来对命令进行控制，也可以省略，`[]代表可选`

parameter1 …：传给命令的参数：可以是零个，一个或多个

> 例如：

```
ls -a ./
```

#####2.查看帮助文档

######1. --help

一般是linux命令自带的帮助信息

> 例如：

```
ls --help
```

######2. man(有问题找男人，manual使用手册)

man是linux提供的一个手册，包含了绝大部分的命令、函数使用说明

该手册分成很多章节（section），使用man时可以指定不同的章节来浏览。

例：man ls ; man 2 printf 

man设置了如下的功能键：

| 功能键    | 功能         |
| ------ | ---------- |
| 空格键    | 显示手册页的下一屏  |
| Enter键 | 一次滚动手册页的一行 |
| b      | 回滚一屏       |
| f      | 前滚一屏       |
| q      | 退出man命令    |
| h      | 列出所有功能键    |
| /word  | 搜索word字符串  |

> 例如：

```
man ls
```

##### 3. 自动补全：

在敲出命令的前几个字母的同时，按下tab键，系统会自动帮我们补全命令

#####4. 历史命令：

当系统执行过一些命令后，可按上下键翻看以前的命令，history将执行过的命令列举出来



#### 2. Linux命令-文件、磁盘管理

#####1.文件管理

#####1>查看文件信息：ls

ls是英文单词list的简写，其功能为列出目录的内容，是用户最常用的命令之一，它类似于DOS下的dir命令。

`Linux文件或者目录名称最长可以有265个字符，“.”代表当前目录，“..”代表上一级目录，以“.”开头的文件为隐藏文件，需要用 -a 参数才能显示。`

ls常用参数：

| 参数   | 含义                     |
| ---- | ---------------------- |
| -a   | 显示指定目录下所有子目录与文件，包括隐藏文件 |
| -l   | 以列表方式显示文件的详细信息         |
| -h   | 配合 -l 以人性化的方式显示文件大小    |

> 例如：

```
ls -a
ll: 相当于ls -la
```

![01-linux基础-31](./01-linux基础-31.png)

 

在Unix/Linux系统中，也同样允许使用特殊字符来同时引用多个文件名，这些特殊字符被称为通配符。

| 通配符       | 含义                                       |
| --------- | ---------------------------------------- |
| *         | 文件代表文件名中所有字符                             |
| ls te*    | 查找以te开头的文件                               |
| ls *html  | 查找结尾为html的文件                             |
| ？         | 代表文件名中任意一个字符                             |
| ls ?.c    | 只找第一个字符任意，后缀为.c的文件                       |
| ls a.?    | 只找只有3个字符，前2字符为a.，最后一个字符任意的文件             |
| [ ]       | [”和“]”将字符组括起来，表示可以匹配字符组中的任意一个。“-”用于表示字符范围。 |
| [abc]     | 匹配a、b、c中的任意一个                            |
| [a-f]     | 匹配从a到f范围内的的任意一个字符                        |
| ls [a-f]* | 找到从a到f范围内的的任意一个字符开头的文件                   |
| ls a-f    | 查找文件名为a-f的文件,当“-”处于方括号之外失去通配符的作用         |
| \         | 如果要使通配符作为普通字符使用，可以在其前面加上转义字符。“?”和“*”处于方括号内时不用使用转义字符就失去通配符的作用。 |
| ls  \\*a  | 查找文件名为*a的文件                              |

#####2>输出重定向命令： >    >> 

Linux允许将命令执行结果重定向到一个文件，本应显示在终端上的内容保存到指定文件中。

如：ls > test.txt ( test.txt 如果不存在，则创建，存在则覆盖其内容 )

注意： `>输出重定向会覆盖原来的内容，>>输出重定向则会追加到文件的尾部。`

>例如：

```shell
ls  >  demo.txt
```

#####2-1>  显示文件内容／合并文件内容：cat

```shell
#显示文件内容
cat filename
```

```shell
#将file1与file2的内容合并到file3文件中
cat file1 file2 > file3
```

#####2-2> 创建文件： touch  文件名

#####3> 分屏显示：more

查看内容时，在信息过长无法在一屏上显示时，会出现快速滚屏，使得用户无法看清文件的内容，此时可以使用more命令，每次只显示一页，按下空格键可以显示下一页，按下q键退出显示，按下h键可以获取帮助。

```shell
more demo.txt
```

#####4>管道：|   

管道：一个命令的输出可以通过管道做为另一个命令的输入。

管道我们可以理解现实生活中的管子，管子的一头塞东西进去，另一头取出来，这里“ | ”的左右分为两端，左端塞东西(写)，右端取东西(读)。 

```shell
ls -lh | more
#通过管道我们可以写两个命令，前面的命令的输出是后面命令输入的内容，最后显示后面命令的输出
```

#####5>清屏：clear

clear作用为清除终端上的显示(类似于DOS的cls清屏功能)，也可使用快捷键：Ctrl + l ( “l” 为字母 )。

注意：这个清除屏幕并不是删除之前的内容，而是让我们的屏幕向上滚动一页。

#####6>切换工作目录： cd

在使用Unix/Linux的时候，经常需要更换工作目录。cd命令可以帮助用户切换工作目录。`Linux所有的目录和文件名大小写敏感`

cd后面可跟绝对路径，也可以跟相对路径。如果省略目录，则默认切换到当前用户的主目录。

| 命令    | 含义                                       |
| ----- | ---------------------------------------- |
| cd    | 切换到当前用户的主目录(/home/用户目录)，用户登陆的时候，默认的目录就是用户的主目录。 |
| cd ~  | 切换到当前用户的主目录(/home/用户目录)                  |
| cd .  | 切换到当前目录                                  |
| cd .. | 切换到上级目录                                  |
| cd -  | 可进入上次所在的目录                               |

注意：

如果路径是从根路径开始的，则路径的前面需要加上 “ / ”，如 “ /mnt ”，通常进入某个目录里的文件夹，前面不用加 “ / ”。

根目录：／

家目录：～



#####7>显示当前路径：pwd

使用pwd命令可以显示当前的工作目录，该命令很简单，直接输入pwd即可，后面不带参数。

#####8>创建目录：mkdir

通过mkdir命令可以创建一个新的目录。参数-p可递归创建目录。

需要注意的是新建目录的名称不能与当前目录中已有的目录或文件同名，并且目录创建者必须对当前目录具有写权限。

```shell
mkdir -p  a/b/c 
```

##### 9>删除目录：rmdir(一般不用)

可使用rmdir命令删除一个目录。必须离开目录，并且目录必须为空目录，不然提示删除失败。

#####10>删除文件：rm（常用）

可通过rm删除文件或目录。使用rm命令要小心，因为文件删除后不能恢复。为了防止文件误删，可以在rm后使用-i参数以逐个确认要删除的文件。

常用参数及含义如下表所示：

| 参数   | 含义                      |
| ---- | ----------------------- |
| -i   | 以进行交互式方式执行              |
| -f   | 强制删除，忽略不存在的文件，无需提示      |
| -r   | 递归地删除目录下的内容，删除目录时必须加此参数 |



#####11>建立链接文件：ln

Linux链接文件类似于Windows下的快捷方式。

链接文件分为软链接和硬链接。

软链接：软链接不占用磁盘空间，源文件删除则软链接失效。

硬链接：硬链接只能链接普通文件，不能链接目录。

使用格式：

```
ln 源文件 链接文件
ln -s 源文件 链接文件
```

如果`没有-s`选项代表建立一个硬链接文件，两个文件占用相同大小的硬盘空间，即使删除了源文件，链接文件还是存在，所以-s选项是更常见的形式。

注意：如果软链接文件和源文件不在同一个目录，源文件要使用绝对路径，不能使用相对路径。

在linux中，文件名与文件的数据是分开保存的。

使用软连接的时候，类似于window中创建的快捷方式，当你将源文件删除的时候，软连接就失效了。

使用硬连接的时候，相当于复制了一份与源文件相同的文件大小，但是他又不是复制，因为当我们使用硬连接进行操作文件的时候，我们发现与硬连接相关的文件全部都会发生变化。

总结：

1.给目录只能创建软连接，无法创建硬连接，因为不支持。

2.当给文件创建软连接的时候，若源文件与链接文件不在同一个目录下，我们必须使用绝对路径，若使用相对路径，一旦挪动连接文件的位置，则此链接就会失效，使用绝对路径不会出现这种情况。

```
1.尝试分别给目录添加软连接与硬连接
2.若创建的软连接文件与源文件不在同一个目录，分别使用绝对路径与相对路径区别
```



#####12>查看或者合并文件内容：cat

```shell
cat  demo.txt
```
```shell
cat demo.txt > demo2.txt  #覆盖写
cat demo.txt >> demo2.txt  #追加写
#写在左边不发生变化，写在右边的会发生变化
```

#####13>文本搜索：grep

Linux系统中grep命令是一种强大的文本搜索工具，grep允许对文本文件进行模式查找。如果找到匹配模式， grep打印包含模式的所有行。

grep一般格式为：

```
grep [-选项] ‘搜索内容串’ 文件名
```

在grep命令中输入字符串参数时，最好引号或双引号括起来。例如：grep ‘a ’ 1.txt。

常用选项说明：

| 选项   | 含义                   |
| ---- | -------------------- |
| -v   | 显示不包含匹配文本的所有行（相当于求反） |
| -n   | 显示匹配行及行号             |
| -i   | 忽略大小写                |

grep搜索内容串可以是正则表达式。

正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑。

grep常用正则表达式：

| 参数           | 含义                                       |
| ------------ | ---------------------------------------- |
| ^a           | 行首,搜寻以 a开头的行；grep -n '^a' 1.txt          |
| ke$          | 行尾,搜寻以 ke 结束的行；grep -n 'ke$' 1.txt       |
| [Ss]igna[Ll] | 匹配 [] 里中一系列字符中的一个；搜寻匹配单词signal、signaL、Signal、SignaL的行；grep -n '[Ss]igna[Ll]' 1.txt |
| .            | (点)匹配一个非换行符的字符；匹配 e 和 e 之间有任意一个字符，可以匹配 eee，eae，eve，但是不匹配 ee，eaae；grep -n 'e.e' 1.txt |

> 例如：

```
grep -n ‘^a’ demo.txt
```

```
grep -n 'm$' demo.txt
```

```
grep -n 't[xn]t' demo.txt
```



#####14>查找文件：find

find命令功能非常强大，通常用来在特定的目录下搜索符合条件的文件，也可以用来搜索特定用户属主的文件。

常用用法：

| 命令                          | 含义                    |
| --------------------------- | --------------------- |
| find ./ -name test.sh       | 查找当前目录下所有名为test.sh的文件 |
| find ./ -name '*.sh'        | 查找当前目录下所有后缀为.sh的文件    |
| find ./ -name "[A-Z]*"      | 查找当前目录下所有以大写字母开头的文件   |
| find /tmp -size 2M          | 查找在/tmp 目录下等于2M的文件    |
| find /tmp -size +2M         | 查找在/tmp 目录下大于2M的文件    |
| find /tmp -size -2M         | 查找在/tmp 目录下小于2M的文件    |
| find ./ -size +4k -size -5M | 查找当前目录下大于4k，小于5M的文件   |
| find ./ -perm 0777          | 查找当前目录下权限为 777 的文件或目录 |

注意：使用find进行查找的时候，查找指定目录以及子目录下所有符合条件的文件

使用特殊符号的时候，我们需要将使用单引号或者双引号给扩起来。



#####15>拷贝文件：cp

cp命令的功能是将给出的文件或目录复制到另一个文件或目录中，相当于DOS下的copy命令。

常用选项说明：

| 选项   | 含义                                       |
| ---- | ---------------------------------------- |
| -a   | 该选项通常在复制目录时使用，它保留链接、文件属性，并递归地复制目录，简单而言，保持文件原有属性。 |
| -f   | 已经存在的目标文件而不提示                            |
| -i   | 交互式复制，在覆盖目标文件之前将给出提示要求用户确认               |
| -r   | 若给出的源文件是目录文件，则cp将递归复制该目录下的所有子目录和文件，目标文件必须为一个目录名。 |
| -v   | 显示拷贝进度                                   |

> 例如：

```
语法：
cp  [-选项]  源文件   目标文件
```

```
cp  -ivr   a/b/cc.txt    a/ceshi.txt
```

注意：当目标文件存在并且是目录的时候，会将其复制到该目录下，若存在，但是不是目录则报错，

若不存在，不报错，复制并且重命名。

> 创建一个目录aa，aa下有一个bb，bb下有一个cc还有一个hello.py文件，cc下面有一个
>
> test.txt文件与一个123.txt文件
>
> 要求：将aa目录复制并且重命名为dir1，查看123.txt文件中包含数字的行，并且删除hello.py



#####16> 移动文件：mv

用户可以使用mv命令来移动文件或目录，也可以给文件或目录重命名。

常用选项说明：

| 选项   | 含义                                       |
| ---- | ---------------------------------------- |
| -f   | 禁止交互式操作，如有覆盖也不会给出提示                      |
| -i   | 确认交互方式操作，如果mv操作将导致对已存在的目标文件的覆盖，系统会询问是否重写，要求用户回答以避免误覆盖文件 |
| -v   | 显示移动进度                                   |

> 例如：

```
mv  [-选项]  源文件  目标文件 
```

若目标文件存在并且是目录的情况下，则将源文件移动到指定目录下，若目标文件存在但是不是目录，则源文件覆盖目标文件，

若目标文件不存在，则将源文件进行重命名。



#####17>归档管理：tar

计算机中的数据经常需要备份，tar是Unix/Linux中最常用的备份工具，此命令可以把一系列文件归档到一个大文件中，也可以把档案文件解开以恢复数据。

tar使用格式

 tar  [选项]   打包文件名   文件

tar命令很特殊，其选项前面可以使用“-”，也可以不使用。

常用参数：

| 参数   | 含义                              |
| ---- | ------------------------------- |
| -c   | 生成档案文件，创建打包文件                   |
| -v   | 列出归档解档的详细过程，显示进度                |
| -f   | 指定档案文件名称，f后面一定是.tar文件，所以必须放选项最后 |
| -x   | 解开档案文件                          |

注意：除了f需要放在参数的最后，其它参数的顺序任意。

> 例如：

```
tar -cvf  test.tar *
```

##### 18>文件压缩解压：gzip

tar与gzip命令结合使用实现文件打包、压缩。 tar只负责打包文件，但不压缩，用gzip压缩tar打包后的文件，其扩展名一般用xxxx.tar.gz。

gzip使用格式如下：

```shell
gzip  [选项]  被压缩文件
```

常用选项：

| 选项   | 含义      |
| ---- | ------- |
| -d   | 解压      |
| -r   | 压缩所有子目录 |

 tar这个命令并没有压缩的功能，它只是一个打包的命令，但是在tar命令中增加一个选项(-z)可以调用gzip实现了一个压缩的功能，实行一个先打包后压缩的过程。

1. 压缩用法：tar cvzf 压缩包包名 文件1 文件2 ...

```
-z ：指定压缩包的格式为：file.tar.gz
```

2. 解压用法： tar zxvf 压缩包包名

```
-z:指定压缩包的格式为：file.tar.gz
```

>例如：

```shell
#打包并压缩文件
tar -zcvf test.tar.gz  *
#解压到当前路径下
tar -zxvf test.tar.gz
#解压到指定目录下
tar -zxvf test.tar.gz -C  a/
```

> 需求：将桌面包含数字的文件名以及目录进行打包压缩，命名为new.tar.gz ,并且将其解压到aa/bb/cc,查找以.txt结尾的文件，并且删除。



#####19>文件压缩解压：bzip2

tar与bzip2命令结合使用实现文件打包、压缩(用法和gzip一样)。

tar只负责打包文件，但不压缩，用bzip2压缩tar打包后的文件，其扩展名一般用xxxx.tar.bz2。

在tar命令中增加一个选项(-j)可以调用bzip2实现了一个压缩的功能，实行一个先打包后压缩的过程。

压缩用法：tar -jcvf 压缩包包名 文件...(tar jcvf bk.tar.bz2   *.c)

解压用法：tar -jxvf 压缩包包名 (tar jxvf bk.tar.bz2)



#####20>文件压缩解压：zip、unzip

通过zip压缩文件的目标文件不需要指定扩展名，默认扩展名为zip。

压缩文件：zip  -r  目标文件(没有扩展名) 源文件

解压文件：unzip -d 解压后目录文件 压缩文件

> 例如：

```shell
#压缩文件
zip -r myzip *
#解压文件到指定路径
unzip -d ./test  myzip.zip
```

#####21> 查看命令位置：which

```
which ls
```

##### 22> 查看目录结构：tree

##### 23>  tail命令 – 查看文件尾部内容 

> tail用于显示文件尾部的内容，默认在屏幕上显示指定文件的末尾10行。如果给定的文件不止一个，则在显示的每个文件前面加一个文件名标题。如果没有指定文件或者文件名为“-”，则读取标准输入。

**参考实例**

显示文件file的最后10行：

```shell
[root@ubuntu ~ ]#  tail file
```

显示文件file的内容，最后20行：

```shell
[root@ubuntu ~ ]#  tail -n 20 file 
```

显示文件file的最后10个字符：

```shell
[root@ubuntu ~ ]#  tail -c 10 file 
```

##### 24> echo命令 – 输出字符串或提取Shell变量的值

> echo命令用于在终端设备上输出字符串或变量提取后的值

**语法格式：**echo [参数][字符串]

**参考实例**

输出一段字符串： 

```shell
[root@ubuntu ~]#  echo "LinuxCool.com" 
LinuxCool.com 
```

输出变量提取后的值：

```shell
[root@ubuntu ~]# echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin
```

对内容进行转义，不让$符号的提取变量值功能生效：

```shell
[root@ubuntu ~]# echo \$PATH
$PATH
```

结合输出重定向符，将字符串信息导入文件中：

```shell
[root@ubuntu ~]# echo "It is a test" > linuxcool
```

##### 25> less命令 – 分页显示工具

> 浏览文字档案的内容，用less命令显示文件时，PageUp键向上翻页，PageDown键向下翻页，要退出less程序，应按Q键。

> less的作用与more十分相似，不同点为less命令允许用户向前或向后浏览文件，而more命令只能向前浏览 

命令内部操作：

- h 显示帮助界面
- Q 退出less 命令

- b 向上翻一页
- d 向下翻半页
- u 向上翻半页
- y 向上翻一行
- f 向下翻一页
- 空格键 滚动一页
- 回车键 滚动一行

**参考实例**

查看文件 ：

```shell
[root@linuxcool ~]# less test.php
```

ps查看进程信息并通过less分页显示：

```shell
[root@linuxcool ~]# ps -ef |less 
# 查看指定进程：ps -ef | grep 'firefox'
# 杀死进程： kill -9 pid
```

查看命令历史使用记录并通过less分页显示：

```shell
[root@linuxcool ~]# history | less 
22  scp -r tomcat6.0.32 root@192.168.120.203:/opt/soft 23  cd .. 
24  scp -r web root@192.168.120.203:/opt/ 
25  cd soft  
……省略……
```

##### 26> wc命令 – 统计文件的字节数、字数、行数

> wc命令统计指定文件中的字节数、字数、行数，并将统计结果显示输出。利用wc指令我们可以计算文件的Byte数、字数或是列数，若不指定文件名称，或是所给予的文件名为“-”，则wc指令会从标准输入设备读取数据。wc同时也给出所指定文件的总统计数

**语法格式：**wc [参数][文件]

**常用参数：**﻿

| -w   | 统计字数，或–words：只显示字数。一个字被定义为由空白、跳格或换行字符分隔的字符串 |
| ---- | ---------------------------------------- |
| -c   | 统计字节数，或–bytes或–chars：只显示Bytes数           |
| -l   | 统计行数，或–lines：只显示列数                       |
| -m   | 统计字符数                                    |
| -L   | 打印最长行的长度                                 |

**参考实例**

统计字数：

```shell
[root@linuxcool ~]# cat test.txt 
 hello world
 hello world
 hello world
 hello world hello world
 [root@linuxcool ~]# wc -w test.txt 
 10 test.txt
```

统计字节数：

```shell
[root@linuxcool ~]# wc -c test.txt 
 60 test.txt
```

统计字符数：

```shell
[root@linuxcool ~]# wc -m test.txt 
 60 test.txt
```

统计行数：

```shell
[root@linuxcool ~]# wc -l test.txt 
 4 test.txt
```

打印最长行的长度：

```shell
[root@linuxcool ~]# wc -L test.txt 
 23 test.txt
```