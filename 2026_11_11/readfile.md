# Python 檔案操作：一步一步練習

這份練習會帶你使用 Python 建立、讀取和修改文字檔案。請依序操作；每一步都可以在自己的 `.py` 檔案或 Python 編輯器中執行。

## 開始前：認識工作目錄

Python 會依照「目前工作目錄」尋找檔案。最簡單的做法是先把練習程式和文字檔放在同一個資料夾。

你也可以執行下面的程式，看看 Python 目前在哪個資料夾工作：

```python
from pathlib import Path

print(Path.cwd())
```

如果稍後遇到 `FileNotFoundError`，請先確認檔案是否放在這個資料夾，或改用完整檔案路徑。

## 第 1 步：建立一個文字檔

先用 Python 建立 `notes.txt`，並寫入一段文字：

```python
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("你好，Python！\n")
    file.write("這是我的第一個文字檔。\n")
```

執行後，確認工作目錄裡出現 `notes.txt`，再用文字編輯器打開看看。

- `open(...)`：開啟檔案。
- `"w"`：寫入模式；如果檔案已存在，原本內容會被清空再重寫。
- `encoding="utf-8"`：以 UTF-8 編碼處理文字，適合中文。
- `with`：離開區塊時會自動關閉檔案。
- `\n`：換行。

> 小心：`"w"` 會覆蓋舊內容。練習時請使用自己的測試檔，例如 `notes.txt`，不要直接對重要檔案使用。

## 第 2 步：讀取整個檔案

接著把剛才寫入的內容讀出來：

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

`"r"` 代表讀取模式，`read()` 會一次讀取整個檔案。

**練習：**把第 1 步的第二行改成你自己的句子，再執行讀取程式，確認畫面顯示新內容。

## 第 3 步：逐行讀取

如果檔案很大，逐行處理通常比一次讀完整個檔案更合適：

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")
```

讀取到的每一行通常已經包含換行符號，所以這裡用 `end=""` 避免多出空白行。

也可以用 `readline()` 一次讀一行：

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    second_line = file.readline()

print("第一行：", first_line, end="")
print("第二行：", second_line, end="")
```

**練習：**在 `notes.txt` 加上第三行，修改程式讀取並印出第三行。

## 第 4 步：追加內容，不覆蓋原內容

想在檔案最後增加一行，使用 `"a"`（append，追加）模式：

```python
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("這一行是後來追加的。\n")
```

再用第 2 步的程式讀取檔案，確認舊內容還在，而且新的一行出現在最後。

常見的檔案模式：

| 模式 | 用途 | 檔案不存在時 |
|---|---|---|
| `"r"` | 讀取 | 會發生 `FileNotFoundError` |
| `"w"` | 寫入並覆蓋舊內容 | 建立新檔案 |
| `"a"` | 在檔案末尾追加 | 建立新檔案 |
| `"x"` | 建立新檔案，不覆蓋既有檔案 | 建立新檔案；若已存在會發生錯誤 |

## 第 5 步：用 `pathlib` 組合檔案路徑

`pathlib` 可以用較清楚的方式處理檔案路徑，也能直接讀寫文字：

```python
from pathlib import Path

file_path = Path("notes.txt")

text = file_path.read_text(encoding="utf-8")
print(text)
```

也可以建立資料夾路徑，再把檔案放進去：

```python
from pathlib import Path

folder = Path("practice_files")
folder.mkdir(exist_ok=True)

file_path = folder / "hello.txt"
file_path.write_text("檔案放在資料夾裡。\n", encoding="utf-8")

print(file_path.read_text(encoding="utf-8"))
```

`folder / "hello.txt"` 會依照作業系統組合路徑，不需要自己猜斜線方向。

## 第 6 步：處理檔案不存在的情況

讀取不存在的檔案會產生 `FileNotFoundError`。可以用 `try` / `except` 顯示清楚的訊息：

```python
from pathlib import Path

file_path = Path("missing.txt")

try:
    text = file_path.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"找不到檔案：{file_path}")
else:
    print(text)
```

**練習：**把 `missing.txt` 改成 `notes.txt`，並分別測試檔案存在和不存在時會發生什麼事。

## 小挑戰：統計文字檔的行數與字數

建立 `story.txt`，放入幾行文字，再完成程式，印出檔案的總行數和總字數：

```python
from pathlib import Path

file_path = Path("story.txt")
text = file_path.read_text(encoding="utf-8")

lines = text.splitlines()
print("行數：", len(lines))
print("字數（含空白與換行）：", len(text))
```

試著回答：

1. `splitlines()` 得到的是什麼？
2. 如果檔案是空的，行數和字數各是多少？
3. 把檔案換成 `notes.txt`，輸出會有什麼不同？

## 完成檢查

- [ ] 我知道怎麼用 `open()` 開啟檔案。
- [ ] 我能說出 `"r"`、`"w"` 和 `"a"` 的差別。
- [ ] 我會用 `with` 和 `encoding="utf-8"`。
- [ ] 我能一次讀完整個檔案，也能逐行讀取。
- [ ] 我知道 `"w"` 會覆蓋原有內容。
- [ ] 我能用 `Path` 檢查或組合檔案路徑。
