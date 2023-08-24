def reverseWords(s):
    # can also be done with split() and will be no need for a for-loop, however, 
    # that approach is slower
    sList = s.split(" ")
    single_spacing = []
    res = ""

    for i in range(len(sList)):
        if(sList[i] != ''):
            single_spacing.append(sList[i])
    
    beg = 0
    end = len(single_spacing) - 1
    temp = ""
    while beg < end:

        temp = single_spacing[beg]
        single_spacing[beg] = single_spacing[end]
        single_spacing[end] = temp

        beg += 1
        end -=1

    res = ' '.join(single_spacing)

    return res

print(reverseWords("the sky is blue"))
print(reverseWords("  hello world  "))
print(reverseWords("a good   example"))