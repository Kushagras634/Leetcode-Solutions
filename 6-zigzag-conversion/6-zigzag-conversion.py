class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        hash_map={row:"" for row in range(1,numRows+1)}
        row=1
        up=True
        for i in s:
            hash_map[row]+=i
            if row==1 or (row<numRows and up):
                row+=1
                up=True
            else:
                row-=1
                up=False
        converted=""
        for i in hash_map:
            converted+=hash_map[i]
        return converted
        
        