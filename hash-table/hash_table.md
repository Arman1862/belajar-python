# What is Hash Table?

## Definition

Hash table atau hash map mengacu pada tipe data abstrak yang menyimpan dan mengekstrak data dengan memetakan sebuah key terhadap sebuah value melalui hashing. Hashing adalah penunjukan lokasi untuk menyimpan data atau menemukan data yang disimpan berdasarkan nilai data. Hash function menentukan kunci dengan menggunakan nilai data.


Dalam hash table, terdapat 3 istilah yang perlu kita pahami yaitu put, get dan hash:

- put(key, value) : Menyimpan nilai ke bucket yang ditentukan oleh key hash value
- get(key) : Mengekstrak nilai yang disimpan dalam bucket yang ditentukan oleh key hash value
- hash(key) : Mengonversi key value data menjadi hash value dalam range tertentu


## Ilustration

![first image](https://assets.skilvul.com/lesson/Python/Algorithm+Data+Structure/Scene_86.jpg)
Untuk lebih mengerti lagi mengenai hash table, berikut contoh penerapan dari hash table. Kondisi di bawah adalah kita memiliki 5 judul buku :
- The Little Prince
- The Old Man and the Sea
- The Little Mermaid
- Beauty and the Beast
- The Last Leaf

dan akan kita letakkan dalam sebuah rak buku dengan 8 tempat yang tersedia.

![second image](https://assets.skilvul.com/lesson/Python/Algorithm+Data+Structure/Scene_87.jpg)
Kita juga memerlukan key values untuk masing-masing judul buku, sebagai contoh mari kita ambil nilai ASCII dari judul-judul buku tersebut.

![third image](https://assets.skilvul.com/lesson/Python/Algorithm+Data+Structure/Scene_88.jpg)
![fourth image](https://assets.skilvul.com/lesson/Python/Algorithm+Data+Structure/Scene_89.jpg)
`ord is for take the ASCII CODES`

Terlihat pada contoh kode di atas kita memiliki key yaitu nilai ASCII dari buku-buku tersebut dan value yaitu judul buku tersebut dalam tipe data string.

## Hashing

Dalam hash table, kita juga perlu mengenal konsep yang disebut sebagai hashing. Hashing mengacu pada proses mengubah kunci yang diberikan menjadi kunci lain dan hash function mengacu pada fungsi yang mengubah kunci yang datanya panjang tidak menentu menjadi kunci lain yang memiliki panjang dengan data yang tetap. Kunci yang diubah oleh hash function disebut hash key. Ada 8 slot di rak buku, jadi definisikan fungsi hash sebagai f(x) = x % 8.

Agar lebih jelasnya perhatikan ilustrasi berikut:
![fifth image](https://assets.skilvul.com/lesson/Python/Algorithm+Data+Structure/Scene_90.jpg)

Dengan adanya hash keys, kita merubah key yang tadinya memiliki panjang tidak tentu menjadi panjang yang tetap (pada contoh ini kita kelompokkan menjadi 0 - 7 sesuai dengan slot rak buku).

```1929 -> 1, 1837 -> 5 dan seterusnya (menggunakan fungsi operator modulo % atau sisa pembagian)```