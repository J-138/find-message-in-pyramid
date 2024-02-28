def decode(message_file):
    f = open(message_file)
    lines = f.readlines()
    pyramid_dict = {}
    pyramid = []

    for line in lines:
        split = line.split()
        pyramid_dict[split[0]] = split[1]

    pyramid_width = 1
    curr_width = 0
    curr_layer = []
    for i in range(1, len(pyramid_dict) + 1):
        curr_layer.append(i)
        curr_width += 1

        if curr_width == pyramid_width:
            pyramid.append(curr_layer)
            curr_width = 0
            pyramid_width += 1
            curr_layer = []

    end_number = []
    for layer in pyramid:
        end_number.append(layer[-1])

    ans = ''
    for number in end_number:
        ans += f'{pyramid_dict[str(number)]} '
        
    ans = ans.lower()
    ans = ans.strip()
    print(f'{ans}')

decode('coding_qual_input.txt')