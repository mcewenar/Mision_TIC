#1. Maximum distance
#
#Given a text and a subText that might be in the text, return the maximum distance from the 
#subText to any side of the text. If the subText is not in the text, return -1. The distance is 
#the number of characters from the subText to any of the text sides.
#
#Example 1:
#
#Input:
#
#text = abcdefghi
#subText = de
#Output: 4
#
#Explanation:
#
#The minimum distance is the one on the right side (fghi).
#
#Example 2:
#
#Input:
#
#text = abcdefgci
#subText = c
#Output: 7
#
#Explanation:
#
#The maximum distance is on the left side to the second c.
#
#Constraints:
#
#1 <= text.length <= 2147483647
#1 <= subText.length <= text.length
#Text and subText contain only English lowercase letters

def maximum_distance(text,subtext):
    distance_list=[]
    index=0
    if subtext in text:
        for i in text:
            c=text.find(subtext)
            if c!=-1:
                valor_izqu = c+index
                final_c=c+len(subtext)
                valor_der = len(text[final_c:])
                x = valor_izqu if valor_izqu > valor_der else valor_der
                distance_list.append(x)
                index+=c
                text = text[c:]
            break
        return max(distance_list)
    return -1

print(maximum_distance("jsjsjsjmarijsdfjjfkgfkfmarikggl","mari"))