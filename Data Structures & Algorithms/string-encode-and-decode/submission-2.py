class Solution:

    def encode(self, strs: list[str]) -> str:
        encode_str = []
        for s in strs:
            n = len(s)
            encode_str.append(f"{n}#{s}")
        return ''.join(encode_str)

    def decode(self, s: str) -> list[str]:
        out = []
        i = 0

        while i < len(s):
            j = s.find('#', i)          # position of '#'
            length = int(s[i:j])        # length is the digits before '#'
            start = j + 1               # start of the actual string
            end = start + length        # end of the actual string

            out.append(s[start:end])
            i = end  
                
        return out