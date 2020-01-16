# *_* coding： UTF-8 *_*
# 开发团队：明日科技
# 明日学院网站：www.mingrisoft.com
# 开发工具：PyCharm
# 任务4：特价商品销售倒计时提醒

import datetime
day20 = datetime.datetime.strptime('2018-12-20 0:0:0','%Y-%m-%d %H:%M:%S')      # 设置未来时间
now = datetime.datetime.today()
delta = day20 - now                                                                 # delta存储两个时间的时间，差精确到毫秒
day = delta.days                                                                    # 获取两个时间之间的天数
hour = int( delta.seconds / 60 / 60 )                                               # 使用int函数把小时取整
minutes = int( ( delta.seconds - hour * 60 * 60 ) / 60 )                            # 使用int函数把分钟取整
seconds = delta.seconds - hour * 60 * 60 - minutes * 60                             # 使用int函数把秒取整
print('\033[31;43m距离结束：\033[43m' + '\033[34;43m'+str(day)+'\033[43m'+'\033[31;43m天\033[43m'+'\033[34;43m'+str(hour)+'\033[43m'+'\033[31;43m小时\033[43m'+'\033[34;43m'+str(minutes)+'\033[43m'+'\033[31;43m分钟\033[43m'+'\033[34;43m'+str(seconds)+'\033[43m'+'\033[31;43m秒\033[0m')

