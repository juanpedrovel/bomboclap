class Solution:
    def findMaxConsecutiveOnes(self, nums):
        if not nums:
            return 0
        lens = len(nums)
        lives = 1
        max_ones = 1
        next_one = []
        start = None
        for i in range(lens):
            if nums[i] == False and start != None:
                if lives == 1:
                    if i < lens - 1 and nums[i+1] == True:
                        next_one.append(i + 1)
                        lives -= 1
                    else:
                        max_ones = max(max_ones, i - start + 1)
                        lives = 1
                        start = None
                else:
                    max_ones = max(max_ones, i - start)
                    if next_one:
                        start = next_one.pop()
                        lives = 0
                        if i + 1 < lens and nums[i+1] == True:
                            next_one.append(i+1)
                    else:
                        start = None                  
                        lives = 1
            elif nums[i] == True and start == None:
                start = i
            
        if start != None:
            max_ones = max(min(lens, lives + lens - start), max_ones)
        return max_ones

time = [0]
k = [1]
d = Solution()
print(d.findMaxConsecutiveOnes(time))
