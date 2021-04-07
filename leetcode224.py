class Solution:
    alphabet = ['0','1','2','3','4','5','6','7','8','9']
    def calculate(self, s: str) -> int:
        swicth = {"+": lambda a,b: a+b, "-": lambda a,b: a-b}
        stack = []
        s = s[::-1]
        result = 0
        for l in s:
            if l in self.alphabet:
                c = l
                if len(stack) != 0:
                    if isinstance(stack[len(stack) - 1], int):
                        tp = str(stack.pop())
                        c = l + tp
                stack.append(int(c))
            elif l == ')':
                stack.append(l)
            elif l == '+' or l == '-':
                    stack.append(l)
            elif l == ' ':
                continue
            elif l == '(':
                if not isinstance(stack[len(stack)-1], int):
                    stack.append(0)
                rs = stack.pop()
                tp = stack[len(stack)-1]
                while tp != ')':
                    op = stack.pop()
                    rs = swicth[op](rs, stack.pop())
                    tp = stack[len(stack)-1]
                stack.pop()
                stack.append(rs)
        if not isinstance(stack[len(stack) - 1], int):
            stack.append(0)
        if len(stack) >= 1:
            result = stack.pop()
            while len(stack) != 0:
                op = stack.pop()
                result = swicth[op](result, stack.pop())
            stack.append(result)
        return result

    def cal(self, s: str) -> int:
        stack = []
        # 当连续数字是追加
        tmp_str = ''
        for i in s[::-1]:
            if i == ' ':
                continue
            if i.isdigit():
                # 追加连续数字
                tmp_str += i
                continue
            # 遇到非数字场景
            if tmp_str:
                # 先将tmp_str 逆序后添加至stack中
                stack.append(int(tmp_str[::-1]))
                # 重置
                tmp_str = ''
            # 遇到-号，取出尾数，添加负号后重新放入
            if i == '-':
                stack.append(-stack.pop())
            # 正常添加
            elif i == ')':
                stack.append(i)
            # 开始合并左括号到右括号之间的数字
            elif i == '(':
                num = 0
                while True:
                    if stack[-1] == ')':
                        stack.pop()
                        break
                    num += stack.pop()
                stack.append(num)
        # 未加入的临时数字，进行追加
        if tmp_str:
            stack.append(int(tmp_str[::-1]))
        return sum(stack)

sv = Solution()
print(sv.calculate("(1+(4+5+2)-3)+(6+8)"))
print(sv.calculate("2345632"))
print(sv.calculate("-2+1"))
print(sv.cal("(9568+(9040-(380+(2042-(7115)+(6294)-(4395-(5183+9744+(7746-(1099+2718))-(9370-(8561+(9302)-(7632+(8451-(1759+(7760))-(3377+5363+9093+(8332-(4492-(1151+(1165-8833+(775+(3749)+9399))+9112+(6273+(7285-(6112-(668-(7756-4316-(582+1835-(6644+690+1204-(7197+(7897))+(7009-(7262))-7782-(7858+(7644+(9461+(2224)-(7531-1095-(891+1022)+2197-(9855)))+(6663-(7417-(6158-(3610))+(1481))-(4182+(4761)))+(5017))+(9990)+(6218)))-(2904)+(5631)-(8888)+3401+(3569))+(1135))-(3695-(7713+(3479)-(9813+(8171+(8616-8026+(4634-(6973))-(9761-(623-4782)+(2514)+(6233)))))+(6140))-(6641)-8611+(8389)+8074-(4412))-(3703)+(9688+(9513))))-(4987)))+(9647)))))))))-(2299))-(4785))))))"))
