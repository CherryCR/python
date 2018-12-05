# 获取用户输入的数字
num = int(input("请输入一个数字: "))
 
# 初始化变量sum 输入数字的每一位的此方和
sum = 0
# 指数
n = len(str(num))
 
# 判断条件
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n
   temp //= 10
 
# 输出结果
if num == sum:
   print(num,"是阿姆斯特朗数")
else:
   print(num,"不是阿姆斯特朗数")