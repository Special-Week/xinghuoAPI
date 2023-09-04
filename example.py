from SparkApi import V2BotClient, V1BotClient

# 请在下面填入你的appid、api_secret、api_key
appid = "0******3"
api_secret = "QWE**************************XyZ"
api_key = "114**************************514"

if __name__ == "__main__":
    # 用1.5版本的接口
    bot1 = V1BotClient(
        appid=appid,
        api_key=api_key,
        api_secret=api_secret,
    )
    # 用2.0版本的接口
    bot2 = V2BotClient(
        appid=appid,
        api_key=api_key,
        api_secret=api_secret,
    )
    while True:
        # 输入问题
        question = input("我: ")
        # 用1.5版本的接口回答
        answer = bot1.ask(question)
        # 打印
        print(f"星火: {answer}")
