import rsa
import hashlib

# 1. 生成 RSA 公私钥对（2048 位）
(pubkey, privkey) = rsa.newkeys(2048)

# 2. 定义昵称（可自行修改）
nickname = "Alice"

# 3. 寻找符合 POW 条件的 nonce
nonce = 0
while True:
    message = f"{nickname}{nonce}".encode('utf-8')
    hash_hex = hashlib.sha256(message).hexdigest()
    if hash_hex.startswith('0000'):          # 前 4 个字符为 0
        print(f"✅ 找到 nonce：{nonce}")
        print(f"📨 消息：{message.decode()}")
        print(f"🔐 SHA256 哈希：{hash_hex}")
        break
    nonce += 1

# 4. 用私钥对消息进行签名（使用 SHA256 哈希算法）
signature = rsa.sign(message, privkey, 'SHA-256')
print(f"✍️ 签名（十六进制）：{signature.hex()}")

# 5. 用公钥验证签名
try:
    rsa.verify(message, signature, pubkey)
    print("✅ 验证成功，签名有效！")
except rsa.VerificationError:
    print("❌ 验证失败，签名无效。")