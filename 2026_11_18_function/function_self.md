# Python 函式（Function）：一步一步練習

這份教材會帶你從零開始學習 Python 函式（Function）的核心觀念與用法，包含定義函式、傳遞參數、接收回傳值、設定預設值、理解變數作用域（Scope），以及使用彈性參數（`*args` 與 `**kwargs`）。請先準備好 Python 環境，並在終端機中跟著範例動手練習。

## 準備環境

你可以在 VS Code 開啟終端機，確認目前位置是專案根目錄，再輸入：

```bash
python --version
```

若你的環境使用 `python3`，請把下方指令中的 `python` 改成 `python3`。

你可以直接在終端機執行同目錄下的練習程式：

```bash
python function_self/function_self.py
```

---

## 第 1 步：定義與呼叫基本函式

函式就像是一台「機器」或一個「任務清單」，把重複要用的程式碼包裝起來，需要時只要呼叫名稱即可執行。

使用 `def` 關鍵字來定義函式，名稱後面加上小括號 `()` 與冒號 `:`，內容必須縮排：

```python
def say_hello():
    print("哈囉！歡迎學習 Python 函式。")
    print("函式能幫你把程式碼模組化、重複使用。")

# 呼叫函式
say_hello()
say_hello()
```

- `def` 是 define（定義）的縮寫。
- `say_hello` 是函式的名稱，命名規則與變數相同（建議使用小寫字母與底線）。
- 括號 `()` 代表參數清單（目前括號內沒有填入任何東西，代表不需要輸入）。
- 定義函式時，裡面的程式碼**不會立刻執行**；只有當你寫出 `say_hello()`（加上括號呼叫）時才會真正執行。

---

## 第 2 步：傳遞參數與引數

如果希望函式能處理不同的資料，可以在括號內設定「參數」（Parameters），呼叫時再傳入具體的「引數」（Arguments）：

```python
def greet_user(name, greeting):
    print(f"{greeting}，{name}！")

# 1. 位置引數（依順序對應）
greet_user("小明", "早安")
greet_user("小美", "晚安")

# 2. 關鍵字引數（指定參數名稱，順序可調換）
greet_user(greeting="你好", name="阿強")
```

- `name` 和 `greeting` 是函式定義時的**參數（Parameters）**。
- `"小明"` 和 `"早安"` 是呼叫時實際給予的**引數（Arguments）**。
- **位置引數（Positional Arguments）**：依照位置由左至右依序代入。
- **關鍵字引數（Keyword Arguments）**：呼叫時清楚指名 `參數名=值`，即使順序調換也能正確對應。
- 提醒：如果混用位置引數與關鍵字引數，**位置引數必須放在前面**，否則 Python 會報錯。

---

## 第 3 步：回傳值（return 的重要性）

很多初學者容易混淆 `print()` 與 `return`：
- `print()` 只是把文字「印在螢幕上看」，程式無法把印出來的結果拿去做其他計算。
- `return` 是把計算結果「交還給呼叫者」，可以存入變數、繼續傳給別的函式使用。

```python
def add(a, b):
    result = a + b
    return result

# 接收回傳值並存入變數
total = add(15, 25)
print(f"相加的結果是：{total}")

# 可以進一步拿回傳值運算
double_total = total * 2
print(f"結果的兩倍是：{double_total}")
```

### 回傳多個值

Python 函式可以使用逗號同時回傳多個數值，這時 Python 會自動把它們打包成元組（Tuple），也可以用多個變數進行解包（Unpack）：

```python
def get_min_and_max(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    return lowest, highest

scores = [85, 92, 58, 77, 99]
min_score, max_score = get_min_and_max(scores)

print(f"最低分：{min_score}，最高分：{max_score}")
```

- 如果函式執行結束都沒有碰到 `return`，或者只寫 `return` 後面沒有值，Python 預設會回傳 `None`。
- `return` 也代表函式結束，函式內一旦執行到 `return`，後續的程式碼就不會再被執行。

---

## 第 4 步：設定預設參數值（Default Arguments）

有時候某些參數大部分情況都有固定的慣用值，我們可以給它設定預設值。呼叫時如果沒有提供該引數，就會自動使用預設值：

```python
def power(base, exponent=2):
    return base ** exponent

# 使用預設次方（平方）
print(power(5))      # 5 ** 2 = 25

# 自行指定次方
print(power(5, 3))   # 5 ** 3 = 125
print(power(2, exponent=4))  # 2 ** 4 = 16
```

### 重要語法規則與避坑指南

1. **預設參數必須放在無預設參數的後面**：
   ```python
   # 正確
   def introduce(name, title="工程師"): ...

   # 錯誤！會產生 SyntaxError
   def introduce(title="工程師", name): ...
   ```
2. **切勿使用可變物件（如空串列 `[]`、空字典 `{}`）作為預設值**：
   可變物件預設值會在記憶體中持續累積。正確寫法是使用 `None`：
   ```python
   # 建議的安全寫法
   def add_item(item, item_list=None):
       if item_list is None:
           item_list = []
       item_list.append(item)
       return item_list
   ```

---

## 第 5 步：變數作用域（全域 vs. 區域）

