#python 中的正则表达式语法
# 记录文本规则的代码，就是对元字符的学习
import re

# re.RegexObject  正则表达式模式对象， re.compile() 返回 RegexObject 对象。
# re.MatchObject  匹配对象，group() 返回被 RE 匹配的字符串。
# r 即后面的字符串为原始字符串

#主要命令有
'''
re.match() #尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
re.search()  #扫描整个字符串并返回第一个成功的匹配。#注意： match 和 search 是匹配一次 findall 匹配所有。
re.sub      #用于替换字符串中的匹配项。 re.sub(pattern, repl, string, count=0, flags=0) 替换的字符串，也可为一个函数。
re.findall() #在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
re.finditer() #和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
re.split    #按照匹配的子串将字符串分割后返回列表，
re.compile() #函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象。re.compile(pattern[, flags])
# 除了以上的方法外，还有pattern.match(pattern) pattern.search(pattern) 等
'''

#---re.math
# '''
# m=re.match('www', 'www.runoob.com') # 在起始位置匹配
# print(m.group())

# line = 'Cats dogs are smarter than dogs'
# matchObj = re.match( r'(.*) are (.*) (.*)', line, re.M|re.I) #() 里面是为.group()准备的
# print(matchObj.group(1))
# matchObj = re.search( r'(.*) dogs .*', line, flags=(re.M|re.I)) #或者不要flags=
# print(matchObj.group())
# '''

#--re.search()
'''
line = "Cats are smarter than dogs"
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)  #匹配括号内的表达式，也表示一个组group()
print ("searchObj.group() : ", searchObj.group())
print ("searchObj.group(1) : ", searchObj.group(1))
'''

#---re.sub
'''
phone = "2004-959-559 # 这是一个电话号码"
num = re.sub(r'#.*$', "", phone)
print (num)
'''
#--
'''
def double(matched):   #repl 参数是一个函数
    value = int(matched.group('value'))
    return str(value * 2)  # 将匹配的数字乘于 2

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
'''

#---re.findall
# '''
# result1 = re.findall(r'\d','runoob 123 google 456')
# print(result1)
# pattern = re.compile(r'\d+')   # 查找数字
# result2 = pattern.findall('runoob 123 google 456')
# print(result2)
# '''

#---re.finditer()
'''
it = re.finditer(r"\d+","12a32bc43jf3") 
for match in it: 
    print (match.group())
'''

#--re.split
# m=re.split('\W+', 'runoob, runoob, runoob.')
# print(m)


#--re.compile()
#e.g 1
# pattern = re.compile(r'\d{1,}')                    # 用于匹配至少一个数字
# m = pattern.findall('one12twothree34fo3351ur')       
# print(m)


#正则表达式修饰符 - 可选标志
'''
正则表达式可以包含一些可选标志修饰符来控制匹配的模式。修饰符被指定为一个可选的标志。多个标志可以通过按位 OR(|) 它们来指定。如 re.I | re.M 被设置成 I 和 M 标志：
修饰符	描述
re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
'''

#常用的模式
'\d{n,}' #至少n位的数字
'(\-|\+)?\d+(\.\d+)?' #正数、负数、和小数
'[\u4e00-\u9fa5]{0,}' #汉字
'\n\s*\r'  #可以用来删除空白行

#元字符和模式的理解
# \ #将下一个字符标记为一个特殊字符、或一个原义字符、或一个 向后引用、或一个八进制转义符。
# 例如，'n' 匹配字符 "n"。'\n' 匹配一个换行符。序列 '\\' 匹配 "\" 而 "\(" 则匹配 "("。
# ^ #匹配输入字符串的开始位置。
# *	# 匹配前面的子表达式零次或多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于{0,}。
# +	# 匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。
# ?	# 匹配前面的子表达式零次或一次。例如，"do(es)?" 可以匹配 "do" 或 "does" 。? 等价于 {0,1}。

# ?	# 当该字符紧跟在任何一个其他限制符 (*, +, ?, {n}, {n,}, {n,m}) 后面时，匹配模式是非贪婪的。
# 非贪婪模式尽可能少的匹配所搜索的字符串，而默认的贪婪模式则尽可能多的匹配所搜索的字符串。
# 例如，对于字符串 "oooo"，'o+?' 将匹配单个 "o"，而 'o+' 将匹配所有 'o'。

