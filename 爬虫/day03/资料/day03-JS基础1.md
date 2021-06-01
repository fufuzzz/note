## 第3天_JavaScript基础

### 1. 学习目标

- JavaScript介绍和引入
- JavaScript变量和数据类型
- JavaScript运算符
- JavaScript分支与循环

### 2. JavaScript介绍和引入

#### 2.1 JavaScript介绍

- JavaScript 的诞生  

   JavaScript 诞生于 1995 年。由Netscape(网景公司)的程序员Brendan Eich(布兰登)与Sun公司联手开发一门脚本语言,  最初名字叫做Mocha，1995年9月改为LiveScript。12月，Netscape公司与Sun公司（Java语言的发明者）达成协议，后者允许将这种语言叫做JavaScript。这样一来，Netscape公司可以借助Java语言的声势。1996年3月， Netscape公司的浏览器Navigator 2.0浏览器正式内置了JavaScript脚本语言.  此后其他主流浏览器逐渐开始支持JavaScript.  谷歌浏览器，火狐浏览器， IE浏览器， 欧朋浏览器， Safari浏览器

- JavaScript组成： 

     - ECMAScript :  包含JS语法   	 
     - BOM ： Brower Object Model  和浏览器相关的操作 

     - DOM ： Document Object Model  和页面内容相关的操作

- JavaScript版本：

     ​	ES5, ES6, ES2020



#### 2.2 JavaScript引入

- 导入内部JavaScript: 

  ```html
  <script type="text/javascript"></script>
  ```

- 在标签中间写js代码: 

  第一句javascript代码：alert(“hello world!”) ;     

  第二句javascript代码：document.write(“亲，我在页面上，跟alert不一样噢！”);    

  第三句javascript代码：console.log(“我是在控制台打印的, 以后常用我！”); 

  注意: document.write可以输出任何HTML的代码

- script标签

  - script标签可以出现多次, 且可以出现在html文件的任何地方
  - 同一个文件中Javascript和HTML代码, 它们的执行顺序都是自上而下，谁在前就谁先执行, 谁在后就后执行.

- JavaScript的注释     

  - 单行注释: // 
  - 多行注释 /* */

- 外部javaScript文件引入：

  ```html
  <script type="text/javascript" src="demo1.js" ></script>
  ```

  注意： 

  - 在引入了外部文件的标签中写代码会无效
  - src 表示要引入的外部文件


### 3.JavaScript变量和数据类型

#### 3.1 JavaScript变量

- 变量定义(使用var关键字)：

  ```
  var age;       
  ```

-  赋值：       

  ```javascript
  age = 20; 
  ```

- 定义的同时赋值：      

  ```javascript
  var age = 20；
  ```

- 可以一次定义多个变量：       

  ```javascript
  var name="zhangsan", age=18, weight=108;
  ```

- JS是弱数据类型的语言，容错性较高, 在赋值的时候才确定数据类型      

  ```javascript
  var temp;           //temp是什么数据类型？不确定      
  temp = 12;            //temp变量是数字类型      
  temp = "hello";      //temp变量变成了字符串类型      
  console.log(typeof temp);  // 查看temp数据类型
  ```

- 变量的命名规范
  - 变量名可以是数字,字母,下划线_和 **美元符 `$ `**组成;
  - 第一个字符不能为数字
  - 不能使用关键字或保留字
  - 标识符区分大小写，如：age和Age是不同的变量。但强烈不建议用同一个单词的大小写区分两个变量。
  - 变量命名尽量遵守驼峰原则: myStudentScore小驼峰， 大驼峰MyStudentScore
  - 变量命名尽量见名思意, age,  users 数组


#### 3.2 JavaScript数据类型

- JS数据类型一般可以分为:      

  - Boolean: 布尔类型 : true, false      
  - Number：数字（整数int，浮点数float）     
  - String：字符串      
  - Object：对象{ }  数组Array [ ]   

  特殊数据类型        

  - Null         
  - Undefined

  注意: 变量的类型在赋值时才能确定

- ##### Undefined类型:       

  Undefined 类型只有一个值，即特殊的 undefined。

  在使用 var 声明变量，但没有对其初始化时，这个变量的值就是 undefined

  例如: 

  ```javascript
  var b;  
  console.log(b);  //undefined
  ```

  注意: 我们在定义变量的时候， 尽可能的不要只声明，不赋值, 而是声明的同时初始化一个值。

