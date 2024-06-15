import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Create a list of tuples (capital, profit) and sort it based on capital
        projects = sorted(zip(capital, profits))
        
        # Initialize the max-heap for profits
        max_profit_heap = []
        
        # Initial capital
        current_capital = w
        project_index = 0
        
        for _ in range(k):
            # Push all projects that can be started with the current capital to the max profit heap
            while project_index < len(projects) and projects[project_index][0] <= current_capital:
                heapq.heappush(max_profit_heap, -projects[project_index][1])
                project_index += 1
            
            # If no project can be done, break the loop
            if not max_profit_heap:
                break
            
            # Get the project with the maximum profit
            current_capital += -heapq.heappop(max_profit_heap)
        
        return current_capital
