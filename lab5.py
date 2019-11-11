from random import randint
from math import log2


def rand_error(_words):
    words = _words.copy()
    for i in range(len(words)):
        error = randint(1, 5)
        if error != 1:
            bit = randint(0, len(words[i]) - 1)
            bit_list = list(words[i])
            bit_list[bit] = '1' if bit_list[bit] == '0' else '0'
            words[i] = ''.join(bit_list)
    return words


def add_even(_words):
    words = _words.copy()
    for i in range(len(words)):
        words[i] = words[i] + ('0' if sum(map(int, words[i])) % 2 == 0 else '1')
    return words


def inverse(string):
    return ''.join('0' if ch == '1' else '1' for ch in string)


def add_inverse(_words):
    words = _words.copy()
    for i in range(len(words)):
        words[i] = words[i] + (words[i] if sum(map(int, words[i])) % 2 == 0 else inverse(words[i]))
    return words


def corelation(_words):
    words = _words.copy()
    for i in range(len(words)):
        temp_word = []
        for j in range(len(words[i])):
            temp_word.append("10" if words[i][j] == "1" else "01")
        words[i] = ''.join(temp_word)
    return words


def berger(_words):
    words = _words.copy()
    for i in range(len(words)):
        r = 1
        while r < log2(len(words[i]) + 1):
            r += 1
        tale = bin(sum(map(int, words[i])))[2:]
        if len(tale) < r:
            temp = ''.join('0' for _ in range(r - len(tale)))
            tale = temp + tale
        words[i] += inverse(tale)
    return words


def num_of_bits(size):
    i = 0
    while 2 ** i <= size + i:
        i += 1
    return i


def num_of_bits_code(size):
    i = 0
    while 2. ** i <= size:
        i += 1

    return i


def heming(_words):
    words = _words.copy()
    for i in range(len(words)):
        k = num_of_bits(len(words[i]))
        word = list()
        loop_c = 0
        par_bits = 0
        data_bits = 0
        while loop_c < k + len(words[i]):
            if loop_c == 2 ** par_bits - 1:
                word.insert(loop_c, '0')
                par_bits += 1
            else:
                word.insert(loop_c, words[i][data_bits])
                data_bits += 1
            loop_c += 1

        loop_c = 0
        p = 1
        while loop_c < k:
            p = 2 ** loop_c
            j = 1
            total = 0
            while j * p - 1 < len(word):
                if j * p - 1 == len(word) - 1:
                    temp = word[j * p - 1:len(word)]
                elif (j + 1) * p - 1 >= len(word):
                    temp = word[j * p - 1:len(word)]
                elif (j + 1) * p - 1 < len(word) - 1:
                    temp = word[(j * p) - 1:(j + 1) * p - 1]
                total = total + sum(int(e) for e in temp)
                j += 2
            if total % 2 > 0:
                word[p - 1] = '1'
            loop_c += 1

        words[i] = ''.join(word)

    return words


def even_check(_words):
    is_error = []
    for i in range(len(_words)):
        if sum(map(int, _words[i])) % 2 != 0:
            is_error.append("Error")
        else:
            is_error.append("No error")
    return is_error


def inverse_check(_words):
    is_error = []
    for i in range(len(_words)):
        if sum(map(int, _words[i][:int(len(_words[i]) / 2)])) % 2 == 0:
            left = _words[i][:int(len(_words[i]) / 2)]
            right = _words[i][int(len(_words[i]) / 2):]
            if left == right:
                is_error.append("No error")
            else:
                is_error.append("Error")
        else:
            left = _words[i][:int(len(_words[i]) / 2)]
            right = inverse(_words[i][int(len(_words[i]) / 2):])
            if left == right:
                is_error.append("No error")
            else:
                is_error.append("Error")
    return is_error


def corelation_check(_words):
    is_error = []
    for word in _words:
        err = False
        for i in range(0, len(word), 2):
            if word[i] == word[i + 1]:
                err = True
                break
        is_error.append("Error" if err else "No error")
    return is_error


