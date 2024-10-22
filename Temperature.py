def konversisuhu(temperature, value) : #Mendefinisikan fungsi untuk mengonversi suhu antara Celsius dan Fahrenheit
    if value == 'C':  
        temperaturesuhu = (temperature - 32) * 5/9   #Mengonversi dari Fahrenheit ke Celsius
        return temperaturesuhu, 'C'   #Mengembalikan suhu yang dikonversi dan unitnya ('C')
    else:
        temperaturesuhu = (temperature * 9/5) + 32  #Mengonversi dari Celsius ke Fahrenheit
        return temperaturesuhu, 'F'  # Mengembalikan suhu yang dikonversi dan unitnya ('F')
    
celsius_temperature = 30 #Menetapkan suhu dalam Celsius
temperaturesuhu, target_value = konversisuhu(celsius_temperature, 'F') #Memanggil fungsi untuk mengonversi 30°C ke Fahrenheit
print(f"{celsius_temperature}°C dikonversi ke Farenheit adalah {temperaturesuhu}°{target_value}") #Mencetak hasil konversi dengan format yang informatif

fahrenheit_temperature = 86  #Menetapkan suhu dalam Fahrenheit
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'C') #Memanggil fungsi untuk mengonversi 86°F ke Celsius
print(f"{fahrenheit_temperature}°F dikonversi ke Celsius adalah {temperaturesuhu}°{target_value}") #Mencetak hasil konversi dengan format yang informatif