Bu python dosyası bir veri depolama aracıdır. CSV, TXT, XML ve Excel dosyalarına veri ekleme, okuma ve kaydetme işlemlerini gerçekleştirmektedir.

saveCSV
Bu sınıf, verilerinizi csv dosyalarında saklamak için tasarlanmıştır. Aşağıdaki yöntemler sağlanmaktadır:

init(self,filepath:str,justreading:bool = False) : Bir dosya yolu alır ve yazma veya sadece okuma işlemi yapacağınızı belirtir.
add_row(self,row) : Bir satır ekleme işlemi yapar.
add_rows(self,rows) : Birden fazla satır ekleme işlemi yapar.
read_row(self,rowcount) : Belirtilen satırdaki verileri okur.
read_rows(self) : Tüm satırlardaki verileri okur.
close(self) : Dosyayı kapatır.
saveEXCEL
Bu sınıf, verilerinizi Excel dosyalarında saklamak için tasarlanmıştır. Aşağıdaki yöntemler sağlanmaktadır:

init(self,FileNAME:str, WorkBookTitle : str,justread:bool) : Bir dosya adı, bir çalışma sayfası adı ve yazma veya sadece okuma işlemi yapacağınızı belirtir.
add_row(self,columns:list) : Bir satır ekleme işlemi yapar.
read_rows(self) : Tüm satırlardaki verileri okur.
saveEXCEL(self) : Dosyayı kaydeder.
saveTXT
Bu sınıf, verilerinizi txt dosyalarında saklamak için tasarlanmıştır. Aşağıdaki yöntemler sağlanmaktadır:

init(self,filename:str,mode:str) : Bir dosya adı ve okuma veya yazma işlemi yapacağınızı belirtir.
add_row(self,Text) : Bir satır ekleme işlemi yapar.
add_rows(self, RowList:list) : Birden fazla satır ekleme işlemi yapar.
read_all(self) : Tüm verileri okur.
read_lines(self) : Tüm satırlardaki verileri okur.
saveTXT(self) : Dosyayı kaydeder.
saveXML
Bu sınıf, verilerinizi XML dosyalarında saklamak için tasarlanmıştır. Aşağıdaki yöntemler sağlanmaktadır:

init(self,filePATH,justreading:bool,tree_name:str = None) : Bir dosya yolu alır, yazma veya sadece okuma işlemi yapacağınızı belirtir.
read(self) : Tüm verileri okur.
find_all(self,element_name) : Verilen element adındaki verileri okur.
create_element(self,element_name: str, elements: list = None, just_return = False) : Verilen element adı ve alt elemanlarını oluşturur.
Kullanım

Örneğin, bir XML dosyasındaki verileri okumak için şu şekilde kullanabilirsiniz:
from saveXML import SaveXML

# Dosya yolu belirleme
xml_file = SaveXML("veriler.xml", justreading=True)

# Tüm verileri okuma
data = xml_file.read()
print(data)

# Belirli bir element adındaki verileri okuma
element_name = "person"
person_data = xml_file.find_all(element_name)
print(person_data)

XML dosyasına veri yazmak için create_element() yöntemi kullanılabilir. Bu yöntem, yeni bir element oluşturur ve alt elementler ekleyebilir.
from saveXML import SaveXML

# Dosya yolu belirleme
xml_file = SaveXML("veriler.xml")

# Yeni bir element oluşturma
element_name = "person"
element_data = {
    "name": "John",
    "surname": "Doe",
    "age": "30"
}
xml_file.create_element(element_name, element_data)

Bu örnekte, "veriler.xml" adlı bir dosya oluşturulur ve "person" adında yeni bir element eklenir. Elementin altındaki "name", "surname" ve "age" adlı alt elementler de belirlenir.

just_return parametresi varsayılan olarak False olarak ayarlanmıştır. Ancak, create_element() yöntemi, belirli bir elementi sadece döndürmek istediğinizde kullanılabilir.
from saveXML import SaveXML

# Dosya yolu belirleme
xml_file = SaveXML("veriler.xml")

# Yeni bir element oluşturma ve yalnızca döndürme
element_name = "person"
element_data = {
    "name": "John",
    "surname": "Doe",
    "age": "30"
}
person_element = xml_file.create_element(element_name, element_data, just_return=True)
print(person_element)


Bu örnekte, "person" adında yeni bir element oluşturulur ve just_return parametresi True olarak ayarlandığından, bu element yalnızca döndürülür ve dosyaya yazılmaz.

Böylece, SaveXML sınıfı kullanarak XML dosyalarında veri okuyabilir ve yazabilirsiniz.
