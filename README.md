#saveCSV#

saveCSV Sınıfı Kullanım Kılavuzu

Bu Python sınıfı, CSV dosyaları üzerinde okuma, yazma ve düzenleme işlemleri yapmak için kullanılabilir. Sınıf, csv modülünü kullanarak çalışır ve özel bir CSV biçimi belirtmezseniz, tüm girdiler ve çıktılar varsayılan olarak virgülle ayrılmış dosyalar olarak ele alınır.

Kurulum
Bu sınıfı kullanmak için, Python 3 veya sonraki bir sürümünün kurulu olması gereklidir. Ayrıca, csv modülü, Python standart kütüphanesinin bir parçası olduğundan, bu sınıfı kullanmak için başka bir kurulum gerektirmez.

Nasıl Kullanılır?
İlk adım, saveCSV sınıfını dosyanızın başına eklemektir. Ardından, sınıfı kullanarak CSV dosyanızı açabilirsiniz.

from saveCSV import saveCSV

# örnek bir dosya yolu
file_path = 'my_file.csv'

# saveCSV sınıfını kullanarak dosyayı açın
my_csv = saveCSV(file_path)

Satır Ekleme
CSV dosyanıza satır eklemek için, add_row veya add_rows yöntemlerini kullanabilirsiniz.
# tek bir satır eklemek için
my_csv.add_row(['Alice', 'Smith', 25])

# birden fazla satır eklemek için
new_rows = [
    ['John', 'Doe', 30],
    ['Jane', 'Doe', 28]
]
my_csv.add_rows(new_rows)

Satır Okuma
CSV dosyanızdaki belirli bir satırı okumak için, read_row yöntemini kullanabilirsiniz. Bu yöntem, belirli bir satır sayısını alır ve o satırı bir liste olarak döndürür.
# belirli bir satırı okumak için
third_row = my_csv.read_row(3)
print(third_row)
# Output: ['John', 'Doe', 30]

CSV dosyanızdaki tüm satırları okumak için, read_rows yöntemini kullanabilirsiniz. Bu yöntem, dosyadaki tüm satırları bir liste olarak döndürür.
# tüm satırları okumak için
all_rows = my_csv.read_rows()
print(all_rows)
# Output: [['Alice', 'Smith', 25], ['Bob', 'Johnson', 35], ['John', 'Doe', 30], ['Jane', 'Doe', 28]]

Dosyayı Kapatma
CSV dosyanızı kapatmak için, close yöntemini kullanabilirsiniz.
my_csv.close()

Parametreler
saveCSV sınıfı, aşağıdaki parametreleri alabilir:

filepath: CSV dosyasının yolu. Eğer dosya yoksa, bu parametre ile belirtilen isimde bir dosya oluşturulur.
justreading: Bu parametre, dosyanın sadece okuma modunda açılmasını sağlar. Bu varsayılan olarak False olarak ayarlanır ve dosya yazma modunda açılır. justreading değeri True olarak ayarlanırsa, dosya yalnızca okuma modunda açılır.