def berger_check(_words):
    is_error = []
    for word in _words:
        k = 0
        for i in range(1, len(word)):
            if 2 ** i - 1 >= len(word) - i:
                k = len(word) - i
                break
        info = word[:k]
        control = word[k:]
        control_int = int(control, 2)
        info_sum_bin = bin(sum(map(int, info)))[2:]
        info_sum_int = int(inverse(''.join('0' for _ in range(len(control) - len(info_sum_bin))) + info_sum_bin), 2)
        if info_sum_int == control_int:
            is_error.append("No error")
        else:
            is_error.append("Error")
    return is_error


def heming_check(_words):
    is_error = []
    words = _words.copy()
    for i in range(len(words)):
        n = num_of_bits_code(len(words[i]))
        j = 0
        word = list(words[i])
        error_bit = 0
        while j < n:
            k = 2**j
            q = 1
            total = 0
            while q * k - 1 < len(word):
                if q * k - 1 == len(word) - 1:
                    temp = word[q*k-1:len(word)]
                elif (q + 1) * k - 1 >= len(word):
                    temp = word[q*k-1:len(word)]
                elif (q + 1) * k - 1 < len(word) - 1:
                    temp = word[(q*k)-1:(q+1)*k-1]

                total = total + sum(int(e) for e in temp)
                q += 2
            if total % 2 > 0:
                error_bit += k
            j += 1

        if error_bit >= 1:
            is_error.append("Error in bit " + str(error_bit))
            if word[error_bit-1] == '0':
                word[error_bit-1] = '1'
            else:
                word[error_bit-1] = '0'
            words[i] = ''.join(word)
        else:
            is_error.append("No error")
    return is_error, words


def heming_decode(_words):
    decoded_words = []
    for word in _words:
        decoded_word = []
        i = 0
        j = 0
        k = 0
        while i < len(word):
            if i != (2 ** k - 1):
                temp = word[i]
                decoded_word.append(temp)
                j += 1
            else:
                k += 1
            i += 1
        decoded_words.append(''.join(decoded_word))
    return decoded_words


def print_table(words, encoded_words, error_codes, is_error):
    print("{0:10}   {1:15}   {2:20}   {3:10}".format("Word", "Encoded word", "Encoded word (error)", "Error"))
    for i in range(len(words)):
        print("{0:10}   {1:15}   {2:20}   {3:10}".format(words[i], encoded_words[i], error_codes[i], is_error[i]))


def print_table_heming(words, encoded_words, error_codes, is_error, fixed):
    print("{0:10}   {1:15}   {2:20}   {3:15}   {4:15}".format("Word", "Encoded word", "Encoded word (error)", "Error",
                                                              "Decoded word"))
    for i in range(len(words)):
        print("{0:10}   {1:15}   {2:20}   {3:15}   {4:15}".format(words[i], encoded_words[i], error_codes[i],
                                                                   is_error[i], fixed[i]))


words_first = ['110', '111', '010', '011', '001', '100', '0000', '0001', '1011', '1010']
words_second = ['010', '011', '101', '0000', '0010', '0011', '1100', '1101', '1111', '11101']
words_third = ['10', '0010', '0011', '0100', '0101', '0110', '0111', '1100', '1101', '1110', '1111', '00000', '00001',
               '00010', '00011']
words_fourth = ['000', '0100', '0101', '0111', '10000', '10010', '10011', '10101', '10110', '11000', '11001', '11010',
                '11100', '11101', '11111']


"""
Calls for data sets:
1. Encode with method (function with method in name)
2. Make random errors (rand_error function)
3. Check for error (check functions)
4. Decode (only with hamming codes) - haming_deocde function
5. Print result (print_table or print_table_heming)
"""
encoded_words = heming(words_fourth)
error_words = rand_error(encoded_words)
is_error, fixed_words = heming_check(error_words)
decoded = heming_decode(fixed_words)
print_table_heming(words_fourth, encoded_words, error_words, is_error, decoded)
