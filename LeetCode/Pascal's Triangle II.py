from typing import List
class Solution:
    def getRow(rowIndex: int) -> List[int]:
        triangle = []
        index = rowIndex - 1
        for i in range(rowIndex):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    prev_row = triangle[i - 1]
                    new_value = prev_row[j - 1] + prev_row[j]
                    row.append(new_value)
            triangle.append(row)

        return triangle[index]
    
print(Solution.getRow(5))