def generateParenthesis(n):
    result = []

    def backtrack(current, bopen, bclose):

        # Complete valid combination
        if bopen == n and bclose == n:
            result.append(current)
            return

        # Add opening bracket
        if bopen < n:
            backtrack(current + "(", bopen + 1, bclose)

        # Add closing bracket
        if bclose < bopen:
            backtrack(current + ")", bopen, bclose + 1)

    backtrack("", 0, 0)

    return result


# Sample input
n = 3

# Generate parentheses
answer = generateParenthesis(n)

print(answer)