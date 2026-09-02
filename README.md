# Kelas-E-Algoritma-Pemrograman

# 🧮 Logika Matematika – Menentukan Jenis Segitiga Berdasarkan Panjang Sisi

## 📝 Deskripsi Masalah

Dalam pembelajaran matematika, segitiga merupakan salah satu bangun datar yang memiliki tiga sisi. Berdasarkan panjang sisinya, segitiga dapat dibedakan menjadi **segitiga sama sisi, segitiga sama kaki, dan segitiga sembarang**.

Untuk membantu siswa memahami materi tersebut, dibuat sebuah program sederhana yang dapat menentukan jenis segitiga berdasarkan panjang ketiga sisinya. Program akan menerima tiga nilai sebagai input, yaitu panjang sisi pertama, sisi kedua, dan sisi ketiga.

Program kemudian membandingkan ketiga sisi tersebut menggunakan logika matematika. Jika ketiga sisi memiliki panjang yang sama, maka segitiga termasuk **segitiga sama sisi**. Jika terdapat dua sisi yang memiliki panjang sama, maka segitiga termasuk **segitiga sama kaki**. Jika ketiga sisi memiliki panjang yang berbeda, maka segitiga termasuk **segitiga sembarang**.

Program ini menerapkan konsep **perbandingan, operator logika, dan percabangan** untuk menyelesaikan permasalahan matematika secara sederhana dan sistematis.

---

## 📥 Input-Proses-Output

### **Input**

Program menerima tiga buah nilai berupa panjang sisi segitiga:

* `sisi1` = panjang sisi pertama
* `sisi2` = panjang sisi kedua
* `sisi3` = panjang sisi ketiga

### **Proses**

Program melakukan perbandingan terhadap ketiga panjang sisi:

1. Jika `sisi1 = sisi2` dan `sisi2 = sisi3`, maka segitiga adalah **segitiga sama sisi**.
2. Jika terdapat dua sisi yang memiliki panjang sama, maka segitiga adalah **segitiga sama kaki**.
3. Jika ketiga sisi memiliki panjang yang berbeda, maka segitiga adalah **segitiga sembarang**.

### **Output**

Program menampilkan jenis segitiga berdasarkan panjang ketiga sisinya.

---

## 💻 Pseudocode

```text
START

INPUT sisi1
INPUT sisi2
INPUT sisi3

IF sisi1 = sisi2 AND sisi2 = sisi3 THEN
    OUTPUT "Segitiga sama sisi"

ELSE IF sisi1 = sisi2 OR sisi1 = sisi3 OR sisi2 = sisi3 THEN
    OUTPUT "Segitiga sama kaki"

ELSE
    OUTPUT "Segitiga sembarang"

END IF

END
```

---

## 📊 Flowchart

```mermaid
%%{init: {
  "themeVariables": {
    "fontSize": "12px"
  },
  "flowchart": {
    "nodeSpacing": 15,
    "rankSpacing": 20,
    "padding": 8
  }
}}%%

flowchart TD
    A([START]) --> B[/INPUT sisi1, sisi2, sisi3/]
    B --> C{Apakah sisi1 = sisi2<br/>dan sisi2 = sisi3?}

    C -->|Ya| D[/OUTPUT<br/>"Segitiga sama sisi"/]
    C -->|Tidak| E{Apakah ada dua sisi<br/>yang sama?}

    E -->|Ya| F[/OUTPUT<br/>"Segitiga sama kaki"/]
    E -->|Tidak| G[/OUTPUT<br/>"Segitiga sembarang"/]

    D --> H([END])
    F --> H
    G --> H

    style A fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a
    style B fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d
    style C fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f
    style D fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d
    style E fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f
    style F fill:#e0e7ff,stroke:#4f46e5,stroke-width:2px,color:#312e81
    style G fill:#fee2e2,stroke:#dc2626,stroke-width:2px,color:#7f1d1d
    style H fill:#dbeafe,stroke:#2563eb,stroke-width:2px,color:#1e3a8a
```

---

## 🧪 Test Case

| Test Case | Input Sisi 1 | Input Sisi 2 | Input Sisi 3 | Kondisi             | Hasil yang Diharapkan |
| --------- | -----------: | -----------: | -----------: | ------------------- | --------------------- |
| 1         |            5 |            5 |            5 | Ketiga sisi sama    | Segitiga sama sisi    |
| 2         |            5 |            5 |            8 | Dua sisi sama       | Segitiga sama kaki    |
| 3         |            4 |            5 |            6 | Ketiga sisi berbeda | Segitiga sembarang    |

---

## 🐍 Implementasi Python

Program dibuat menggunakan bahasa pemrograman **Python** dan dijalankan melalui **Visual Studio Code**. Program menggunakan percabangan `if`, `elif`, dan `else`, serta operator logika `and` dan `or` untuk menentukan jenis segitiga.

### **Source Code `main.py`**

```python
sisi1 = int(input("Masukkan panjang sisi 1: "))
sisi2 = int(input("Masukkan panjang sisi 2: "))
sisi3 = int(input("Masukkan panjang sisi 3: "))

if sisi1 == sisi2 and sisi2 == sisi3:
    print("Segitiga sama sisi")
elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
    print("Segitiga sama kaki")
else:
    print("Segitiga sembarang")
```

---

## 📸 Hasil Pengujian

Program telah diuji menggunakan tiga kondisi yang berbeda. Pengujian pertama menggunakan panjang sisi **5, 5, dan 5**, sehingga program menghasilkan **"Segitiga sama sisi"**.
<img width="932" height="168" alt="Screenshot 2026-09-02 130032" src="https://github.com/user-attachments/assets/50ba710a-34fe-4716-bb72-98c9d17ccd24" />

Pengujian kedua menggunakan panjang sisi **5, 5, dan 8**. Karena terdapat dua sisi yang memiliki panjang sama, program menghasilkan **"Segitiga sama kaki"**.
<img width="925" height="158" alt="Screenshot 2026-09-02 125959" src="https://github.com/user-attachments/assets/287cd606-db22-45e8-8038-843a1980720a" />

Pengujian ketiga menggunakan panjang sisi **4, 5, dan 6**. Karena ketiga sisi memiliki panjang yang berbeda, program menghasilkan **"Segitiga sembarang"**.
<img width="917" height="140" alt="Screenshot 2026-09-02 130052" src="https://github.com/user-attachments/assets/9962483c-d88b-4f7f-8571-e8d44420d63b" />

Berdasarkan hasil pengujian tersebut, program dapat menentukan jenis segitiga dengan benar sesuai dengan kondisi panjang ketiga sisinya.

---

## 📌 Kesimpulan

Berdasarkan program yang telah dibuat, dapat disimpulkan bahwa **logika matematika dapat diterapkan dalam pemrograman untuk menyelesaikan permasalahan sehari-hari maupun permasalahan dalam pembelajaran matematika**.

Pada program ini, konsep perbandingan panjang sisi digunakan bersama dengan operator logika dan percabangan untuk menentukan jenis segitiga. Dengan adanya program ini, proses menentukan jenis segitiga berdasarkan panjang sisinya dapat dilakukan dengan lebih cepat dan mudah.
