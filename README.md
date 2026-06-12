# Encryption-Program
Encrypt and Decrypt program made by Python, Which's build with Fernet, argon2id than this encrypt could got score 8 of Entropy to make sure it encrypt is safely


### Requirements / 環境需求
* Python 3.8+
* pip install cryptography argon2-cffi


# JaceEncryptor (基於 Argon2id + Fernet 的軍規級本地檔案加密系統)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

An advanced, high-security local file encryption system utilizing Argon2id for key derivation and Fernet for authenticated data encryption, optimized to achieve maximum theoretical ciphertext entropy (~7.99).
一套結合 **Argon2id 記憶體硬性金鑰衍生**與 **Fernet 驗證加密**的高強度本地檔案加解密系統。經深度優化，密文高達 **7.99 完美資訊熵**，外觀毫無規律，徹底杜絕統計學破解。


## 💡 What Makes It Special? / 這套加密系統有何特別？

### 1. Maximum Ciphertext Entropy (~7.99) / 完美的密文隨機度（資訊熵）
* **EN:** Standard Fernet encryption outputs Base64 strings, which restricts data to 64 ASCII characters and reduces randomness. This tool **reverses Base64 encoding into 256-bit raw binary bytes** before writing to disk. CyberChef Shannon Entropy analysis proves it hits **~7.99xxxx** (Theoretical Max: 8.0). It looks like pure cosmic static noise to attackers, leaving zero statistical patterns for cryptanalysis.
* **中文:** 傳統加密工具輸出的密文多為 Base64 字串（只有 64 個字元），容易留下統計學規律。本系統在寫入硬碟前，**將密文強制還原為 256 進位的純二進位數據（Raw Bytes）**。經 CyberChef 香農資訊熵分析，數值高達 **7.99xxxx**（極限值為 8.0），在外觀上毫無規律，徹底阻斷黑客利用頻率分析或統計學反推金鑰。
* <img width="952" height="967" alt="entropy" src="https://github.com/user-attachments/assets/d9bd7553-9738-45da-9fad-200f3e050d27" />

### 2. GPU/ASIC-Resistant KDF (Argon2id) / 抗防禦硬體加速的金鑰衍生
* **EN:** Instead of weak password hashing, we deploy **Argon2id** (the profile winner of the Password Hashing Competition) with custom parameters (`Memory=64MB`, `Time=3`, `Parallelism=4`). This imposes massive memory hard constraints, rendering multi-million dollar GPU/ASIC brute-force clusters completely useless.
* **中文:** 捨棄傳統易被破譯的弱雜湊，引入現役最強的 **Argon2id** 金鑰衍生函數，並配置軍規規格（記憶體開銷 64MB、時間開銷 3、並行度 4）。這使得黑客即使動用數百萬美元的 GPU 顯示卡叢集或 ASIC 專用晶片，也無法進行並行暴力破解。
* Wiki https://en.wikipedia.org/wiki/Argon2

### 3. Smart Keyless Architecture (Salt Prepend) / 免外置金鑰的一體化設計
* **EN:** No more worry about losing `salt.key` or `secret.key`. The system dynamically generates a cryptographic 16-byte random salt for each file and **prepends it directly to the ciphertext binary stream**. The decryption module streams it out fluidly via pointer indexing.
* **中文:** 擺脫了必須單獨保存金鑰或鹽值檔案的致命缺點。系統為每個檔案動態生成獨立的 16 位元組隨機鹽值（Salt），並**一體化拼接在密文流的最前端**。解密時利用二進位指標動態拆解，實現「金鑰隨檔案走」的極高便攜性。

## How to usage? / 如何使用?

### put the program and the files you want to encrypt at same folder. / 將程式與需要加解密的檔案放在同樣的資料夾
<img width="1001" height="403" alt="image" src="https://github.com/user-attachments/assets/ffb5a917-0bce-4416-9b6c-c99b3e06ffe3" />
### Starting encryption and decryption testing. / 開始進行加密和解密測試
<img width="1757" height="392" alt="image" src="https://github.com/user-attachments/assets/46ee2b38-aa53-4bd5-b20e-7c3706ab247c" />
<img width="1836" height="377" alt="image" src="https://github.com/user-attachments/assets/2a329860-9403-4d80-ae41-bcdac6507ce7" />



