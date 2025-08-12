class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        # 遍历数组，统计每个数字出现的次数
        for num in nums:
            count[num] = count.get(num,0) + 1
        # 找出出现一次的数字
        for num in nums:
            if count[num] == 1:
                return num
        return -1
