# FreqtradeCRStrategies
[Freqtrade](https://www.freqtrade.io/en/stable/ "Freqtrade documentation") strategies inspired by the [Crypto Robot Youtube channel](https://www.youtube.com/channel/UCGjfXO9kR34es5IsHLyP5eA "Crypto Robot Youtube channel").

- AlligatorStrategy: https://www.youtube.com/watch?v=tHYs5135jUA
- CrossEMAStrategy: https://www.youtube.com/watch?v=z9dbgvAYDuA
- SupertrendStrategy: https://www.youtube.com/watch?v=rl00g3-Iv5A
- TrixStrategy: https://www.youtube.com/watch?v=uE04UROWkjs

**This repository is not affiliated with the channel, it is a personal programming exercise.
Do not use these strategies without (back)testing them.**

## Installation

1. Install Freqtrade (see [documentation](https://www.freqtrade.io/en/stable/docker_quickstart/ "official documentation").)
2. Add strategies to your [user_data/strategies/](user_data/strategies/) folder
3. Set up your [/user_data/config.json](/user_data/config.json) file. You'll find some examples in this repo.
4. Add the strategy name in the [docker-compose.yml](/docker-compose.yml)

```
---
version: '3'
services:
  freqtrade:
    image: freqtradeorg/freqtrade:stable
    restart: unless-stopped
    container_name: freqtrade
    volumes:
      - "./user_data:/freqtrade/user_data"
    ports:
      - "127.0.0.1:8080:8080"
    command: >
      trade
      --logfile /freqtrade/user_data/logs/freqtrade.log
      --db-url sqlite:////freqtrade/user_data/tradesv3.sqlite
      --config /freqtrade/user_data/config.json
      --strategy TrixStrategy
```

5. In your Freqtrade folder: `sudo docker-compose up -d`

Thanks to Crypto Robot, and to all those who share their knowledge