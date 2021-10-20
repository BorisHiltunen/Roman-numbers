class App:
    
    def roman_Numbers(n):
        roman = "IIIVIIIX"
        answer = ""
        list = []
        list1 = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
        list2 = [roman[:-7], roman[:-6], roman[:-5], roman[2:-4], roman[3:-4], roman[3:-3], roman[3:-2], roman[3:-1], roman[6:], roman[7:]]
        if n == 0:
            return None
        if n < 11:
            return list1[n-1]
        if n < 40:
            for number in str(n):
                list.append(int(number))
            if list[1] == 0:
                answer += "X" * list[0]
            else:
                answer += "X" * list[0] + list1[list[1]-1]
            return answer
        if n < 50:
            for number in str(n):
                list.append(int(number))
            if list[1] == 0:
                return "XL"
            else:
                answer += "XL" + list1[list[1]-1]
            return answer
        if n == 50:
            return "L"
        if n < 90:
            for number in str(n):
                list.append(int(number))
            if list[1] == 0:
                answer += "L" + "X" * (list[0]-5)
            else:
                answer += "L" + "X" * (list[0]-5) + list1[list[1]-1]
            return answer
        if n < 100:
            for number in str(n):
                list.append(int(number))
            if list[1] == 0:
                return "XC"
            else:
                answer += "XC" + list1[list[1]-1]
            return answer
        if n == 100:
            return "C"
        if n == 200:
            return "CC"
        if n == 300:
            return "CCC"
        if n < 400:
            combo = ""
            for number in str(n):
                list.append(int(number))
            combo = str(list[1]) + str(list[2])
            answer += ("C" * list[0]) + App.roman_Numbers(int(combo))
            return answer
        if n == 400:
            return "CD"
        if n < 500:
            combo = ""
            for number in str(n):
                list.append(int(number))
            combo = str(list[1]) + str(list[2])
            answer += "CD" + App.roman_Numbers(int(combo))
            return answer
        if n == 500:
            return "D"
        if n == 600:
            return "DC"
        if n == 700:
            return "DCC"
        if n == 800:
            return "DCCC"
        if n < 900:
            combo = ""
            for number in str(n):
                list.append(int(number))
            combo = str(list[1]) + str(list[2])
            answer += "D" + ("C" * (list[0]-5)) + App.roman_Numbers(int(combo))
            return answer
        if n == 900:
            return "CM"
        if n < 1000:
            combo = ""
            for number in str(n):
                list.append(int(number))
            combo = str(list[1]) + str(list[2])
            answer += "CM" + App.roman_Numbers(int(combo))
            return answer
        if n == 1000:
            return "M"

    def roman_list(n: list):
        new_list = []
        for number in n:
            new_list.append((number, App.roman_Numbers(number)))
        return new_list

if __name__ == "__main__":
    count = 876
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(App.roman_Numbers(count))
    print(App.roman_list(list))