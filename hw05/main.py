import re
s='我的电子邮件tom@gmail.com'
re.findall(r'\d+',s)
print(s.search(str))

import re
a='将什么发送到jerry123@163.com,或者3123432@qq.com'
re.findall(r'\d+',a)
print(a.search(str))

import re
w='遇到特殊情况打电话182123445678'
re.findall(r'\d+',w)
print(w.search(str))