- ##### Null 类型:       

  Null 类型是一个只有一个值的数据类型，即特殊的值 null。

  它表示一个空对象引用(指针)，而 typeof 操作符检测 null 会返回 object。

   例如: 

  ```javascript
  var b = null;   
  console.log(typeof b);
  ```

  注意： undefined 是派生自 null 的，因此 ECMA-262 规定对它们的相等性测试返回 true, 表示值相等， 但是两者的数据类型是不一样的。

  例如:

  ```javascript
  console.log(undefined == null);  //true
  var b，car = null;   
  console.log(typeof b== typeof car);  //false
  ```

- ##### Boolean类型:       

  Boolean 类型有两个值：true和false。

  而true一般等于1，false一般等于0。 

  JavaScript 是区分大小写的，True和False或者其他都不是Boolean类型的值。

  例如:

  ```javascript
  var b= true;  
  console.log(typeof b);    
  ```

  Boolean 类型的转换规则: (牢记)	

  - String: 非空字符串为true, 空字符串为false     	


  - Number: 非0数值为true, 0或者NaN为false        
  - Object: 对象不为null则为true, null为false 
  - Undefined : undefined为false       

- ##### Number类型:      

  Number 类型包含两种数值：整型和浮点型. 

  - 整型:

  ```js
  var b = 100;    
  console.log(b);
  ```

  - 浮点类型: 

  ```js
  var b = 3.8;
  var b = 0.8;
  var b = .8;	//有效，但不推荐此写法
  ```

  由于保存浮点数值需要的内存空间比整型数值大两倍，因此 ECMAScript 会自动将可以 转换为整型的浮点数值转成为整型。 整数: 4字节， float: 8字节   

  常见单位换算： 

  ​	1位=0/1， 

  ​	1byte=8位  

  ​	1kb=1024byte, 

  ​	1MB=1024kb,

  ​	1GB=1024MB, 

  ​	1TB=1024GB, 

  ​	1PB=1024TB, 

  ​	1EB=1024PB,... 

  ```js
  var b = 8.0;	//小数点后面没有值，转换为8
  var b = 12.0;	//小数点后面是0，转成为12对于那些过大或过小的数值，
  ```

  ##### 科学技术法: 

  ​	用 e 表示该数值的前面 10 的指数次幂。

   ```js
  var box = 4.12e5;	//即 412000
  var box = 0.0000412;	//即 4.12e-5
   ```

  浮点数值的范围在：Number.MIN_VALUE ~ Number.MAX_VALUE 之间, 如果超过了浮点数值范围的最大值或最小值，那么就先出现 Infinity(正无穷)或-Infinity(负无穷)。


##### NaN: 


  	即非数值(Not a Number)是一个特殊的值     
  	
  	这个数值用于表示一个本来要返回数值的操作数未返回数值的情况(这样就不会抛出错误了)。

  - 比如: 

    - 在其他语言中,  任何数值除 以 0 都会导致错误而终止程序执行。但在ECMAScript中，会返回出特殊的值，因此不会影响程序执行。

      ```js
      var b = 0/0;    //NaN
      var b = 12/0;  //Infinity
      var b = 12/0 * 0;  //NaN
      ```

    ECMAScript 提供了 isNaN()函数，用来判断是不是 NaN。isNaN()函数在接收到一个值之后，会尝试将这个值转换为数值。

    ```js
    console.log(isNaN(NaN));   //true
    console.log(isNaN(25));	  //false，25 是一个数值
    console.log(isNaN('25'));   //false，'25'是一个字符串数值，可以转成
    console.log(isNaN('zhangsan'));     //true，'zhangsan'不能转换为数值
    console.log(isNaN(true));        //false   => true 可以转成成 1
    ```

- ##### 数据类型转换：

  字符串转换数字类型：     

  - parseInt()      是把其它类型转换为整型     
    - 字符串转数字
      - 如果是以数字开头,会保留数字部分,省略字符串部分
        - 比如:parseInt('12abc') 结果是12
      - 如果是以字符串开头,将不能转换成整型,结果是Nan
        - 比如:parseInt('abc12')
  - parseFloat()  是把其它类型转换为浮点型（小数）    
    - 字符串转浮点型,转换的方式和字符串转整型一样的


### 4. JavaScript运算符

#### 4.1 JS运算符归纳

- 算术运算符 ：` +，-, *, /, %(取余数)`
- *字符串和变量的拼接：` +`*
- *关系运算符 ： `<、>、<=、>=、==、===、!=, !==`*
- *逻辑运算符 ： `&&  与(且)、||  或、! `*
- 赋值运算符和复合运算符 ：`  =、+=、-=、*=、/=、%=`
- 一元运算符（自增、自减） ：` ++a, a++, --a, a--`
- 三目运算符： `? : `

#### 4.2 一元运算符

- 一元运算符： 

   只有一个操作数的运算符

