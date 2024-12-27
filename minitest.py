import tkinter as tk

# 創建主視窗
root = tk.Tk()
root.title("更改顏色範例")
root.geometry("300x200")

# 創建標籤並更改文字和背景顏色
label = tk.Label(root, text="這是一個標籤", fg="white", bg="blue", font=("Arial", 16))
label.pack(pady=10)

# 創建按鈕並更改顏色
def change_color():
    label.config(text="顏色已更改", fg="black", bg="pink")

button = tk.Button(root, text="更改顏色", command=change_color, fg="white", bg="pink")
button.pack(pady=10)

# 啟動主循環
root.mainloop()





