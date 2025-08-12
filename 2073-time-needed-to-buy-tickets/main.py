class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # 用队列模拟整个过程
        queue = collections.deque()
        for i in range(len(tickets)):
            # 队列中记录每个人
            queue.append(i) 

        time = 0
        while queue:
            # 队头的人买票
            front = queue.popleft()
            time += 1
            tickets[front] -= 1

            # 如果k-th人，票买完了
            if k == front and tickets[front] == 0:
                return time

            if tickets[front] == 0:
                continue
            
            queue.append(front)
        
        return time
