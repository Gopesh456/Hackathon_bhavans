class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        r1 = { 1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM' }

        answer = str()

        def convert(count,a):
            temp = str()
            if count == 4*a or count == 9*a: 
                temp = r1[count]
            else: 
                while count > 0:
                    if count >= 5*a:
                        temp = r1[5*a]
                        count -= 5*a
                    else:
                        temp = temp + r1[a]
                        count -= a
            return temp

        answer = convert(int(str(num)[-1]),1)
        if len(str(num))>1: answer = convert(int(str(num)[-2])*10,10) +answer

        if len(str(num))>2: answer = convert(int(str(num)[-3])*100,100) +answer

        if len(str(num))>3: 
            for i in range(int(str(num)[0])):
                answer = 'M' + answer

        return answer
    

ans = Solution().intToRoman(1994)
print(ans)