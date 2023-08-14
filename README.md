# BNU-ChiLab-Webcrawler
爬取北师大汉字全息系统的数据内容

爬取页面：https://qxk.bnu.edu.cn/#/danziDetail   
尝试爬取左侧检索框输入汉字后的返回内容

祖传的爬虫程序，在本机运行时报错。
本人coding水平仅限于简单的Python，debug水平有限，已善用chatgpt，仍希望得到指点。


目前报错内容：
Exception in thread Thread-1 (_readerthread):

Traceback (most recent call last):
  File "D:\Anaconda\Lib\threading.py", line 1038, in _bootstrap_inner
    self.run()
  File "D:\Anaconda\Lib\threading.py", line 975, in run
    self._target(*self._args, **self._kwargs)
  File "D:\Anaconda\Lib\subprocess.py", line 1568, in _readerthread
    buffer.append(fh.read())
                  ^^^^^^^^^
UnicodeDecodeError: 'gbk' codec can't decode byte 0xbf in position 63: illegal multibyte sequence


Traceback (most recent call last):
  File "D:\Testing Table\北师大汉字全息 第一版.py", line 56, in <module>
    res1=execjs.compile(open('decoding.js','r',encoding='UTF-8', errors="ignore").read()).call('jiemi',response.text)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Anaconda\Lib\site-packages\execjs\_abstract_runtime_context.py", line 37, in call
    return self._call(name, *args)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Anaconda\Lib\site-packages\execjs\_external_runtime.py", line 92, in _call
    return self._eval("{identifier}.apply(this, {args})".format(identifier=identifier, args=args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Anaconda\Lib\site-packages\execjs\_external_runtime.py", line 78, in _eval
    return self.exec_(code)
           ^^^^^^^^^^^^^^^^
  File "D:\Anaconda\Lib\site-packages\execjs\_abstract_runtime_context.py", line 18, in exec_
    return self._exec_(source)
           ^^^^^^^^^^^^^^^^^^^
  File "D:\Anaconda\Lib\site-packages\execjs\_external_runtime.py", line 88, in _exec_
    return self._extract_result(output)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Anaconda\Lib\site-packages\execjs\_external_runtime.py", line 156, in _extract_result
    output = output.replace("\r\n", "\n").replace("\r", "\n")
             ^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'replace'
