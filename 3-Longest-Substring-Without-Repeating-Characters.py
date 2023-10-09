def length_of_longest_substring(s):
    max_length = 0

    for i in range(len(s)):
        char_set = set()
        substring_length = 0

        for j in range(i, len(s)):
            if s[j] not in char_set:
                char_set.add(s[j])
                substring_length += 1
                max_length = max(max_length, substring_length)
            else:
                break

    return max_length

input_string = "abcabcbb"
result = length_of_longest_substring(input_string)
print(result)
