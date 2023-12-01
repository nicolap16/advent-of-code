with open('input.txt') as f:
    lines = f.readlines()

    calib_values = []

    temp_digit = []

    for line in lines:
        for character in line:
            if character.isnumeric() == True:
                temp_digit.append(character)

        digit = ''
        if 0 < len(temp_digit):
          digit = temp_digit[0] + temp_digit[-1]
        calib_values.append(int(digit))
        temp_digit = []
  
    total = sum(calib_values)

    print(f'The total is: {total}')

f.close()