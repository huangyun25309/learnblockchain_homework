import hashlib
import time
from functools import wraps

def timer(func):
    """装饰器：打印函数的执行时间"""
    @wraps(func)  # 保留原函数的元信息（如函数名、文档字符串）
    def wrapper(*args, **kwargs):
        start = time.perf_counter()      # 开始时间
        result = func(*args, **kwargs)   # 执行原函数
        end = time.perf_counter()        # 结束时间
        print(f"{func.__name__} 执行耗时: {end - start:.4f} 秒")
        return result
    return wrapper

@timer
def Cal_hash(nickname):
    nonce = 0
    while(1):
        string_to_hash = nickname + str(nonce)
        # 创建一个sha256对象
        sha256_obj = hashlib.sha256()
        # 更新对象，传入要哈希的数据
        sha256_obj.update(string_to_hash.encode('utf-8'))  # 字符串需要编码为字节串
        # 获取十六进制格式的哈希值
        hash_hex = sha256_obj.hexdigest()
        if hash_hex[:5] == '00000':
            print(string_to_hash)
            print("SHA256 Hash:", hash_hex)
            break
        else:
            nonce += 1

nickname = '云朵飘飘'
Cal_hash(nickname)
