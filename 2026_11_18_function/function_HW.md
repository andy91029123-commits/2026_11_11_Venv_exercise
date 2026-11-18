# Python 函式呼叫與進階參數規範教學講義 (Function Call & Argument Specifications)

> **導覽 / Navigation / ナビゲーション**：
> - [繁體中文 (Traditional Chinese)](#-繁體中文版-traditional-chinese)
> - [English](#-english-version)
> - [日本語 (Japanese)](#-日本語版-japanese)

---

# 🇹🇼 繁體中文版 (Traditional Chinese)

## 簡介與環境準備

本講義專門針對 Python 函式（Function）的呼叫方式與進階參數限制語法進行深度解析。你將學會如何精確掌握「位置引數」、「關鍵字引數」、預設參數，以及 Python 3.8+ 引入的特殊控制符號 `/`（僅限位置引數）與 `*`（僅限關鍵字引數）。

### 準備環境
請於終端機確認使用 Python 3.12+ 虛擬環境：
```powershell
# 確認 Python 版本
python --version
```

---

## 前置觀念：參數（Parameter）與引數（Argument）

在深入語法前，務必釐清兩者的核心差別：
- **參數（Parameter）**：**定義函式時**，寫在 `def 函式名稱(...)` 括號內的變數名稱（相當於空白表格上的欄位名稱）。
- **引數（Argument）**：**呼叫函式時**，實際傳入括號內的真實資料值（填入表格的實際內容）。

```python
# 定義函式時，name 是「參數」(Parameter)
def greet(name):
    print(f"哈囉，{name}！")

# 呼叫函式時，"小明" 是「引數」(Argument)
greet("小明")
```

---

## 步驟分解教學

### 第 1 步：依「引數位置」呼叫（Positional Arguments）

最直覺的呼叫方式，直接將值放入括號內。Python 會依據傳入的**前後順序**，由左至右依序對應到定義的參數：

```python
def describe_pet(animal, name):
    print(f"我養了一隻{animal}，牠叫做{name}。")

describe_pet("貓", "小橘")   # 輸出：我養了一隻貓，牠叫做小橘。
describe_pet("小橘", "貓")   # 位置對調：我養了一隻小橘，牠叫做貓。
```
- 引數順序若顛倒，邏輯結果就會錯誤。
- 少傳或多傳引數時，會引發 `TypeError`。

---

### 第 2 步：依「引數名稱」呼叫（Keyword Arguments）

當參數較多、順序難記時，可直接以 **`參數名稱=值`** 的形式傳遞：

```python
def describe_pet(animal, name):
    print(f"我養了一隻{animal}，牠叫做{name}。")

describe_pet(animal="貓", name="小橘")
describe_pet(name="小橘", animal="貓")  # 順序對調完全不影響結果！
```

#### 重要規則：混用時「位置引數」必須在「關鍵字引數」前面
```python
# 正確：位置引數在前面，關鍵字引數在後
describe_pet("狗", name="旺財")

# 錯誤：位置引數不能在關鍵字引數之後，會觸發 SyntaxError
# describe_pet(animal="狗", "旺財")
```

---

### 第 3 步：設定預設參數值（Default Arguments）

常態使用的參數可賦予預設值，呼叫時可省略傳入：

```python
def order_drink(drink, ice="正常冰", sugar="半糖"):
    print(f"點餐：{drink}（{ice} / {sugar}）")

order_drink("紅茶")                          # 全部使用預設：正常冰 / 半糖
order_drink("紅茶", "去冰")                  # 覆蓋 ice
order_drink("紅茶", sugar="無糖")            # 透過關鍵字跳過 ice，直接修改 sugar
order_drink("綠茶", sugar="微糖", ice="少冰") # 關鍵字順序可自由調換
```
> **語法鐵則**：定義函式時，無預設值的參數（如 `drink`）必須排在有預設值的參數（如 `ice`, `sugar`）前面。

---

### 第 4 步：特殊限制符號 `/` —— 僅限位置引數（Positional-Only）

寫在符號 `/` **左邊**的所有參數，在呼叫時**強制只能用位置傳入**，嚴禁指名參數名稱：

```python
def calc_bmi(weight, height, /):
    bmi = weight / (height ** 2)
    print(f"BMI 為：{bmi:.1f}")

calc_bmi(65, 1.75)  # 正確：依位置傳入

# 錯誤：若寫出參數名稱會引發 TypeError
# calc_bmi(weight=65, height=1.75)
```
- **設計目的**：避免呼叫端將內部參數名稱寫死，未來即便重構改名也不會破壞外部呼叫。

---

### 第 5 步：特殊限制符號 `*` —— 僅限關鍵字引數（Keyword-Only）

寫在單獨符號 `*` **右邊**的所有參數，呼叫時**強制必須寫出參數名稱**，不可依位置傳遞：

```python
def send_email(to, *, subject, urgent=False):
    print(f"寄給：{to}｜主旨：{subject}｜急件：{urgent}")

send_email("student@example.com", subject="課堂通知", urgent=True)  # 正確
send_email("student@example.com", subject="作業提醒")               # 正確（urgent 採預設）

# 錯誤：subject 與 urgent 在 * 右邊，不能用位置傳遞
# send_email("student@example.com", "課堂通知", True)
```
- **設計目的**：提高布林值開關（如 `urgent=True`）或關鍵選項的程式碼可讀性，防止傳錯位置。

---

### 第 6 步：`/` 與 `*` 綜合切分規則

結合兩者，函式參數可明確劃分為三個區域：
```text
def 函式名稱( [僅限位置引數] , / , [位置或關鍵字皆可] , * , [僅限關鍵字引數] ):
```

```python
def register(id_no, /, name, *, role="student"):
    print(f"編號：{id_no}｜姓名：{name}｜身分：{role}")

# 合法呼叫
register("A01", "小明", role="leader")
register("A01", name="小明", role="leader")
register("A01", "小明")

# 非法呼叫（觸發 TypeError）
# register(id_no="A01", name="小明")  # 錯誤：id_no 不能寫名稱
# register("A01", "小明", "leader")   # 錯誤：role 必須寫名稱
```

---

## 實作練習題

請先獨立思考練習，完成後再參考提示：

1. **咖啡點餐函式**：
   已有定義 `def make_coffee(beans, milk="全脂鮮奶", sugar=0):`
   - 請以純**位置引數**點一杯 `"曼巴"`、`"燕麥奶"`、糖度 `2`。
   - 請以**位置引數 + 關鍵字引數**混用方式，保留預設牛奶，僅修改糖度為 `1`。
2. **語法錯誤除錯題**：
   請判斷下方定義的函式中，哪幾次呼叫會產生錯誤？該如何更正？
   ```python
   def create_ticket(event, /, seat, *, price, vip=False):
       print(event, seat, price, vip)

   # 呼叫 A
   create_ticket("演唱會", "A區", price=2000)
   # 呼叫 B
   create_ticket(event="演唱會", seat="A區", price=2000)
   # 呼叫 C
   create_ticket("演唱會", "A區", 2000, True)
   ```
3. **資料處理函式設計（延伸實戰作業）**：
   請設計一個具備擴充性與可讀性的資料統計運算函式 `process_scores(data, /, metric="avg", *, round_digits=2)`：
   - `data` 必須僅限位置傳入（數字串列）。
   - `metric` 可用位置或關鍵字傳入，可選 `"avg"`（平均）或 `"sum"`（總和）。
   - `round_digits` 僅限關鍵字傳入，指定四捨五入小數位數。

### 練習提示：
```python
# 第 1 題：make_coffee("曼巴", "燕麥奶", 2) 以及 make_coffee("曼巴", sugar=1)
# 第 2 題：呼叫 B 錯誤（event 禁寫名稱）；呼叫 C 錯誤（price 與 vip 禁依位置傳入）
# 第 3 題：def process_scores(data, /, metric="avg", *, round_digits=2):
#             if metric == "avg": val = sum(data) / len(data)
#             else: val = sum(data)
#             return round(val, round_digits)
```

---

## 常見問題 (FAQ)

- **Q1: 為什麼呼叫函式時出現 `SyntaxError: positional argument follows keyword argument`？**
  - **解析**：你在關鍵字引數後面又寫了位置引數。Python 規定位置引數必須全部排在最前面。
- **Q2: 出現 `TypeError: ... got some positional-only arguments passed as keyword arguments`？**
  - **解析**：表示該參數位於 `/` 左側，受限為僅限位置傳遞，請移除呼叫時的 `參數名=`。
- **Q3: 出現 `TypeError: ... takes 1 positional argument but 3 were given`？**
  - **解析**：參數位於 `*` 右側，受限為僅限關鍵字傳遞，請為該引數明確加上 `參數名=`。

---

## 完成檢查 (Checklist)

- [ ] 能清楚區分參數（Parameter）與引數（Argument）的定義。
- [ ] 能正確使用位置引數、關鍵字引數，並嚴格遵循混用時位置在前的原則。
- [ ] 能在函式定義中設定合理的預設參數值。
- [ ] 能理解並運用 `/` 定義僅限位置引數。
- [ ] 能理解並運用 `*` 定義僅限關鍵字引數。
- [ ] 能設計出結合 `/` 與 `*` 的三段式安全參數架構。

---

# 🇺🇸 English Version

## Introduction & Environment Setup

This tutorial provides a comprehensive guide to Python function call mechanisms and advanced argument specification syntax. You will master positional arguments, keyword arguments, default parameters, and the special delimiters `/` (positional-only) and `*` (keyword-only) introduced in modern Python (3.8+).

### Environment Setup
Verify your Python environment in your terminal (Python 3.12+ recommended):
```powershell
python --version
```

---

## Prerequisites: Parameters vs. Arguments

Before exploring syntax rules, clarify the fundamental distinction:
- **Parameter**: The variable name listed inside the function parentheses in the **function definition** (`def func(...)`).
- **Argument**: The real value or expression passed into the function when **calling** it.

```python
# 'name' is a Parameter
def greet(name):
    print(f"Hello, {name}!")

# "Alice" is an Argument
greet("Alice")
```

---

## Step-by-Step Breakdown

### Step 1: Calling by Positional Arguments

The most common way to call functions is by supplying values in order. Python maps each argument from left to right:

```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet("cat", "Rusty")  # I have a cat named Rusty.
describe_pet("Rusty", "cat")  # Swapped: I have a Rusty named cat.
```
- Positional ordering dictates correctness.
- Missing or extra arguments raise `TypeError`.

---

### Step 2: Calling by Keyword Arguments

When there are multiple parameters, use **`name=value`** syntax to specify arguments explicitly:

```python
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet(animal="cat", name="Rusty")
describe_pet(name="Rusty", animal="cat")  # Order does not matter!
```

#### Important Rule: Positional arguments MUST precede Keyword arguments
```python
# Valid: Positional first, then keyword
describe_pet("dog", name="Buddy")

# Invalid: Raises SyntaxError
# describe_pet(animal="dog", "Buddy")
```

---

### Step 3: Default Arguments

Provide fallback values for commonly used parameters:

```python
def order_drink(drink, ice="Regular", sugar="Half"):
    print(f"Order: {drink} ({ice} / {sugar})")

order_drink("Black Tea")                           # Uses defaults
order_drink("Black Tea", "No Ice")                 # Overrides ice
order_drink("Black Tea", sugar="Zero")             # Skips ice, overrides sugar
order_drink("Green Tea", sugar="Zero", ice="Less") # Free order
```
> **Rule**: In definitions, parameters without default values must be placed before parameters with default values.

---

### Step 4: Special Delimiter `/` (Positional-Only Parameters)

Parameters defined to the **left** of `/` can **only** be passed positionally. Keyword syntax is strictly prohibited:

```python
def calc_bmi(weight, height, /):
    bmi = weight / (height ** 2)
    print(f"BMI: {bmi:.1f}")

calc_bmi(65, 1.75)  # Valid

# Invalid: Raises TypeError
# calc_bmi(weight=65, height=1.75)
```
- **Purpose**: Enables API authors to rename internal parameters without breaking caller code.

---

### Step 5: Special Delimiter `*` (Keyword-Only Parameters)

Parameters defined to the **right** of a bare `*` **must** be supplied as keyword arguments:

```python
def send_email(to, *, subject, urgent=False):
    print(f"To: {to} | Subject: {subject} | Urgent: {urgent}")

send_email("student@example.com", subject="Notice", urgent=True)  # Valid
send_email("student@example.com", subject="Reminder")             # Valid

# Invalid: Raises TypeError
# send_email("student@example.com", "Notice", True)
```
- **Purpose**: Enforces explicit naming for boolean flags and optional configurations, preventing misplacement bugs.

---

### Step 6: Combining `/` and `*` (Three Parameter Zones)

```text
def func_name( [Positional-Only] , / , [Positional or Keyword] , * , [Keyword-Only] ):
```

```python
def register(id_no, /, name, *, role="student"):
    print(f"ID: {id_no} | Name: {name} | Role: {role}")

# Valid calls
register("A01", "Alice", role="leader")
register("A01", name="Alice", role="leader")
register("A01", "Alice")

# Invalid calls (TypeError)
# register(id_no="A01", name="Alice")  # id_no must be positional
# register("A01", "Alice", "leader")   # role must be keyword
```

---

## Hands-on Exercises

1. **Coffee Order Function**:
   Given `def make_coffee(beans, milk="Whole Milk", sugar=0):`
   - Call it using purely positional arguments: `"Dark Roast"`, `"Oat Milk"`, `2`.
   - Call it by mixing positional and keyword arguments to keep default milk but set sugar to `1`.
2. **Syntax Debugging**:
   Identify which calls fail and explain why:
   ```python
   def create_ticket(event, /, seat, *, price, vip=False):
       print(event, seat, price, vip)

   # Call A
   create_ticket("Concert", "A1", price=2000)
   # Call B
   create_ticket(event="Concert", seat="A1", price=2000)
   # Call C
   create_ticket("Concert", "A1", 2000, True)
   ```
3. **Data Processor Function Design**:
   Implement `process_scores(data, /, metric="avg", *, round_digits=2)`:
   - `data`: positional-only list of numbers.
   - `metric`: positional or keyword (`"avg"` or `"sum"`).
   - `round_digits`: keyword-only integer decimal places.

### Hints:
```python
# Exercise 1: make_coffee("Dark Roast", "Oat Milk", 2) & make_coffee("Dark Roast", sugar=1)
# Exercise 2: Call B fails (event is positional-only); Call C fails (price & vip must be keyword)
```

---

## Frequently Asked Questions (FAQ)

- **Q1: Why do I get `SyntaxError: positional argument follows keyword argument`?**
  - All positional arguments must appear before any keyword arguments in a call.
- **Q2: Why `TypeError: ... got some positional-only arguments passed as keyword arguments`?**
  - You passed a parameter situated to the left of `/` using keyword syntax.
- **Q3: Why `TypeError: ... takes 1 positional argument but 3 were given`?**
  - Arguments to the right of `*` cannot be passed by position; use `name=value`.

---

## Completion Checklist

- [ ] Clear understanding of Parameter vs. Argument.
- [ ] Able to use positional and keyword calls properly.
- [ ] Understand ordering rules when mixing argument types.
- [ ] Understand and apply `/` for positional-only parameters.
- [ ] Understand and apply `*` for keyword-only parameters.
- [ ] Capable of building safe 3-zone function signatures.

---

# 🇯🇵 日本語版 (Japanese)

## はじめに・環境準備

このテキストでは、Python における関数呼び出しの仕組みと、高度な引数の制御構文（位置専用引数 `/` およびキーワード専用引数 `*`）を詳しく学びます。

### 実行環境の確認
ターミナルで Python 3.12+ の仮想環境が有効になっていることを確認してください：
```powershell
python --version
```

---

## 前提知識：仮引数（Parameter）と実引数（Argument）

- **仮引数（Parameter）**：関数の**定義時**に括弧内に記述する変数名（空欄の項目名）。
- **実引数（Argument）**：関数の**呼び出し時**に実際に渡すデータ値（入力された値）。

```python
# 定義側の name は「仮引数 (Parameter)」
def greet(name):
    print(f"こんにちは、{name}さん！")

# 呼び出し側の "太郎" は「実引数 (Argument)」
greet("太郎")
```

---

## ステップ別解説

### ステップ 1：位置による引数渡し（Positional Arguments）

最も標準的な呼び出し方です。引数の並び順に従って、左から右へ順に仮引数へと代入されます：

```python
def describe_pet(animal, name):
    print(f"私は{animal}を飼っています。名前は{name}です。")

describe_pet("猫", "ミケ")   # 私は猫を飼っています。名前はミケです。
describe_pet("ミケ", "猫")   # 順番が逆：私はミケを飼っています。名前は猫です。
```

---

### ステップ 2：キーワードによる引数渡し（Keyword Arguments）

仮引数が多い場合、**`引数名=値`** の形式で指定することで、順番に依存せずに安全に呼び出せます：

```python
def describe_pet(animal, name):
    print(f"私は{animal}を飼っています。名前は{name}です。")

describe_pet(animal="猫", name="ミケ")
describe_pet(name="ミケ", animal="猫")  # 順番を逆にしても正しく動作！
```

#### 重要ルール：混在時は必ず「位置引数」を先に書く
```python
# 正常：位置引数が先、キーワード引数が後
describe_pet("犬", name="ポチ")

# エラー（SyntaxError）：キーワード引数の後に位置引数は置けません
# describe_pet(animal="犬", "ポチ")
```

---

### ステップ 3：デフォルト値の設定（Default Arguments）

よく使われる値に初期値を設定しておくことで、呼び出し時の指定を省略できます：

```python
def order_drink(drink, ice="普通", sugar="半分"):
    print(f"注文：{drink}（氷：{ice} / 砂糖：{sugar}）")

order_drink("紅茶")                          # デフォルト値を使用
order_drink("紅茶", "氷なし")                # ice のみ上書き
order_drink("紅茶", sugar="無糖")            # キーワード指定で ice を飛ばして sugar を変更
```
> **文法規則**：デフォルト値を持たない引数は、デフォルト値を持つ引数よりも前に定義する必要があります。

---

### ステップ 4：特殊記号 `/`（位置専用引数 Positional-Only）

`/` の**左側**に書かれた仮引数は、呼び出し時に**位置引数としてのみ**渡すことができ、キーワード指定（`引数名=`）は禁止されます：

```python
def calc_bmi(weight, height, /):
    bmi = weight / (height ** 2)
    print(f"BMI：{bmi:.1f}")

calc_bmi(65, 1.75)  # 正常

# エラー（TypeError）：キーワード指定は不可
# calc_bmi(weight=65, height=1.75)
```

---

### ステップ 5：特殊記号 `*`（キーワード専用引数 Keyword-Only）

独立した `*` の**右側**に書かれた仮引数は、呼び出し時に**必ずキーワード（`引数名=`）で指定**しなければなりません：

```python
def send_email(to, *, subject, urgent=False):
    print(f"宛先：{to}｜件名：{subject}｜緊急：{urgent}")

send_email("student@example.com", subject="授業案内", urgent=True)  # 正常
send_email("student@example.com", subject="リマインダー")           # 正常（urgent はデフォルト）

# エラー（TypeError）：位置指定は不可
# send_email("student@example.com", "授業案内", True)
```

---

### ステップ 6：`/` と `*` を組み合わせた 3 つの引数領域

```text
def 関数名( [位置専用] , / , [位置・キーワード両用] , * , [キーワード専用] ):
```

```python
def register(id_no, /, name, *, role="student"):
    print(f"ID：{id_no}｜氏名：{name}｜権限：{role}")

# 有効な呼び出し
register("A01", "太郎", role="leader")
register("A01", name="太郎", role="leader")
register("A01", "太郎")

# 無効な呼び出し（TypeError）
# register(id_no="A01", name="太郎")  # id_no はキーワード指定不可
# register("A01", "太郎", "leader")   # role は位置指定不可
```

---

## 演習問題

1. **カフェ注文関数**：
   定義：`def make_coffee(beans, milk="普通牛乳", sugar=0):`
   - 全て位置引数で「`"深煎り"`」「`"オーツミルク"`」「`2`」を指定して呼び出してください。
   - 牛乳はデフォルトのまま、砂糖のみ「`1`」に変更して混在形式で呼び出してください。
2. **デバッグ問題**：
   次のうち、エラーになる呼び出しはどれですか？
   ```python
   def create_ticket(event, /, seat, *, price, vip=False):
       print(event, seat, price, vip)

   # 呼び出し A
   create_ticket("コンサート", "S席", price=2000)
   # 呼び出し B
   create_ticket(event="コンサート", seat="S席", price=2000)
   # 呼び出し C
   create_ticket("コンサート", "S席", 2000, True)
   ```
3. **データ集計関数の設計**：
   `process_scores(data, /, metric="avg", *, round_digits=2)` を実装し、各引数の呼び出し制限の挙動を確認してください。

---

## よくある質問 (FAQ)

- **Q1: `SyntaxError: positional argument follows keyword argument` の原因は？**
  - キーワード引数の後ろに位置引数を記述しています。必ず位置引数を先頭に配置してください。
- **Q2: `TypeError: ... got some positional-only arguments passed as keyword arguments`？**
  - `/` より左側にある引数に `引数名=` を付けて呼び出しています。位置引数として渡してください。
- **Q3: `TypeError: ... takes 1 positional argument but 3 were given`？**
  - `*` より右側のキーワード専用引数を位置引数で渡そうとしています。必ず `引数名=` を指定してください。

---

## 修了チェックリスト

- [ ] 仮引数（Parameter）と実引数（Argument）の違いを説明できる。
- [ ] 位置引数とキーワード引数の正しい組み合わせ順序を理解している。
- [ ] デフォルト引数の文法ルールを理解している。
- [ ] `/` による「位置専用引数」の定義と制約を説明できる。
- [ ] `*` による「キーワード専用引数」の定義と制約を説明できる。
- [ ] `/` と `*` を適切に使い分けた安全な関数を設計できる。
