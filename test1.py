"""
 * Project name(项目名称)：Python_raise
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 10:29
 * Version(版本): 1.0
 * Description(描述)： raise [exceptionName [(reason)]]

 raise：单独一个 raise。该语句引发当前上下文中捕获的异常（比如在 except 块中），或默认引发 RuntimeError 异常。
raise 异常类名称：raise 后带一个异常类名称，表示引发执行类型的异常。
raise 异常类名称(描述信息)：在引发指定类型的异常的同时，附带异常的描述信息。
 """

if __name__ == '__main__':
    if 1 < 3:
        raise ValueError
