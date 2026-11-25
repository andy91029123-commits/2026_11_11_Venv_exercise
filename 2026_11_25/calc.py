def divide(a, b):
    """回傳 a 除以 b 的結果；當 b 為 0 時拋出 ValueError。"""
    if b == 0:
        raise ValueError("除數不可為零")
    return a / b
