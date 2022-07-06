# os.name : işletim istemini öğrenmeye yarar
#GNu/Linux ve macOS de "posix"
#Windows da ise "nt" çıktısını verecektir

# os.sep işletim sistemilerinin dosya yollarında kullanılan ayracı görmek için kullanırız 
#windows için \\, linux için / işaretleri kullanılır

# print(os.getcwd()) : hangi dizinde olduğumuzu görüntülemek için kullanılır

# os.chdir("klasöryolu") : dizin değiştirme

# print(os.listdir("klasöryolu")) : bulunduğu dizinin içeriğini okuma

"""listdir() i for ile kullanmak :
    for içerik in os.listdir():
        print(içerik)
        
//bu şekilde daha düzgün bir biçimde liseteleme yapabilirsiniz
"""

# os.mkdir("klasörismi") : yeni klasör oluşturur

# os.makedirs("d1/d2/d3") : çoklu dizin oluşturmak için 

# os.rmdir("klasörismi") : boş klasörleri silmek için kullanılır 

# os.rename("dosyaismi.txt",değişecekisim.py) : klasör ismi değiştirmek için kullanılır

# print(os.stat("dosyaismi")) : herhangi bir dosya hakkında bilgi verir

#bu doküman bu kütüphaneye ait kısa bir özet kütüphaneye hakim olmak istiyorsanız 
#farklı kaynaklara da göz atabilirsiniz :D