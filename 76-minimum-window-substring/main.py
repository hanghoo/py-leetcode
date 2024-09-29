class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, need = {}, {}
        for c in t:
            need[c] = need.get(c,0) + 1
        
        left, right = 0, 0
        valid = 0
        # print string
        start = 0
        length = float("inf")

        while right < len(s):
            c = s[right]
            right += 1
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] = window.get(c,0) + 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                # 在这里更新最小覆盖子串
                if right - left < length:
                    start = left
                    length = right - left
                
                d = s[left]
                left += 1

                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        
        return "" if length == float('inf') else s[start:start+length]
