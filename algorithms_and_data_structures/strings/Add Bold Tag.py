class Solution:
    def addBoldTag(self, s, dict):
        lens = len(s)
        matchs = []
        if not s or not dict:
            return s
        tree = {0:{}}
        counter = 1
        for word in dict:
            current = tree[0]
            for j in range(len(word)):
                if word[j] in current:
                    current = tree[current[word[j]]]
                else:
                    current[word[j]] = counter
                    tree[counter] = {'word': False}
                    current = tree[counter]
                    counter += 1
                if j == len(word) - 1:
                    current['word'] = True

        for i in range(lens):
            current = tree[0]
            for j in range(i, lens):
                letter = s[j]
                if letter in current:
                    current = tree[current[letter]]
                    if current['word'] == True:
                        if matchs:
                            last = matchs.pop()
                            if i > last[1] + 1:
                                matchs.append(last)
                                matchs.append([i,j])
                            elif i > last[0] and j < last[1]:
                                matchs.append(last)
                            else:
                                last[1] = j
                                matchs.append(last)
                        else:
                                matchs.append([i,j])
                else:
                    break

        changes = 0
        for element in matchs:
            i = element[0]
            j = element[1] + 1
            s = s[:i+changes] + '<b>' + s[i+changes:j+changes] + '</b>' + s[j+changes:]
            changes += 7
        return s

s = "aaabbcc"
dict = ["aaa","aab","bc"]
d = Solution()
print(d.addBoldTag(s, dict))