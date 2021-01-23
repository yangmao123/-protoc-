1、爬取数据流

2、数据流多数为二进制数据，将数据保存为data.bin文件

3、将protocol以及自己写的爬虫代码放一起，exe以及bin文件等需要在同一个文件夹下

复制bin文件到protocol Buffers软件下,执行命令，生成text.txt文件

protocol Buffers v3.14.0（C++）教程链接：https://github.com/protocolbuffers/protobuf/releases/

protobuf协议逆向解析--APP爬虫：https://www.yuanrenxue.com/app-crawl/parse-protobuf.html

protoclo Buffer Basics(Python)：https://developers.google.com/protocol-buffers/docs/pythontutorial#compiling-your-protocol-buffers

protobuf3语法指南：https://colobu.com/2017/03/16/Protobuf3-language-guide/


命令：1. protoc --decode_raw < data.bin  >text.txt


      2. protoc --python_out=. argis.proto
      
5、生成plythoy文件

6、复制plythoy到工程文件下（爬虫的工程文件）

其中ins，dsfsdd，d都是proto里面定义的

7、尝试改count（get里面的请求参数），得先删掉原来已有的bin文件，此时每次只能爬取2000个数据

8、输出的数据文件，利用标号标记数据：每个15以下对应的都是数据。

其中大多数的加密数据都是倍数关系

例如：时间戳，需要÷1000再÷2

利用标号标记的每列数据，问题：出现了多个1（本来应该只有一个），使用list保存

4：÷2

9、导出数据