- 例如：

  ```js
  var a = ++b;  //加后取值 先执行加法运算, 再取值	
  var a = b++; //加前取值 先取值, 再执行加法运算
  ```

#### 4.3 关系运算符      

- 关系运算符: 

  用于进行比较的运算符. 

- 关系运算符有:  

  小于(<)、大于(>)、小于等于(<=)、大于等于(>=)、相等(`==`)、不等(!=)、全等(恒等)(`===`)、不全等(不恒等)(!==) 

  ===是判断值和类型

- 关系运算符的比较规则:      
  - 数字和数字比较, 直接比较大小     
  - 数字和字符串比较, 字符串转换为数字后再比较     
  - 字符串和字符串比较, 进行字符的ASCII码值比较  
  
- 注意事项:     
  - 布尔值 ture=1, false=0     
  - 只要不等于NaN, 就是true,其他有NaN的运算都为false     
  - 如果要恒等, 则必须值和类型都要相等;

关系运算符特殊值：

NaN:不是一个特定值,它代表除了数字之外的所有其他值

| 运算                | 值     |
| ----------------- | ----- |
| null == undefined | true  |
| 'NaN' == NaN      | false |
| 5 == NaN          | false |
| NaN == NaN        | false |
| false == 0        | true  |
| true == 1         | true  |
| true == 2         | false |
| undefined == 0    | false |
| null == 0         | false |
| '100' == 100      | true  |
| '100' === 100     | false |

#### 4.4 逻辑运算符      

​	逻辑与 &&：

​		短路操作，如果第一个操作数返回是 false，第二个数不管是true还是false都会返回false。      

​	逻辑或|| ： 

​		短路操作，当第一操作数的求值结果为 true， 就不会对第二个操作数求值了。       

​	逻辑非(NOT)：! 


#### 4.5 赋值运算符:      

​	如: +=, -=, *=,  /=, %= 等


#### 4.6 三目运算符:   

​	三目运算符符号： ?  : 

​	格式:判断条件 ? 条件为true的值:条件为false的值

例如：

```javascript
var b = true ? 10 : 20 
// 结果b的值是10
```




### 5. 分支语句

#### 5.1 if分支

- if单分支: 

  ```js
  if （1） {
    console.log(1);
  }
  ```

- if双分支

  ```js
  if (a >= 18) {
    console.log("成年了");
  }
  else {
    console.log("小屁孩");
  }
  ```

- if多分支


  ```js
  if (score >= 90) {
    console.log("成绩优秀");
  }
  else if (score >= 60) {
    console.log("及格了");
  }
  else {
    console.log("不及格");
  }
  ```

  练习： 

  	1. 判断一个数是偶数还是奇数	；     

  ​	2. 求两个数的最大数；      

  ​	3. 判断一个年份是闰年还是平年； 	

  ​	（ 满足两种情况中的一种即为闰年： 

  ​		a.能被4整除而不能被100整除.（如2004年就是闰年,1800年不是.）	    

  ​		b.能被400整除.（如2000年是闰年）

  ​	  ）

  ​	4.开发一款软件，根据公式（身高-108）*2=标准体重，可以有10斤左右的浮动。来观察测试者体重是否合适

  	5.成绩判定(大于85 优秀;  大于等于75小于等于85 良好;	大于等于60小于75 及格;  小于60  不及格;)

#### 5.2 switch分支(扩展)

```js
var grade = "A";
switch(grade) {
  case "A":
  	console.log("优秀");
  	break;
  case "B":
  	console.log("良好");
  	break;
  case "C":
  	console.log("一般");
  	break;
  default: 
  	console.log("其他情况");
}
```

#### 5.3 循环

- ##### while循环

  ```js
  // 计算1+2+...+100
  var i = 1;
  var sum = 0;
  while (i <= 100) {
    sum += i;
    i++;
  }
  console.log(sum);
  ```

- ##### for循环

  ```js
  // 计算1+2+...+100
  var sum = 0;
  for (var i=1; i<=100; i++) {
    sum += i;
  }
  console.log(sum);
  ```

- ##### for-in循环

  JavaScript中的for-in：从头遍历到尾，需要提供现成的数组

  ```js
  var arr = [1,2,3,4]
  for (var i in arr) {
    console.log(i, arr[i]);
  }
  
# 循环的变量i是下标不是值
  ```

  练习:     

  ​	1, 判断一个数是不是合数。

  ​		(指自然数中除了能被1和本身整除外，还能被其他的数整除（不包括0)的数。)   

  ​	2, 判断一个数是不是素数。
  
  ​		(除了1和它本身以外不再有其他的除数整除。)












