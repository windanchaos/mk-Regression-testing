import time, sys, random, string
'''
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
    return  your_str+time.strftime("%Y-%m-%d日%H:%M", time.localtime())

def random_xpath(part1,random_number,*part2):
    """
    返回随机的xpath或者其他类似的元素路径
    :param part1: 路径前半部分
    :param random_number: 随机数的最大范围
    :param part2: 路径后半部分
    :return: 全路径
    """
    num = random.randint(0, random_number)
    if len(part2)==0:
        return str(part1) + str(num)
    else:
        part3=part2[0]
        return str(part1)+str(num)+str(part3)

def random_string():
    return ''.join(random.sample(['0','1','2','3','4','5','6','7','8','9','z',
                                      'y','x','w','v','u','t','s','r','q','p','o',
                                      'n','m','l','k','j','i','h','g','f','e','d',
                                      'c','b','a'], 8))

def random_product_name():
    pro_names=['初春新品','连衣裙','裤子','T恤打底','衬衫','针织衫','毛衣','毛呢外套',
               '短外套','牛仔裤','套装','卫衣','风衣','半身裙','蕾丝衫','大码女装',
               '皮草','妈妈装','高腰裤','西装','羽绒服', '红人私服','甜美风']
    return pro_names[random.randint(0,len(pro_names)-1)]

def random_product_sku():
    sku_names=['S','M','XL','XXL']
    return sku_names[random.randint(0,len(sku_names)-1)]

def random_special_charactor():
    sep_charactor =['\'','\\"','\&','\\','\\n','\\r','\\t','\\b','\\f','\<','\>',
                    '<br/>','`','@','$','*','\^','#','?','_','&&']
    return ''.join(random.sample(sep_charactor,5))
print(random_xpath('//*[@id="pager"]/ul/li[',random.randint(2,3),']'))
productName = date_uni_string(random_special_charactor()+random_product_name())
shortDes = date_uni_string(random_product_name()+random_special_charactor())
product_sku = random_product_sku()
sku_quto = str(random.randint(10,3000000))
sku_price = str(random_number_float(2))
p_inventory =str(random.randint(100,5000))
skuCode = random_string()
share_title = random_special_charactor()+"分享经济"+time.strftime("%Y-%m-%d日%H:%M", time.localtime())
share_content =random_special_charactor()+"将社会海量、分散、闲置资源、平台化、协同化地集聚、复用与供需匹配"+\
               time.strftime("%Y-%m-%d日%H:%M", time.localtime())