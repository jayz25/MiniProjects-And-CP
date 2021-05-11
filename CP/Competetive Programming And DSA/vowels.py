def check_Vow(string,vowels):
    final = [each for each in string if each  in vowels]
    print(final)
string = 'Jayesh Milind Patil'
vowels = 'AaEeIiOoUu'
check_Vow(string,vowels)