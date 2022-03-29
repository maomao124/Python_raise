"""
 * Project name(项目名称)：Python_raise
 * Package(包名): 
 * File(文件名): test5
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 10:36
 * Version(版本): 1.0
 * Description(描述)： 
 """

if __name__ == '__main__':
    try:
        a = input("输入一个数：")
        if not a.isdigit():
            raise
    except RuntimeError as e:
        print("引发异常：", repr(e))
