from openai import OpenAI

client = OpenAI(
    api_key = "api-key"
)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "You are a helpful assistant that only returns Python code."},
        {"role": "user", "content": """我需要生成一個 Python 迴圈，具體要求如下：
        
        1. 這段程式碼要能生成一個tkinter 的calculator,
        2. 請注意，回應中僅需包含可執行的程式碼，不要有額外的文字。
        """}
    ]

)

output = response.choices[0].message.content.strip()
output = output[9:-3]

print(output)
try:
    exec(output)
except Exception as e:
    print(f"執行生成的程式碼時發生錯誤: {e}")