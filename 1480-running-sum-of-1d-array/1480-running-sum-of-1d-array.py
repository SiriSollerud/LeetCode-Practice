class Solution(object):
    def runningSum(self, nums):
        run = []
        run_sum = []
        for num in nums:
            run_sum.append(num + sum(run))
            run.append(num)
        return run_sum