# Python 例外處理（Exception Handling）完整教學：由淺入深

在編寫 Python 程式時，難免會遇到錯誤。例外處理能讓程式在遇到異常時「優雅地處理錯誤」，而不是直接崩潰終止。

---

## 目錄
1. [什麼是例外（Exception）？](#1-什麼是例外exception)
2. [基礎語法：try 與 except](#2-基礎語法try-與-except)
3. [進階捕捉：多重例外與取得錯誤訊息](#3-進階捕捉多重例外與取得錯誤訊息)
4. [完整結構：try ... except ... else ... finally](#4-完整結構try--except--else--finally)
5. [主動引發例外：raise](#5-主動引發例外raise)
6. [自訂例外（Custom Exceptions）](#6-自訂例外custom-exceptions)
7. [進階技巧：例外鏈（Exception Chaining）](#7-進階技巧例外鏈exception-chaining)
8. [Python 風格：EAFP vs LBYL](#8-python-風格eafp-vs-lbyl)
9. [最佳實踐與常見地雷](#9-最佳實踐與常見地雷)

---

## 1. 什麼是例外（Exception）？

Python 的錯誤主要分為兩大類：
- **語法錯誤（Syntax Errors）**：程式碼尚未執行時就被直譯器抓到的語法問題（例如少寫冒號 `:`）。這無法透過例外處理來補救，必須直接修改程式碼。
- **例外（Exceptions）**：語法完全正確，但執行階段（Runtime）發生了非預期的狀況（例如：除以 0、找不到檔案、字串無法轉換為整數）。

### 常見內建例外：
| 例外名稱 | 觸發情境 |
| :--- | :--- |
| `ZeroDivisionError` | 數值除以零 |
| `ValueError` | 傳入無效或不適當的值（如 `int("abc")`） |
| `TypeError` | 型態不符的操作（如 `"5" + 2`） |
| `IndexError` | 清單取值超出索引範圍 |
| `KeyError` | 字典中找不到指定的 Key |
| `FileNotFoundError` | 試圖打開不存在的檔案 |

---

## 2. 基礎語法：try 與 except

最基本的防護網：把可能出錯的程式碼放在 `try` 區塊，若發生錯誤，則執行 `except` 區塊。

### 範例 1：除以零的錯誤防範

```python
try:
    num = 10 / 0
    print(f"結果是：{num}")
except ZeroDivisionError:
    print("錯誤：除數不能為 0！")

print("程式繼續正常執行...")
```

**輸出結果：**
```text
錯誤：除數不能為 0！
程式繼續正常執行...
```

---

## 3. 進階捕捉：多重例外與取得錯誤訊息

### 範例 2：處理多種不同的例外

一段程式碼可能會引發多種不同錯誤，可以撰寫多個 `except` 區塊分別應對。

```python
def calculate_ratio():
    try:
        val1 = input("請輸入被除數：")
        val2 = input("請輸入除數：")
        
        num1 = int(val1)
        num2 = int(val2)
        
        result = num1 / num2
        print(f"計算結果：{result}")
        
    except ValueError:
        print("型態轉換錯誤：請務必輸入整數！")
    except ZeroDivisionError:
        print("運算錯誤：除數不能為 0！")

calculate_ratio()
```

### 範例 3：合併處理多個例外並取得例外物件 (`as e`)

若多種例外的處理邏輯相同，可用元組 `(ExceptionA, ExceptionB)` 包裝，並使用 `as e` 查看系統給出的具體錯誤訊息。

```python
try:
    my_list = [1, 2, 3]
    index = int("abc")  # 會觸發 ValueError
    print(my_list[index])
except (ValueError, IndexError) as err:
    print(f"操作失敗，錯誤類型：{type(err).__name__}")
    print(f"詳細錯誤訊息：{err}")
```

---

## 4. 完整結構：try ... except ... else ... finally

Python 提供了四位一體的完整結構：
- **`try`**：執行測試代碼。
- **`except`**：發生特定例外時執行。
- **`else`**：**沒有發生任何例外時**才會執行。
- **`finally`**：**無論成功或失敗都保證會執行**（常搭配資源清理、關閉連線等）。

### 範例 4：安全處理檔案與清理資源

```python
file = None
try:
    print("1. 嘗試打開檔案...")
    file = open("sample.txt", "r", encoding="utf-8")
    content = file.read()
except FileNotFoundError:
    print("2. 找不到指定檔案！")
else:
    print("2. 成功讀取檔案！內容長度：", len(content))
finally:
    print("3. 執行 finally 清理區塊")
    if file and not file.closed:
        file.close()
        print("檔案已安全關閉。")
```

---

## 5. 主動引發例外：raise

除了被動捕捉系統錯誤，我們也可以在商務邏輯不符合預期時，主動「引發（raise）」例外。

### 範例 5：檢查輸入參數是否合法

```python
def set_age(age: int):
    if not isinstance(age, int):
        raise TypeError("年齡必須是整數！")
    if age < 0 or age > 150:
        raise ValueError(f"不合理的年齡值：{age}，必須介於 0 ~ 150 之間。")
    
    print(f"年齡設定成功：{age} 歲")

try:
    set_age(-5)
except ValueError as e:
    print(f"設定失敗：{e}")
```

### 範例 6：重新拋出例外（Re-raising）

在 `except` 內記錄 log 或做局部處理後，可單獨呼叫 `raise` 將例外往上層拋出：

```python
def process_data(data):
    try:
        return data["key"]
    except KeyError:
        print("[Log] 找不到 key，正在記錄日誌...")
        raise  # 重新拋出 KeyError，讓呼叫這支函式的人決定如何處理
```

---

## 6. 自訂例外（Custom Exceptions）

當內建的例外類型無法精確描述領域問題時，我們可以透過繼承 `Exception` 類別來建立自訂例外。

### 範例 7：銀行帳戶提款系統

```python
# 1. 建立基底自訂例外
class BankError(Exception):
    """所有銀行相關例外的基礎類別"""
    pass

# 2. 建立具體例外類別
class InsufficientFundsError(BankError):
    """餘額不足例外"""
    def __init__(self, balance: float, amount: float):
        self.balance = balance
        self.amount = amount
        super().__init__(f"提款失敗：餘額不足！當前餘額 ${balance}，嘗試提款 ${amount}")

# 3. 在業務邏輯中使用
class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"提款成功！提款：${amount}，剩餘餘額：${self.balance}")

# 4. 測試自訂例外
account = BankAccount(balance=1000)

try:
    account.withdraw(500)   # 成功
    account.withdraw(1200)  # 觸發自訂例外
except InsufficientFundsError as err:
    print(f"業務錯誤攔截 -> {err}")
    print(f"不足金額為：${err.amount - err.balance}")
```

---

## 7. 進階技巧：例外鏈（Exception Chaining）

在捕獲低層級例外時，可能想包裝成高層級業務例外並往外拋，同時保留原本例外的呼叫堆疊（Traceback）。使用 `raise ... from ...` 即可達成。

### 範例 8：使用 from 保留根本原因

```python
class DatabaseConnectionError(Exception):
    pass

def query_user():
    try:
        # 模擬網路或檔案失敗
        open("db_config.ini")
    except FileNotFoundError as origin_err:
        # 將 FileNotFoundError 轉換成更高階的 DatabaseConnectionError
        raise DatabaseConnectionError("無法連接至資料庫設定") from origin_err

try:
    query_user()
except DatabaseConnectionError as e:
    print(f"主錯誤：{e}")
    print(f"原始根本原因：{e.__cause__}")
```

---

## 8. Python 風格：EAFP vs LBYL

- **LBYL（Look Before You Leap）**：三思而後行，在操作前先做大量 `if` 檢查。
- **EAFP（Easier to Ask for Forgiveness than Permission）**：先斬後奏，大膽嘗試，出錯再來道歉（處理例外）。這是 Python 推薦的核心哲學！

### 對比示範：讀取字典中的鍵值

```python
data = {"name": "Alice"}

# 方式 A：LBYL 風格 (非慣用)
if "age" in data:
    age = data["age"]
else:
    age = 18

# 方式 B：EAFP 風格 (Pythonic 慣用例外)
try:
    age = data["age"]
except KeyError:
    age = 18

# 註：此處也可用字典的內建方法 data.get("age", 18)
```

---

## 9. 最佳實踐與常見地雷

1. **避免裸奔的 `except:`**
   ```python
   # ❌ 不良寫法：會連帶捕捉 SystemExit、KeyboardInterrupt (Ctrl+C)
   try:
       do_something()
   except:
       pass

   # ✅ 良好寫法：明確指定例外型態，若需要捕獲所有常規例外，使用 Exception
   try:
       do_something()
   except Exception as e:
       print(f"發生未預期錯誤：{e}")
   ```

2. **保持 `try` 區塊盡可能小**
   - 只把可能出錯的關鍵行放進 `try` 區塊，不要整段幾十行全包進去，否則容易掩蓋不相干的 bug。

3. **別讓例外「默默消失」（Silent Failure）**
   - 避免使用 `except Exception: pass`。至少記錄 log 或印出訊息，避免未來除錯困難。

4. **善用 Context Manager（`with` 陳述句）**
   - 對於檔案關閉、鎖（Lock）釋放等資源操作，推薦使用 `with` 取代手動 `finally`：
   ```python
   with open("sample.txt", "r", encoding="utf-8") as f:
       content = f.read()
   # 區塊結束後自動關閉檔案，即使中途報錯也不會洩漏資源
   ```

---

## UV 環境中執行範例

本專案使用 `uv` 虛擬環境，若將上述範例寫入 `.py` 檔案執行，請使用以下指令：

```bash
uv run python your_script.py
```
