
import re 
class Solution:
    def isPalindrome(self, s: str) -> bool:


        tex = re.sub(r'[^a-zA-Z0-9]', '', s).lower()


        right = len(tex)-1

        i=0


        while i <= right:

            if(tex[i] != tex[right]):
                return False

            right -= 1
            i +=1
        

        return True