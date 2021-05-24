def encoding(data):
    count = 1
    prev_char = ''
    en_char = ''
    for char in data:
        if char != prev_char:
            if prev_char:
                en_char += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    en_char += str(count) + prev_char
    return en_char




data = 'aabcc'
print (encoding(data))

# def rle_encode(data):
#     encoding = ''
#     prev_char = ''
#     count = 1
#
#     # if not data: return ''
#
#     for char in data:
#         # If the prev and current characters
#         # don't match...
#         if char != prev_char:
#             # ...then add the count and character
#             # to our encoding
#             if prev_char:
#                 encoding += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             # Or increment our counter
#             # if the characters do match
#             count += 1
#     else:
#         # Finish off the encoding
#         encoding += str(count) + prev_char
#         return encoding
#
# data = 'aabcc'
# print (rle_encode(data))