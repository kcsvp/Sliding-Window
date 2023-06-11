class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []

        for each in operations:
            if each =='C':
                records.pop()
            elif each == 'D':
                records.append(2*records[-1])
            elif each == '+':
                records.append(records[-1] + records[-2])
            else:
                records.append(int(each))
        
        return sum(records)
