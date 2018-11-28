







### python基础 

**一、数据类型和变量** 

* 整数 ：与数学上写法一样。有时候用十六进制表示整数更方便，用0x前缀和0-9，a-f表示，eg: 0xff00, 0xa5b4c3d2.整数运算永远精确

* 浮点数：小数点位置可变，8.18x109 和 81.8x108 完全相等.很大或很小的浮点数，用e代替10，eg: 8.18e9 或 81.8e8，0.000018写成1.8e-5.浮点数运算可能会有四舍五入的误差

* 字符串：‘ ’ 或 " " 括起来的任意文本。

  1.若字符串内部既包含‘又包含“，用转义字符\在'或”前面进行标识。 eg: ' I  \ 'm  \ "OK \ " !'    'I \'m \"OK\" !' 

  2.转义字符\可转义很多字符 \本身也要转义 

  ![1542982499839](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542982499839.png) 

​	3.r' ' 表示' ' 内部字符串默认不转义

​	![1542982679690](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542982679690.png) 

​	4.用'''...'''格式表示多行内容

​	![1542982734911](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542982734911.png) 

* 布尔值：true 、false 

* 空值：None，不能理解为0，一个特殊的空值变量：

* 变量：可任意数据类型

  1.必须以大小写英文、数字和_的组合，不能用数字开头

  2.变量类型本身不固定的语言：动态语言，相对应的是静态语言。静态语言在定义变量时必须指定变量类型

* 常量：不能变的变量

  1.用全部大写的变量名表示常量。PI=3.1415

  2.两种除法

  ​	A. / 结果一定是浮点数

   ![1542983503538](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542983503538.png)   ![1542983542546](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542983542546.png) 

​               B.// 地板除 结果只取整数部分

​	![1542983595550](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542983595550.png) 

​	另外，取余% ![1542983648667](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542983648667.png) 

> > > python的整数、浮点数没有大小限制，但是超出一定范围直接表示为inf(无限大)

**二、字符串和编码**

* 字符编码

  1.Unicode : 把所有语言统一到一套编码里。2个字节

​	2.Ascii：只有127个字符，大小写英文字母、数字和符号。1个字节

​	字母`A`用ASCII编码是十进制的`65`，二进制的`01000001`；

​	字符`0`用ASCII编码是十进制的`48`，二进制的`00110000`，注意字符`'0'`和整数`0`是不同的；

​	3.GB2312：中国制定编进中文

​	4.shift_JIS：日本制定编进日文

​	5.Euc-kr：韩国制定编进韩文

​	6.UTF-8：节省空间

* python的字符串

  1.对于单个字符编码。

  ​	A.用ord()获取字符的整数表示

  ​	![1542984309852](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542984309852.png)  ![1542984208217](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542984208217.png) 

  ​	B. chr()把编码转换为对应字符。

   	![1542984349689](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542984349689.png) ![1542984359023](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542984359023.png) 

  ​	C.知道字符整数编码，可以用十六进制写

  ​        ![1542984547808](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542984547808.png) 

​	2.如果要在网络上传输，或者保存到磁盘上，就需要把`str`变为以字节为单位的`bytes`

​		A.Python对`bytes`类型的数据用带`b`前缀的单引号或双引号表示。

​		B. ’ABC‘ 是skr,一个字符对应若干个字节。b'ABC'每个字符只占用一个字节。

​		C.以Unicode表示的`str`通过`encode()`方法可以编码为指定的`bytes`

​		![1542984878050](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542984878050.png) 

​	3.把`bytes`变为`str`，就需要用`decode()`方法：

​		![1542985606857](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542985606857.png) 

​	4.len()

​		A.计算skr包含多少个字符

​		B.换成bytes,就是计算字节数

 * 格式化 : 

   1.用%格式化字符串

   ​     (’...')%(...)   %x 十六进制整数

   ![1542986075291](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542986075291.png) 

   2.用format()格式化字符串

   ![1542986289854](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542986289854.png) 



> > >当`str`和`bytes`互相转换时，需要指定编码。最常用的编码是`UTF-8`  



**三、使用list 和 tuple**

* list :有序集合，可随时添加和删除其中元素。

  1.用索引来访问list中每一个位置的元素，记得索引是从`0`开始的，最后一个是 `-1`

  ![1542987604240](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542987604240.png) 

​	2.可以往list中追加元素到末尾 .append()

​	3.删除list末尾元素   pop() 删除指定位置pop(i)

​	4.把某个元素替换，直接赋值

* tuple:一旦初始化不可修改

  1.定义只有一个元素的tuple：加一个逗号来消除歧义

  ![1542988082679](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542988082679.png)  定义的不是tuple，而是1这个数。

  括号()既可以表示tuple，又可以表示数学公式中的小括号，产生歧义。

  Python规定，这种情况下，按小括号进行计算，计算结果自然是`1`  ![1542988481231](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542988481231.png)

​	2.可变的tuple

​	![1542988898435](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1542988898435.png) 

​	指向不能变，但list本身可变。

**四、条件判断**

* if else语句：不要少些冒号，从上往下判断

* elif语句：elif = else if 

  ![1543024629993](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1543024629993.png) 

> > > input返回的数据类型是skr，用input()读取用户的输入后，需要先把skr转换成整数

​	![1543025113529](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1543025113529.png) 

**五、循环**

* for...in循环：依次把list或tuple中的每个元素迭代出来

  ![1543025537695](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1543025537695.png) 

  range(): 

  ![1543026009645](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1543026009645.png)

* while循环

* break：提前结束循环

* continue:提前结束本轮循环，并直接开始下一轮循环

> > > 程序陷入“死循环”，可以用`Ctrl+C`退出程序，或者强制结束Python进程

**六、dict和set**

* dict :快速查找，一个key对应一个value

  1.对照表功能:![1543027421588](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1543027421588.png) 

  2.内部直接计算:通过key放入数据 ![1543027397245](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1543027397245.png) 



​	3.避免key错误。

 		A.通过in判断key是否存在 ![1543027501657](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1543027501657.png) 

​		B. 通过dict提供的get()方法，如果key不存在，可以返回none，或者自己指定value

  		返回none时交互环境不显示结果

​		![1543027858336](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1543027858336.png) 

​	4.删除一个key，用pop(key)

​		![1543027677248](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1543027677248.png) 

​	5.dict内部存放的顺序和key放入的顺序是没有关系的

​	6.和list比较，dict有以下几个特点：

​		A.查找和插入的速度极快，不会随着key的增加而变慢；

​		B.需要占用大量的内存，内存浪费多。

​		而list相反：

​		A.查找和插入的时间随着元素的增加而增加；

​		B.占用空间小，浪费内存很少。

7.dict的key必须是**不可变对象**：

​	dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

* set: key的集合，但不存储value

  1.set只告诉你这个set内部有什么元素

  ![1543028439661](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1543028439661.png) 

  2.添加元素到set中，但不会有效果 add(key)

  ![1543028502184](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1543028502184.png) 

  3.删除元素 remove(key)

  ![1543028538378](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1543028538378.png) 

  	4.做数学意义上的交集、并集

​	![1543028628734](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1543028628734.png) 

* 不可变对象

  1.str是不变对象，而list是可变对象。

  2.对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。

   ![1543028863490](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1543028863490.png) ![1543028941806](C:\Users\yxcr0\AppData\Roaming\Typora\typora-user-images\1543028941806.png) 


​	