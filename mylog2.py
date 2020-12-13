from  loguru import logger


#需求：实现一个加法的操作

def add(a , b, *args):
    sum = 0
    if not isinstance(a,int):
        logger.error("输入的参数a的类型不正确")
        return
    if not isinstance(b, int):
        logger.error("输入的参数b的类型不正确")
        return
    for x in args:
        if not isinstance(x,int):
            logger.warning("输入的数据有错误类型，请检查")
            continue
        sum += x
        sum =sum+a+b
    return sum
add(3,4)
print("="*20)
add(3,'g')
print("="*20)
add(2,5,8)
print("="*20)
add(3,5,'k',2)

