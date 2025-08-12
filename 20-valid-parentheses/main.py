class Solution:
    def isValid(self, s: str) -> bool:
        # 用列表模拟栈
        left = []
        for c in s:
            if c in '({[':
                # 字符c是左括号，入栈
                left.append(c)
            else:
                # 字符c是右括号
                if left and self.leftOf(c) == left[-1]:
                    left.pop()
                else:
                    # 和最近的左括号不匹配
                    return False
        # 是否所有的左括号都被匹配了
        return not left
    


    def leftOf(self, c):
        if c == ')': 
            return '('
        elif c == '}':
            return '{'
        else:
            return '['
