#119. Pascal's Triangle II

class Solution:
    def return_next_row(self, row):
        next_row = []
        for i in range(len(row)+1):
            if i == 0 or i == len(row):
                next_row.append(1)
                continue
            next_row.append(row[i-1] + row[i])
        return next_row
            
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        row = [1]
        for i in range(numRows):
            output.append(row)
            row = self.return_next_row(row)
        return output
    
    def getRow(self, rowIndex: int) -> List[int]:
        return self.generate(rowIndex+1)[-1]

#Results:
#Runtime: 37 ms, faster than 18.75% of Python3 online submissions for Pascal's Triangle II.
#Memory Usage: 14.2 MB, less than 77.95% of Python3 online submissions for Pascal's Triangle II.