變數在不同的位置被定義，會有不同的有效存取範圍（Scope）：
- **區域變數（Local Variable）**：在函式內部建立的變數，只在函式執行期間存在，外部無法讀取。
- **全域變數（Global Variable）**：在函式外部（模組最頂層）建立的變數，整個檔案都可以看見。

```python
school_name = "Python 學院"  # 全域變數

def show_student_info(name):
    student_id = "S1001"    # 區域變數
    # 函式內部可以讀取全域變數
    print(f"學校：{school_name} | 姓名：{name} | 學號：{student_id}")

show_student_info("小華")

# 嘗試在函式外部存取區域變數會引發 NameError
# print(student_id)  # 這行會報錯！
```

### 修改全域變數

如果真的需要在函式內部修改外部的全域變數，必須加上 `global` 宣告；但**良好的程式設計原則建議透過「傳入參數」與「回傳新值」**來傳遞資料，避免濫用 `global` 造成程式難以除錯與追蹤。

---

## 第 6 步：彈性參數（*args 與 **kwargs）與 Docstring

有時候無法預先確定呼叫者會傳入幾個引數，這時可以使用 `*args` 與 `**kwargs`：

```python
def make_order(table_num, *dishes, **details):
    """
    記錄餐廳點餐資訊。
    
    :param table_num: 桌號
    :param dishes: 不定數量的餐點名稱（打包成 tuple）
    :param details: 不定數量的備註資訊（打包成 dict）
    """
    print(f"=== 桌號 {table_num} 的點餐 ===")
    print(f"餐點項目：{dishes}")
    print(f"特殊備註：{details}")

# 呼叫範例
make_order(5, "牛肉麵", "燙青菜", "滷蛋", spicy="少辣", soup="多湯")
```

- `*dishes`（常用名稱為 `*args`）：會把傳入的多個位置引數打包成一個 **Tuple（元組）**。
- `**details`（常用名稱為 `**kwargs`）：會把多個 `鍵=值` 的關鍵字引數打包成一個 **Dict（字典）**。
- 緊跟在函式名稱下方用三引號 `"""..."""` 撰寫的文字稱為 **Docstring（文件字串）**，能為函式提供說明。你可以用 `help(make_order)` 查詢函式說明。

---

## 練習題

請先嘗試自己寫寫看，再參考後方的提示：

1. **溫度轉換函式**：撰寫 `celsius_to_fahrenheit(c)`，接收攝氏溫度，換算成華氏溫度後回傳（公式：$F = C \times \frac{9}{5} + 32$）。
2. **統計計算函式**：撰寫 `calculate_stats(numbers)`，傳入一個整數串列，同時回傳這組數字的「總和」、「平均值」、「最大值」與「最小值」。
3. **個人檔案產生器**：撰寫 `create_profile(name, age, city="台北")`，回傳一個整理好的字典或格式化字串。若未指定居住城市，預設顯示「台北」。
4. **不定量數值加總**：撰寫 `sum_all(*numbers)`，利用可變參數接受任意個數的數值，回傳加總總和。若呼叫 `sum_all()` 沒有傳入任何數值，請回傳 `0`。

提示：

```python
# 練習 1：記得使用 return，例如 return c * 9 / 5 + 32
# 練習 2：sum(numbers)、len(numbers)、max(numbers)、min(numbers)，return 逗號隔開
# 練習 3：善用字串 f-string 或字典回傳 {"name": name, "age": age, "city": city}
# 練習 4：numbers 會是一個 tuple，可以用 sum(numbers) 或用 for 迴圈累加
```

---

## 常見問題

- **為什麼要用 `return` 而不直接用 `print`？**
  `print` 只能將資訊顯示在終端機供人類閱讀，程式其他部分無法重複利用輸出。`return` 能讓函式成為積木，隨意被其他程式呼叫、計算與轉傳。
- **出現 `SyntaxError: non-default argument follows default argument` 是什麼意思？**
  這代表你把沒有預設值的參數排在有預設值的參數後面了。請調整參數順序，把所有沒有預設值的參數排在前面。
- **出現 `UnboundLocalError: local variable referenced before assignment`？**
  通常是因為你在函式內嘗試修改一個全域變數，但沒有宣告 `global`，Python 誤以為你在該行重新賦值區域變數，導致讀取早於賦值而引發錯誤。建議把變數改用參數傳入並用 `return` 回傳更新。
- **預設參數為什麼不要用 `items=[]`？**
  因為 Python 只會在定義函式時建立一次預設物件，如果不小心傳入了空串列預設值，多次呼叫時所有操作會共用同一個串列物件，導致資料相互污染。建議用 `items=None`。

---

## 完成檢查

- [ ] 能使用 `def` 與縮排正確定義並呼叫無參數函式。
- [ ] 能清楚區分「位置引數」與「關鍵字引數」的傳遞方式。
- [ ] 能理解 `print()` 與 `return` 的差別，並能回傳單一值或多個值。
- [ ] 能為參數設定預設值，並知道預設參數的順序規則。
- [ ] 能區分區域變數與全域變數的生命週期與存取權限。
- [ ] 能理解 `*args`（打包成元組）與 `**kwargs`（打包成字典）的使用場景。
