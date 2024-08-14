#FUNDAMENTAL PYTHON BASIC


#Question:
#1.Manipulasi List dan fungsi:
#Buatlah sebuah fungsi find_average(numbers) yang menerima sebuah list bilangan dan mengembalikan nilai rata-rata dari bilangan-bilangan tersebut.
#Buat list angka acak sebagai input dan panggil fungsi find_average untuk menghitung rata-ratanya.


def find_average(numbers):
    
    # Pastikan list tidak kosong untuk menghindari pembagian dengan nol
    if len(numbers) == 0:
        return 0
    
    # Hitung jumlah total angka dalam list
    total_sum = sum(numbers)
    
    # Hitung rata-rata dengan membagi total sum dengan jumlah angka
    average = total_sum / len(numbers)
    
    return average

# List angka acak
random_numbers = [5, 10, 15, 25, 30, 40, 60 ]

average_value = find_average(random_numbers)
print(f"Rata-rata dari list {random_numbers} adalah {average_value:.2f}")


#2. Pemahaman string dan fungsi
#Buatlah sebuah fungsi reverse_words(sentence) yang menerima sebuah kalimat dan mengembalikan kalimat tersebut dengan urutan kata-kata dibalik.
#Berikan sebuah kalimat sebagai input dan panggil fungsi reverse_words untuk membalik urutan kata-kata dalam kalimat tersebut.


def reverse_words(sentence):

    
    words = sentence.split() #Pemisah kalimat jadi list kata

    reversed_words = words[::-1] #Pembalik urutan dalam list

    reversed_sentence = ' '.join(reversed_words) #mix words into new sentence

    return reversed_sentence


#contoh kalimat
sentence = "Python adalah salah satu bahasa pemrograman"
reversed_sentence = reverse_words(sentence) #mix words into new sentence
print(f"kalimat yang dibalik: '{reversed_sentence}'")


#3. Pemahaman data casting dan fungsi
#Buatlah sebuah fungsi convert_temperature(degrees, from_unit, to_unit) yang mengonversi suhu dari unit yang diberikan (from_unit) ke unit lainnya (to_unit). Parameter degrees adalah nilai suhu, dan from_unit serta to_unit dapat berupa "C" untuk Celsius, "F" untuk Fahrenheit, atau "K" untuk Kelvin.
#Uji fungsi convert_temperature dengan nilai suhu dan unit yang berbeda untuk melihat konversinya.

def convert_temperature(degrees, from_unit, to_unit):
    
    #Convert unit asal ke celcius
    if from_unit == "C":
        celcius = degrees
    elif from_unit == "F":
        celcius = (degrees - 32) *5/9
    elif from_unit == "K":
        celcius = degrees - 273
    else:
        raise ValueError("unit asal tidak valid")
    
    # Konversi ke unit tujuan
    if to_unit == "C":
        return celcius
    elif to_unit == "F":
        return celcius *9/5 + 32
    elif to_unit == "K":
        return celcius + 273
    else:
        raise ValueError("Unit tujuan tidak valid")
    

print(f"25 Celcius ke Farenhait: {convert_temperature(25, 'C', 'F')} F")
print(f"100 Farenhait ke Celcius: {convert_temperature(100, 'F', 'C')} C")
print(f"300 Kelvin ke Celcius: {convert_temperature(300, 'K', 'C')} C")
print(f"0 Celcius ke Kelvin: {convert_temperature(0, 'C', 'K')} K")
print(f"32 Farenhait ke Kelvin: {convert_temperature(32, 'F', 'K')} K")


#4. Manipulasi Dictionary dan fungsi
#Buatlah sebuah fungsi count_characters(string) yang menghitung jumlah kemunculan setiap karakter dalam sebuah string dan mengembalikan hasilnya dalam bentuk dictionary.
#Berikan sebuah string sebagai input dan panggil fungsi count_characters untuk menghitung jumlah kemunculan setiap karakter dalam string tersebut.

def count_characters(string):

    char_count = {} #Dictionary untuk menyimpan hitungan dalam karakter

    for char in string: #Iterasi karakter di string
        if char in char_count:  #add  number character if in dictionary 
            char_count[char] +=1 #add number 1 if not in dictionary
        else:
            char_count[char] = 1
    return char_count

input_string = "Hello bayu"
character_counts = count_characters(input_string)
print(f"jumlah karakter yang ada dalam '{input_string}': {character_counts}")


#5. Pemahaman list comrehension and fungtion
#Buatlah sebuah fungsi even_square_numbers(n) yang menggunakan list comprehension untuk menghasilkan list bilangan kuadrat dari bilangan genap antara 1 hingga n.
#Panggil fungsi even_square_numbers dengan nilai n tertentu untuk menghasilkan list bilangan kuadrat dari bilangan genap sampai nilai n.

def even_square_numbers(n):

#Menggunakan list comprehension untuk menghasilkan list bilangan kuadrat
    return [x**2 for x in range(2, n+1, 2)]

#Contoh penggunaan
n = 20
squared_even_number = even_square_numbers(n)
print(f"List bilangan kuadrat adri bilangan genap antara 1 hingga {n}: {squared_even_number}")

