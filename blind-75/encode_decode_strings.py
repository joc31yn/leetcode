class Solution:
    def encode(self, strs):
        """
        Time Complexity: O(n)
        """
        encoded_str = ""
        for s in strs:
            prefix = str(len(s)) + "#"
            encoded_str += prefix + s
        return encoded_str

    def decode(self, s):
        """
        Time Complexity: O(n)
        """
        decoded_strs = []
        length = 0
        str_len = len(s)
        i = 0
        while i < str_len:
            if s[i] != "#":
                length = length * 10 + int(s[i])
            elif length > 0:
                decoded_strs.append(s[i + 1:i + length + 1])
                i += length
                length = 0
            else:
                decoded_strs.append("")
            i += 1
        return decoded_strs


sol = Solution()

print(sol.decode(sol.encode(["neet", "code", "love", "you"])))
