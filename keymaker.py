import string


def alphabet_maker():
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    return alphabet_list


def shift_characters(word, shift):
    word = word.lower()
    alphabet_list = alphabet_maker()
    shifted_word = ""
    for char in word:
        index = alphabet_list.index(char) + shift
        if index >= len(alphabet_list):
            index = index - len(alphabet_list)
        shifted_word = shifted_word + alphabet_list[index]
    return shifted_word


def pad_up_to(word, shift, n):
    word = word.lower()
    alphabet_list = alphabet_maker()
    shifted_word = shift_characters(word, shift)
    new_word = word + shifted_word
    while len(new_word) < n:
        shifted_word = shift_characters(word, shift)
        for letter in shifted_word:
            if len(new_word) < n:
                new_word += letter
            elif len(new_word) == n:
                break
    return new_word


def abc_mirror(word):
    word = word.lower()
    alphabet_list = alphabet_maker()
    mirrored_word = ""
    for char in word:
        index = alphabet_list.index(char)
        index = len(alphabet_list) - index - 1
        mirrored_word += alphabet_list[index]
    return mirrored_word


def create_matrix(word1, word2):
    alphabet_list = alphabet_maker()
    c_matrix = []
    for i in word2:
        word2_index = alphabet_list.index(i)
        shifting = shift_characters(word1, word2_index)
        c_matrix.append(shifting)
    return c_matrix


def zig_zag_concatenate(matrix):
    new_word = ""
    length = len(matrix[0])
    index = 0
    while True:
        if index < length:
            for elements in matrix:
                new_word += elements[index]
            index += 1
        elif index == length:
            break
        if index < length:
            for elements in matrix[::-1]:
                new_word += elements[index]
            index += 1
        elif index == length:
            break
    return new_word


def rotate_right(word, n):
    word = word.lower()
    word_chars_list = [char for char in word]
    rotated_to_right = ""
    for i in range(n):
        word_chars_list.insert(0, word_chars_list[-1])
        del word_chars_list[-1]
    for chars in word_chars_list:
        rotated_to_right += chars
    return rotated_to_right


def get_square_index_chars(word):
    square_shifted_word = ""
    for char in word:
        index = word.index(char)
        index = index * index
        if index > len(word) - 1:
            break
        elif index <= len(word) - 1:
            square_shifted_word += word[index]
    return square_shifted_word


def remove_odd_blocks(word, block_length):
    new_string_with_spaces = ""
    index = -1
    for char in word:
        index = index + 1
        if (index + 1) % block_length != 0:
            new_string_with_spaces = new_string_with_spaces + char
        elif (index + 1) % block_length == 0:
            new_string_with_spaces = new_string_with_spaces + (char + " ")
        # Spaces added to word's characters by block length
    split_word = new_string_with_spaces.split(" ")
    # word splitted by the spaces to the asked blocks
    final_result_string = ""
    index = -1
    for elements in split_word:
        index = index + 1
        if (index - 1) % 2 != 0:
            final_result_string = final_result_string + elements
    return final_result_string


def reduce_to_fixed(word, n):
    index = -1
    reduced_word = ""
    for char in word:
        index = index + 1
        if index < n:
            reduced_word = reduced_word + char
    left_rotated = reduced_word[(n // 3):] + reduced_word[:(n // 3)]
    final = left_rotated[::-1]
    return final


def hash_it(word):
    """
    >>> hash_it('morpheus')
    'trowdo'
    """
    padded = pad_up_to(word, 15, 19)
    elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
    rotated = rotate_right(elongated, 3000003)
    cherry_picked = get_square_index_chars(rotated)
    halved = remove_odd_blocks(cherry_picked, 3)
    key = reduce_to_fixed(halved, 6)
    return key


if __name__ == '__main__':
    hash_it(word='morpheus')
    name = input("Enter your name! ").lower()
    print(f'Your key: {hash_it(name)}')
