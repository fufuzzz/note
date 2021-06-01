''''''

'''
1. 异常处理
    try-except
    try-except-else
    try-except-finally
    
    try:
        pass
    except:
        pass
    
    try:
        pass
    except Exception as e:
        pass
        
    主动抛出异常:
        raise NameError()
    
    自定义异常:
        class MyException(Exception):
    
    断言:
        assert n!=0, "报错"

2. 文件操作
    1.打开文件
        打开方式mode
        r: 只读字符串,如果过文件不存在则报错
        rb: 只读二进制,如果文件不存在则报错
        w: 清空写字符串,如果文件不存在则创建
        wb: 清空写二进制,如果文件不存在则创建
        a: 追加写字符串,如果文件不存在则创建
        ab: 追加写二进制,如果文件不存在则创建

        open('filename', 'mode', encoding='utf-8')
        open('filename', 'rb')
        
    2.操作文件
        读取:
            read() 读取所有
            read(10) 读取接下来的10个字符
            readline() 读取接下来的一行
            readlines() 读取所有行,返回列表
            
        写入:
            write()
            write('helo'.encode())
            fp.flush()  # 写入时清空缓存
            
    3.关闭
        fp.close()
    
    4.with-as:
        作用: 让文件自动关闭
        with open() as fp:
            pass

3. csv文件操作
    import csv
    读取器: 
        r.csv.reader()
        for row in r:
            print(row)
    写入器: 
        w.csv.writer()
        w.writerow([])
        writer.writerows([[], [], []])    
    

'''