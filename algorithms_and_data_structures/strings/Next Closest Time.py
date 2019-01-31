class Solution:
    def nextClosestTime(self, time):
        lent = len(time)
        digits = [False] * 10
        next_time = []
        for i in time:
            next_time.append(i)
            if i == ':':
                continue
            x = int(i)
            digits[x] = True
            
        least_digit = 0
        for i in range(len(digits)):
            if digits[i] == True:
                least_digit = i
                break
                
        for i in range(lent-1, -1, -1):
            if time[i] == ':':
                continue
            x = int(time[i])
            if i == 0:
                limit = 3
            elif i == 1:
                if time[0] == '2':
                    limit = 5
                else:
                    limit = 10
            elif i == 3:
                limit = 6
            else:
                limit = 10
            
            for j in range(x + 1, limit):
                if digits[j] == True:
                    next_time[i] = str(j)
                    return self.build_time(next_time)
                
            if least_digit < limit:
                next_time[i] = str(least_digit)
        
        return self.build_time(next_time)
    
    
    def build_time(self, next_time):
        answer = ''.join(next_time)
        return answer

time = '23:59'
d = Solution()
print(d.nextClosestTime(time))