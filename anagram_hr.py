# https://www.hackerrank.com/challenges/anagram/problem
# I had to use pen and paper extensively on this problem to map out this logic.
# It was easy to say in plain english what needed to be done but translating that to python was challenging.

s = "mnop"


def anagram(string):
    s1_dict = {}
    s2_dict = {}
    string_length = len(string)

    # check to string for even length
    if string_length % 2 != 0:
        return -1

    half_string = int(string_length / 2)
    sliceobject1 = slice(0, half_string)
    sliceobject2 = slice(half_string, string_length)

    s1 = string[sliceobject1]
    s2 = string[sliceobject2]

    # Builds histogram for string 1
    for i in s1:
        if i not in s1_dict.keys():
            s1_dict[i] = 1
        else:
            s1_dict[i] += 1

    # Builds histogram for string 2
    for i in s2:
        if i not in s2_dict.keys():
            s2_dict[i] = 1
        else:
            s2_dict[i] += 1

    '''
    The pattern I noticed is the answer always equaled the length of the substring minus the number of matches. The length of the substring is easy, thus the challenge was to figure out when to increment the "match" variable.
    '''
    s1_length = len(s1)
    match = 0
    # checking to see if the dicts both have the same key
    for key in s1_dict:
        if key in s2_dict:
            # if they do, I want to grab the smaller value so I don't overcount matches
            if s1_dict[key] < s2_dict[key]:
                match += s1_dict[key]
            else:
                match += s2_dict[key]

    answer = s1_length - match
    return answer


answer = anagram(s)
print(answer)