# . #匹配除换行符（\n、\r）之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用像"(.|\n)"的模式。
# x|y	匹配 x 或 y。例如，'z|food' 能匹配 "z" 或 "food"。'(z|f)ood' 则匹配 "zood" 或 "food"。

# (pattern)	#匹配 pattern 并获取这一匹配。所获取的匹配可以从产生的 Matches 集合得到
# (?:pattern)	#匹配 pattern 但不获取匹配结果，也就是说这是一个非获取匹配，不进行存储供以后使用。这在使用 "或" 字符 (|) 来组合一个模式的各个部分是很有用。例如， 'industr(?:y|ies) 
# (?=pattern)	#正向肯定预查（look ahead positive assert），在任何匹配pattern的字符串开始处匹配查找字符串。这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用。例如，"Windows(?=95|98|NT|2000)"能匹配"Windows2000"中的"Windows"，但不能匹配"Windows3.1"中的"Windows"。预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始。
# (?!pattern)	#正向否定预查(negative assert)，在任何不匹配pattern的字符串开始处匹配查找字符串。这是一个非获取匹配，也就是说，该匹配不需要获取供以后使用。例如"Windows(?!95|98|NT|2000)"能匹配"Windows3.1"中的"Windows"，但不能匹配"Windows2000"中的"Windows"。预查不消耗字符，也就是说，在一个匹配发生后，在最后一次匹配之后立即开始下一次匹配的搜索，而不是从包含预查的字符之后开始。
# (?<=pattern)	#反向(look behind)肯定预查，与正向肯定预查类似，只是方向相反。例如，"(?<=95|98|NT|2000)Windows"能匹配"2000Windows"中的"Windows"，但不能匹配"3.1Windows"中的"Windows"。
# (?<!pattern)	#反向否定预查，与正向否定预查类似，只是方向相反。例如"(?<!95|98|NT|2000)Windows"能匹配"3.1Windows"中的"Windows"，但不能匹配"2000Windows"中的"Windows"。

# [xyz] #字符集合。匹配所包含的任意一个字符。
# [^xyz]	#负值字符集合。匹配未包含的任意字符。
# \b	#匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
# \B	# 匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
# \cx	# 匹配由 x 指明的控制字符。例如， \cM 匹配一个 Control-M 或回车符。x 的值必须为 A-Z 或 a-z 之一。否则，将 c 视为一个原义的 'c' 字符。
# \d	# 匹配一个数字字符。等价于 [0-9]。
# \D	# 匹配一个非数字字符。等价于 [^0-9]。
# \f	# 匹配一个换页符。等价于 \x0c 和 \cL。
# \n	# 匹配一个换行符。等价于 \x0a 和 \cJ。
# \r	# 匹配一个回车符。等价于 \x0d 和 \cM。
# \s	# 匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
# \S	# 匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
# \t	# 匹配一个制表符。等价于 \x09 和 \cI。
# \v	# 匹配一个垂直制表符。等价于 \x0b 和 \cK。
# \w	# 匹配字母、数字、下划线。等价于'[A-Za-z0-9_]'。
# \W	# 匹配非字母、数字、下划线。等价于 '[^A-Za-z0-9_]'。
# \xn	# 匹配 n，其中 n 为十六进制转义值。十六进制转义值必须为确定的两个数字长。例如，'\x41' 匹配 "A"。'\x041' 则等价于 '\x04' & "1"。正则表达式中可以使用 ASCII 编码。
# \num	# 匹配 num，其中 num 是一个正整数。对所获取的匹配的引用。例如，'(.)\1' 匹配两个连续的相同字符。
# \1...\9	匹配第n个分组的内容。


# 正则表达式 - 运算符优先级,以下安装优先的先后顺序
# \	转义符
# (), (?:), (?=), []	圆括号和方括号
# *, +, ?, {n}, {n,}, {n,m}	限定符
# ^, $, \任何元字符、任何字符	定位点和序列（即：位置和顺序）
# |	替换，"或"操作
# 字符具有高于替换运算符的优先级，使得"m|food"匹配"m"或"food"。若要匹配"mood"或"food"，请使用括号创建子表达式，从而产生"(m|f)ood"。
