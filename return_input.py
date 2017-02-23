import time, sys, random
'''
随机选择图片
随机生成价格
随机生成库存
随机生产sku编码
生成带时间戳的产品名称
随机给范围数字
'''

def random_number_float(number):
    """
    随机给出范围内的两位实数
    :param number: 范围最大值
    :return:
    """
    return round(random.random() * number, 2)

def date_uni_string(your_str):
    """
    返回时间+string，构造具有时间差别的名称
    """
    return  time.strftime("%Y-%m-%d日%H:%M", time.localtime())+your_str

def random_xpath(part1,random_number,part2):
    """
    返回随机的xpath或者其他类似的元素路径
    :param part1: 路径前半部分
    :param random_number: 随机数的最大范围
    :param part2: 路径后半部分
    :return: 全路径
    """
    return part1+str(random.randint(0,random_number))+part2

def test_random_number_float():
    print("random_number_float test====")
    for i in range(1, 10):
        print(random_number_float(5))


test_random_number_float()
print(date_uni_string("测试商品"))
print(random_xpath('//*[@id="addSkuWindow"]/div/div/fieldset[',12,']/div/div/span/span/input'))
print(random.randint(1,50))