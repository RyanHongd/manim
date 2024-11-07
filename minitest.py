def needs_borrowing_vertical(minuend, subtrahend):
    minuend_str = str(minuend)
    subtrahend_str = str(subtrahend)

    # 確保 minuend 和 subtrahend 的位數相同，方便逐位比較
    max_length = max(len(minuend_str), len(subtrahend_str))
    minuend_str = minuend_str.zfill(max_length)
    subtrahend_str = subtrahend_str.zfill(max_length)

    # 將 minuend 轉為數字列表
    minuend_list = [int(digit) for digit in minuend_str]
    subtrahend_list = [int(digit) for digit in subtrahend_str]

    # 顯示原始的直式減法
    print("原始直式減法：")
    print(" " * 3 + ''.join(map(str, minuend_list)))
    print("- " + ''.join(map(str, subtrahend_list)))
    print("------")

    # 執行逐位減法並顯示借位過程
    for i in range(max_length - 1, -1, -1):
        m_digit = minuend_list[i]
        s_digit = subtrahend_list[i]

        if m_digit < s_digit:
            # 若需要借位
            borrow_pos = i - 1
            while borrow_pos >= 0 and minuend_list[borrow_pos] == 0:
                minuend_list[borrow_pos] = 9
                borrow_pos -= 1
            if borrow_pos >= 0:
                minuend_list[borrow_pos] -= 1
                minuend_list[i] += 10

            # 顯示當前的借位結果
            print("借位後的直式減法：")
            print(" " * 3 + ''.join(map(str, minuend_list)))
            print("- " + ''.join(map(str, subtrahend_list)))
            print("------")

    # 最後的減法結果
    result = int("".join(map(str, minuend_list))) - int("".join(map(str, subtrahend_list)))
    print("最終結果：")
    print(" " * 3 + str(result))

# 以 100 - 25 為例
needs_borrowing_vertical(100, 25)







