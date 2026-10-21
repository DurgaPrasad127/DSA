class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []
        for i in range(len(operations)):
            if operations[i] == 'C':
                record.pop()
            elif operations[i] == 'D':
                record.append(int(2*record[-1]))
            elif operations[i] == '+':
                record.append(record[-1]+record[-2])
            else:
                record.append(int(operations[i]))
        return sum(record)