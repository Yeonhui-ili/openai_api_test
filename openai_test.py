from dotenv import load_dotenv
import os
from openai import OpenAI

# api 키를 가져옴(보안)
load_dotenv()
openai_api_key=os.getenv("OPEN_API_KEY")

client = OpenAI(api_key = openai_api_key)

# GPT에게 질문하고 응답 받는 함수
def ask_to_gpt(messages, MODEL):
    response = client.chat.completions.create(
        model=MODEL,
        top_p=0.1,
        temperature=0.1,
        messages=messages,
    )
    return response.choices[0].message.content

def basic_chat():
    MODEL = "gpt-3.5-turbo-1106"

    #시키고 싶은 일. 초기 메세지
    want_to = """너는 아래 내용을 기반으로 질의응답을 하는 로봇이야.
                content {}"""
    content = "나는 짱 멋있는 사람이다"
    messages=[
            {'role': 'system', 'content': want_to.format(content)},
        ]

    # 사용자가 멈출 때까지 채팅
    while True:
        user_input = input('You: ')

        if user_input.lower() == 'quit':
            break

        messages.append(
            {'role': 'user', 'content': user_input},
        )

        response = ask_to_gpt(messages, MODEL)
        messages.append(
            {'role': 'assistant', 'content': response},
        )
        print('AI: ', response)

def completions_chat():
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
    )
    print(response.choices[0].message.content)

def json_chat():
    # json mode 이용. 후기 긍/부정 정리할 때 활용가능
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    response_format={ "type": "json_object" }, #응답 옵션 : json_object
    messages=[
        {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
        {"role": "user", "content": "음료가 너무 달고 끈적해요. 그래도 향은 인위적이지 않고 좋은것 같아요"}
    ]
    )
    print(response.choices[0].message.content)


basic_chat()
# completions_chat()
# json_chat()
