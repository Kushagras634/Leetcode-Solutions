class Solution:
    def fullJustify(self, words, maxWidth):
        i, N, result = 0, len(words), []
        while i < N:
            oneLine, j, currWidth, positionNum, spaceNum = [words[i]], i + 1, len(words[i]), 0, maxWidth - len(words[i])
            while j < N and currWidth + 1 + len(words[j]) <= maxWidth:
                oneLine.append(words[j])
                currWidth += 1 + len(words[j])
                spaceNum -= len(words[j])
                positionNum, j = positionNum + 1, j + 1
            i = j
            if i < N and positionNum:
                spaces = [' ' * (int(spaceNum / positionNum) + (k < spaceNum % positionNum)) for k in range(positionNum)]+ ['']
            else:
                spaces = [' '] * positionNum + [' ' * (maxWidth - currWidth)]
            result.append(''.join([s for pair in zip(oneLine, spaces) for s in pair]))
        return result