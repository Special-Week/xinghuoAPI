# 讯飞星火认知模型api调用(免费)

## 1. [白嫖API调用](https://xinghuo.xfyun.cn/sparkapi?scr=price)
![](./image/image.png)
![](./image/image2.png)
- 两个都可白嫖并且分别计算token(应该是)


## 2. 调用直接查看example
- 类V1BotClient是调用V1.5
- 类V2BotClient是调用V2.0
- 其实用websockets是支持流式的，并且SparkApi中on_message就是流式对answer进行+=操作，但我是想要作为bot调用就干脆bot.ask强行返还了最后的结果，如有流式需求可以自行修改