#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/16 15:22
# @Author :zhai shuai
"""
 作用
    一：监控cpu的利用率
 难点
    位（bit）：二进制数中的一个数位，可以是0或者1，是计算机中数据的最小单位。
    字节（Byte，B）：计算机中数据的基本单位，每8位组成一个字节。各种信息在计算机中存储、处理至少需要一个字节。例如，一个ASCII码用一个字节表示，一个汉字用两个字节表示。
    字（Word）：两个字节称为一个字。汉字的存储单位都是一个字。
    扩展的存储单位
    在计算机各种存储介质（例如内存、硬盘、光盘等）的存储容量表示中，用户所接触到的存储单位不是位、字节和字，而是KB、MB、GB等，但这不是新的存储单位，而是基于字节换算的。
    KB：  。早期用的软盘有360KB和720KB的，不过软盘已经很少使用。
    MB：  。早期微型机的内存有128MB、256MB、512MB，目前内存都是1GB、2GB甚至更大。
    GB：  。早期微型机的硬盘有60GB、80GB，目前都是500GB、1TB甚至更大。
    TB：  。目前个人用的微型机存储容量也都能达到这个级别了，而作为服务器或者专门的计算机，不可缺少这么大的存储容量。

 注意点
    
"""
import psutil
import time

def get_cpu(t = 1):
    t1 = psutil.cpu_times() # 获取开始时间的cpu时间累计

    time.sleep(2)

    t2 = psutil.cpu_times()# 获取结束时间的cpu时间累计

    t1_all = sum(t1) #
    t2_all = sum(t2)


    t1_busy = t1_all - t1.idle
    t2_busy = t2_all - t2.idle

    if t2_busy - t1_busy < 0:
        return 0.0

    cpu_busy = t2_busy - t1_busy
    all_time = t2_all-t1_all
    cpu_rate = (cpu_busy / all_time) * 100

    return round(cpu_rate,2)



if __name__ == '__main__':
    while True:
        print(get_cpu())

