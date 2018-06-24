# -*- coding:UTF8 -*-

import re

a = 'https://c.static-nike.com/a/images/t_PDP_1280_v1/f_auto/rdj8sxres6rd3vnfjok3/epic-react-flyknit-mens-running-shoe-ZwTJE04z.jpg'

# 将正则表达式编译成Pattern对象
# pattern = re.compile(r'\/\d*$')
str = a.split('/')
lenStr = len(str)
print str[lenStr-1]
