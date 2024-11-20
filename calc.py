
def calc(string):
    dct_1 = {number: word for word, number in enumerate("один два три четыре пять шесть семь восемь девять".split(), 1)}
    dict_10 = {number: word for word, number in enumerate("десять одиннадцать двенадцать тринадцать четырнадцать пятнадцать шестнадцать семнадцать восемнадцать девятнадцать".split(),10)}
    dict_20 = {number: word * 10 for word, number in enumerate("двадцать тридцать сорок пятьдесят шестьдесят семьдесят восемьдесят девяносто".split(), 2)}
    dct_100 = {number: 100 * word for word, number in enumerate('сто двести триста четыреста пятьсот шестьсот семьсот восемьсот девятьсот'.split(), 1)}
    dct_operation = {'плюс': '+', 'минус': '-', 'умножить': '*', 'разделить': '/'}

    dct = {**dct_1, **dict_10, **dict_20, **dct_100, **dct_operation}

    def parsing_in_line(string):
        """Преобразует строку с выражанием в строку  с числовым выражением"""
        words = string.split()
        result = ""
        check_num = 0

        element = 0
        while element < len(words):
            word = words[element]
            if word in dct:
                value = dct[word]
                if word in dct_1 or word in dict_10 or word in dict_20 or word in dct_100:
                    check_num += value  # Добавляем числовое значение
                elif word in dct_operation:
                    if check_num != 0:
                        result += str(check_num)
                        check_num = 0
                    result += dct_operation[word]
            elif word == "скобка" and element + 1 < len(words):
                next_word = words[element + 1]
                if next_word == "открывается":
                    if check_num != 0:
                        result += str(check_num)
                        check_num = 0
                    result += "("
                    element += 1
                elif next_word == "закрывается":
                    if check_num!= 0:
                        result += str(check_num)
                        check_num= 0
                    result += ")"
                    element += 1

            element += 1

        if check_num != 0:
            result += str(check_num)

        return result

    parsed_expression = parsing_in_line(string)
    result = eval(parsed_expression)
    return  result

def number_to_words(number):
    dct_units = {
        1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять",
        6: "шесть", 7: "семь", 8: "восемь", 9: "девять"
    }

    dct_teens = {
        10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать",
        14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать",
        18: "восемнадцать", 19: "девятнадцать"
    }

    dct_tens = {
        2: "двадцать", 3: "тридцать", 4: "сорок", 5: "пятьдесят",
        6: "шестьдесят", 7: "семьдесят", 8: "восемьдесят", 9: "девяносто"
    }

    if number == int(number):
        number = int(number)
        words = []
        if number == 0:
            return "ноль"

        if number < 0:
            words.append("минус")
            number = abs(number)

        if number >= 100:
            hundreds = number // 100
            words.append(
                ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"][
                    hundreds - 1])
            number %= 100

        if 10 <= number <= 19:
            words.append(dct_teens[number])
        else:
            tens = number // 10
            if tens > 1:
                words.append(dct_tens[tens])
            number %= 10

            if number in dct_units:
                words.append(dct_units[number])

        return " ".join(words)


string = input("Введите выражние: ")
result = calc(string)
print(f"{string} -> {number_to_words(result)}")
