# 🔐 CaesarJaw Encryption & Decryption

## 📌 Description
This Python program provides functionality for encrypting and decrypting text using the **Caesar cipher**. It supports uppercase and lowercase letters, as well as digits, while leaving punctuation and spaces unchanged. The program also allows finding the shift key from encrypted and decrypted text and attempts to decrypt text without a known key by brute force.

## ✨ Features
✅ **Encrypt text** using a specified shift key.
✅ **Decrypt text** using a specified shift key.
✅ **Find the shift key** from an encrypted and decrypted text pair.
✅ **Brute-force decryption** to find possible plaintext outputs without knowing the key.

---

## 🚀 Installation & Usage

### 📥 Clone the Repository
To get started, clone the repository using Git:
```sh
git clone https://github.com/mohammedmehdio/CeasarJaw-PY.git
cd CeasarJaw-PY
```

### 🛠 Run the Program
Make sure you have Python installed, then run:
```sh
python main.py
```

### 📌 Options
Once the script runs, select an option:
1️⃣ Encrypt a message.
2️⃣ Decrypt a message.
3️⃣ Find the shift key given an encrypted and decrypted text pair.
4️⃣ Try decrypting text without a key by brute force.

---

## 🎯 Example Usage

### 🔒 Encryption
**Input:**
```
Enter Option (1,2,3 or 4): 1
Enter Shift Key (an integer): 3
Please enter text: Hello123
```
**Output:**
```
==> Output Result: Khoor456
```

### 🔓 Decryption
**Input:**
```
Enter Option (1,2,3 or 4): 2
Enter Shift Key (an integer): 3
Please enter text: Khoor456
```
**Output:**
```
==> Output Result: Hello123
```

### 🔑 Finding the Key
**Input:**
```
Enter Option (1,2,3 or 4): 3
Please enter encrypted text: Khoor
Please enter decrypted text: Hello
```
**Output:**
```
Shift Key: 3
```

### 🤯 Decrypt Without Key (Brute Force)
**Input:**
```
Enter Option (1,2,3 or 4): 4
Please enter text to decrypt without a key: Khoor
```
**Output:**
```
Trying key 1: Jgnnq
Trying key 2: Ifmmp
Trying key 3: Hello
...
```

---

## 👨‍💻 Authors
- **Mohammed Mehdi Boudir**
- **Salah Eddine Rhazouni**

## 📜 License
This project is licensed under the **MIT License** - see the LICENSE file for details.

💡 _If you find this project useful, don't forget to star ⭐ the repo!_

