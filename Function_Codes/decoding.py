from encoding import encoding


def decoding(a, codes):
    decoded = ''
    code = ''
    for each_index in a:
        code = code + each_index
        for char in codes:
            if code == codes[char]:
                decoded = decoded + char
                code = ''

    return decoded

def txt_to_list(file):
    our_file = open(file, "r")
    list_of_lists = []
    for line in our_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)

    our_file.close()
    return list_of_lists

def txt_to_dict(file):
    details_file = open("passenger_detials.txt", 'r')
    list_of_lists = []
    mobile_attached = {}
    for line in details_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        key_dict = line_list[2]
        line_list.pop(2)
        mobile_attached[key_dict] = line_list
        list_of_lists.append(line_list)
    details_file.close()
    return mobile_attached


def check_decoded(text):
    details_list = txt_to_list("passenger_detials.txt")
    mobile_numbers = []
    for i in details_list:
        mobile_numbers.append(i[2])
    encoded_lists = []
    for j in mobile_numbers:
        # encoded_num_list,tree = encoding(j)
        encoded_lists.append(encoding(j))
    for k in encoded_lists:
        if text == k[0]:
            matched = True
            decoded_num = decoding(text,k[1])
        else:
            matched = False
    dict_details = txt_to_dict("passenger_details.txt")
    return dict_details[decoded_num],matched




