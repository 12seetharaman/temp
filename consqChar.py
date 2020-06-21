def delCount(word):
    i = 0
    j = 1
    del_count = 0
    while j < len(word):
        if word[i] == word[j]:
            del_count += 1
        i = j
        j += 1
    return del_count

def getCount(word):
    return (len([i for i in range(len(word)-1) if word[i] == word[i+1]]))


if __name__ == "__main__":
    input = ['JJJJ', 'QQQQQQQQQQ', 'JQJQJQJK', 'KQKJQKJQK', 'JJJQQQ', 'JJQQKK']
    for w in input:
        #print(f'Deletion count {delCount(w)}')
        print(f'Deletion count {getCount(w)}')