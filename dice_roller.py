"""擲骰子程式 (Dice Roller)
僅以數字呈現結果，不包含任何圖形介面或 ASCII 繪圖。
"""

import random


def roll_dice(count: int = 1, sides: int = 6) -> list[int]:
    """擲骰子並回傳點數串列。

    :param count: 擲骰子的數量（預設為 1）
    :param sides: 骰子的面數（預設為 6）
    :return: 包含每次擲出點數的串列
    """
    if count < 1:
        raise ValueError("骰子數量至少需要 1 顆")
    if sides < 2:
        raise ValueError("骰子面數至少需要 2 面")

    return [random.randint(1, sides) for _ in range(count)]


def main() -> None:
    print("=== 簡易擲骰子程式（純數字呈現）===")
    print("操作說明：按 Enter 鍵擲骰子，輸入 'q' 離開程式。\n")

    while True:
        user_input = input("請輸入擲骰顆數 (直接按 Enter 預設為 1 顆，輸入 q 離開): ").strip()

        if user_input.lower() == "q":
            print("程式結束，謝謝使用！")
            break

        # 判斷輸入顆數
        if user_input == "":
            num_dice = 1
        else:
            try:
                num_dice = int(user_input)
                if num_dice <= 0:
                    print("請輸入大於 0 的正整數！\n")
                    continue
            except ValueError:
                print("輸入無效，請輸入正整數或 'q'！\n")
                continue

        # 擲骰子並呈現數字結果
        results = roll_dice(count=num_dice)

        if num_dice == 1:
            print(f"擲出點數: {results[0]}\n")
        else:
            print(f"各顆點數: {results}")
            print(f"點數總和: {sum(results)}\n")


if __name__ == "__main__":
    main()
###123
