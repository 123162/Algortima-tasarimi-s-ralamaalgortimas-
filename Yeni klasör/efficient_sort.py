import random
import statistics

def search_all(matrix, value):
    # Matrix satır ve sütun sayısı alınır
    rows = len(matrix)
    cols = len(matrix[0])

    # Satır ve sütun indeksleri 0'dan başlatılır
    row = 0
    col = cols - 1

    # Toplam karşılaştırma sayısı sıfır olarak başlatılır
    count = 0

    # Sonuç listesi oluşturulur
    result = []

    # Matrisin sol üst köşesinden başlanır ve arama yapılır
    while row < rows and col >= 0:
        # Karşılaştırma sayısı artırılır
        count += 1

        # Eğer aranan değer, mevcut indeksteki değerden küçükse, sütun indeksi azaltılır
        if matrix[row][col] > value:
            col -= 1
        # Eğer aranan değer, mevcut indeksteki değerden büyükse, satır indeksi artırılır
        elif matrix[row][col] < value:
            row += 1
        # Eğer aranan değer, mevcut indeksteki değere eşitse, sonuç listesine pozisyon ve karşılaştırma sayısı eklenir
        # ve satır ve sütun indeksleri azaltılarak arama devam edilir
        else:
            result.append((row, col, count))
            col -= 1
            row += 1

    # Sonuç listesi döndürülür
    return result



matrix = [[10 ,30 ,45 ,50 ,58 ,71 ,79 ,86 ,89 ,93 ,99 ,107,112],
          [13 ,34 ,48 ,66 ,69 ,78 ,85 ,88 ,94 ,96 ,100,115,118],
          [15 ,44 ,51 ,67 ,72 ,83 ,87 ,91 ,97 ,103,105,117,121],
          [17 ,46 ,53 ,70 ,74 ,84 ,90 ,93 ,98 ,104,109,120,189],
          [23 ,55 ,64 ,77 ,81 ,93 ,101,111,116,122,130,147,201],
          [37 ,65 ,73 ,80 ,82 ,106,110,119,125,129,152,169,205],
          [39 ,68 ,76 ,102,108,113,114,124,131,137,161,178,210],
          [40 ,93 ,123,126,140,144,148,150,157,160,162,202,267],
          [43 ,128,133,135,149,164,166,171,177,183,192,204,301],
          [400,500,600,700,800,900,901,902,903,904,905,906,909]]

keys = [30, 107, 51, 93, 162, 123, 111, 134, 300]

for key in keys:
    result = search_all(matrix, key)
    print(f"Key {key} için:")
    print(f"Pozisyonlar: {result}")
    print(f"Toplam yapılan karşılaştırma: {sum([t[2] for t in result])}")
    print()





# 1 ve 130 arasında olan elemanların listesini oluşturun
elements = [elem for row in matrix for elem in row if 1 <= elem <= 130]

# 50 tane rastgele eleman seçin
selected_elements = random.sample(elements, 50)

print("\nrastgele oluşturulan dizi:\n", selected_elements)


# Karşılaştırma sayılarını tutan liste oluşturun
comparison_counts = []

# Her bir eleman için arama işlemini yapın
for elem in selected_elements:
    result = search_all(matrix, elem)
    # Eğer sonuç listesi boş değilse, karşılaştırma sayısını listeye ekleyin
    if result:
        comparison_counts.append(result[0][2])

# Karşılaştırma sayılarının ortalamasını ve standart sapmasını hesaplayın
mean = statistics.mean(comparison_counts)
stdev = statistics.stdev(comparison_counts)
print("\n\n\n")
print("Ortalama:", mean)
print("Standart Sapma:", stdev)











