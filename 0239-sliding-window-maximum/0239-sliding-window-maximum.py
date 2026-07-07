from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        monotonic_queue = deque()
        max_at_sliding_windows = []
        for current_index, num in enumerate(nums):
            # 1. Remove indices whose values are smaller than the current value
            # (they can never be the max while num is still in the window)
            while monotonic_queue and nums[monotonic_queue[-1]] < num:
                monotonic_queue.pop()  # remember this is loop pop(), pop multiple entries
                # this pop() is pop_right(), basically remove the smallest ones

            monotonic_queue.append(
                current_index
            )  # so logically this is the largest so far

            # 2. Remove the front index if it's outside the current window
            # access the top index and remove it if it has been outside of the window
            if monotonic_queue[0] <= current_index - k:
                monotonic_queue.popleft()

            if current_index >= k - 1:  # breakpoint for the availability of windows
                max_at_sliding_windows.append(nums[monotonic_queue[0]])
        return max_at_sliding_windows
