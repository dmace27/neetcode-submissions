class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1
        n = len(nums)
        num_windows = n - k + 1
        solution_arr = [None] * num_windows
        

        def search_sublist(nums: List[int], l: int, r: int) -> int:
            mx = -10001
            for i in range(l, r):
                if nums[i] > mx:
                    mx = nums[i]

            return mx 

        # initial step
        solution_arr[0] = search_sublist(nums, l, r)
        current_max = solution_arr[0]
        
        for i in range(1, num_windows):
            # r+1 is the incoming number
            if nums[r+1] > current_max:
                current_max = nums[r+1]
            
            # in the case that the outgoing number is the current max
            if nums[l] == current_max:
                current_max = search_sublist(nums, l+1, r+1)
            
            l +=1
            r += 1

            solution_arr[i] = current_max
        
        return solution_arr





