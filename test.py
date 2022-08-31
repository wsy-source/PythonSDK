# import uuid
#
# from werkzeug.routing import BaseConverter, Map
#
#
# class RegexConverter(BaseConverter):
#     def __init__(self, map: Map, regex):
#         super(RegexConverter, self).__init__(map)
#         self.regex = regex
#
#     def to_python(self, value: str):
#         """
#         路由匹配成功则会调用to_python方法
#         :param value:
#         :return:
#         """
#         return int(value)
#
#     def to_url(self, value) -> str:
#         """
#         使用url_for 反向生成URL时，传递的参数经过该方法处理，返回的值用于生成URL中的参数
#         :param value:
#         :return:
#         """
#         value = super(RegexConverter, self).to_url(value)
#         return value
#
class Dog:
    def __call__(self, *args, **kwargs):
        print('wangwang')

    def __init__(self):
        self.name = 'lisi'


dog = Dog()
dog()
