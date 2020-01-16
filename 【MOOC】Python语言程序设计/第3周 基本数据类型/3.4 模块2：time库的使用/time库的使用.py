import time

# time.time() 获得当前时间戳，即计算机内部时间值，浮点数
print(time.time())  

# time.ctime() 获取当前时间并以易读方式表示，返回字符串
print(time.ctime())

# 获取当前时间，表示为计算机可处理的时间格式
print(time.gmtime())



'''
时间格式化，将时间以合理的方式展示出来
  -格式化：类似字符串格式化，需要有展示模板
  -展示模板由特定的格式化控制符组成
  -strftime(tpl,ts)   tpl是格式化模板字符串，用来定义输出效果
                      ts是计算机内部时间类型变量
    >>>t = time.gmtime()
    >>>time.strftime("%Y-%m-%d %H:%M:%S",t)
    "2018-01-26 12:55:20"
'''
t = time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",t)) # 结果是12小时制
'''
%Y    年份         0000~9999，例如：1900
%m    月份         01~12，例如：10
%B    月份名称     January~December，例如：April
%b    月份名称缩写 Jan~Dec，例如：Apr
%d    日期         01~31，例如：25
%A    星期         Monday~Sunday，例如：Wednesday
%a    星期缩写     Mon~Sun，例如：Wed
%H    小时（24h制）00~23，例如：12
%h    小时（12h制）01~12，例如：7
%p    上/下午      AM,PM，例如：PM
%M    分钟         00~59，例如：26
%S    秒           00~59，例如：26
'''


'''
程序计时
  -测量时间：perf_counter() 返回一个CPU级别精确时间计数值，单位是秒
                            由于这个计数值起点不确定，连续调用差值才有意义
             >>>start = time.perf_counter()
             318.66599499718114
             >>>end = time.perf_counter()
             341.3905185375658
             >>>end - start
             22.724523540384666
  -休眠时间：sleep(s) s拟休眠时间，单位是秒，可以是浮点数
             >>>def wait():
                    time.sleep(3.31)
             >>>wait() # 程序将等待3.3秒后退出             
'''
