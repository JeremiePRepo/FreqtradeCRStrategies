```
freqtrade backtesting --strategy TrixV23Strategy --stake-amount 100 --timeframe 1h --max-open-trades -1 --fee 0.001 --dry-run-wallet 1000 --timerange=20210101-
Creating freqtradelocal_freqtrade_run ... done
2021-12-17 18:15:40,132 - freqtrade.configuration.configuration - INFO - Using config: user_data/config.json ...
2021-12-17 18:15:40,134 - freqtrade.loggers - INFO - Verbosity set to 0
2021-12-17 18:15:40,134 - freqtrade.configuration.configuration - INFO - Parameter -i/--timeframe detected ... Using timeframe: 1h ...
2021-12-17 18:15:40,134 - freqtrade.configuration.configuration - INFO - Parameter --max-open-trades detected, overriding max_open_trades to: -1 ...
2021-12-17 18:15:40,134 - freqtrade.configuration.configuration - INFO - Parameter --stake-amount detected, overriding stake_amount to: 100.0 ...
2021-12-17 18:15:40,134 - freqtrade.configuration.configuration - INFO - Parameter --dry-run-wallet detected, overriding dry_run_wallet to: 1000.0 ...
2021-12-17 18:15:40,134 - freqtrade.configuration.configuration - INFO - Parameter --fee detected, setting fee to: 0.001 ...
2021-12-17 18:15:40,135 - freqtrade.configuration.configuration - INFO - Parameter --timerange detected: 20210101- ...
2021-12-17 18:15:41,318 - freqtrade.configuration.configuration - INFO - Using user-data directory: /freqtrade/user_data ...
2021-12-17 18:15:41,320 - freqtrade.configuration.configuration - INFO - Using data directory: /freqtrade/user_data/data/binance ...
2021-12-17 18:15:41,320 - freqtrade.configuration.configuration - INFO - Overriding timeframe with Command line argument
2021-12-17 18:15:41,320 - freqtrade.configuration.check_exchange - INFO - Checking exchange...
2021-12-17 18:15:41,328 - freqtrade.configuration.check_exchange - INFO - Exchange "binance" is officially supported by the Freqtrade development team.
2021-12-17 18:15:41,329 - freqtrade.configuration.configuration - INFO - Using pairlist from configuration.
2021-12-17 18:15:41,329 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2021-12-17 18:15:41,334 - freqtrade.commands.optimize_commands - INFO - Starting freqtrade in Backtesting mode
2021-12-17 18:15:41,334 - freqtrade.exchange.exchange - INFO - Instance is running with dry_run enabled
2021-12-17 18:15:41,334 - freqtrade.exchange.exchange - INFO - Using CCXT 1.61.92
2021-12-17 18:15:41,349 - freqtrade.exchange.exchange - INFO - Using Exchange "Binance"
2021-12-17 18:15:43,975 - freqtrade.resolvers.exchange_resolver - INFO - Using resolved exchange 'Binance'...
2021-12-17 18:15:44,560 - TrixV23Strategy - INFO - pandas_ta successfully imported
2021-12-17 18:15:44,716 - freqtrade.resolvers.iresolver - INFO - Using resolved strategy TrixV23Strategy from '/freqtrade/user_data/strategies/TrixV23Strategy.py'...
2021-12-17 18:15:44,717 - freqtrade.strategy.hyper - INFO - Loading parameters from file /freqtrade/user_data/strategies/TrixV23Strategy.json
2021-12-17 18:15:44,726 - freqtrade.strategy.hyper - INFO - Strategy Parameter: buy_btc_ema_enabled = True
2021-12-17 18:15:44,726 - freqtrade.strategy.hyper - INFO - Strategy Parameter: buy_btc_ema_multiplier = 0.996
2021-12-17 18:15:44,726 - freqtrade.strategy.hyper - INFO - Strategy Parameter: buy_btc_ema_timeperiod = 184
2021-12-17 18:15:44,726 - freqtrade.strategy.hyper - INFO - Strategy Parameter: buy_ema_enabled = True
2021-12-17 18:15:44,726 - freqtrade.strategy.hyper - INFO - Strategy Parameter: buy_ema_multiplier = 0.85
2021-12-17 18:15:44,726 - freqtrade.strategy.hyper - INFO - Strategy Parameter: buy_ema_src = open
2021-12-17 18:15:44,726 - freqtrade.strategy.hyper - INFO - Strategy Parameter: buy_ema_timeperiod = 10
2021-12-17 18:15:44,726 - freqtrade.strategy.hyper - INFO - Strategy Parameter: buy_rsi_timeperiod = 5
2021-12-17 18:15:44,726 - freqtrade.strategy.hyper - INFO - Strategy Parameter: buy_stoch_rsi = 0.629
2021-12-17 18:15:44,726 - freqtrade.strategy.hyper - INFO - Strategy Parameter: buy_stoch_rsi_enabled = True
2021-12-17 18:15:44,727 - freqtrade.strategy.hyper - INFO - Strategy Parameter: buy_stoch_rsi_timeperiod = 12
2021-12-17 18:15:44,727 - freqtrade.strategy.hyper - INFO - Strategy Parameter: buy_trix_signal_timeperiod = 22
2021-12-17 18:15:44,727 - freqtrade.strategy.hyper - INFO - Strategy Parameter: buy_trix_signal_type = trigger
2021-12-17 18:15:44,727 - freqtrade.strategy.hyper - INFO - Strategy Parameter: buy_trix_src = high
2021-12-17 18:15:44,727 - freqtrade.strategy.hyper - INFO - Strategy Parameter: buy_trix_timeperiod = 5
2021-12-17 18:15:44,727 - freqtrade.strategy.hyper - INFO - Strategy Parameter: sell_atr_enabled = True
2021-12-17 18:15:44,728 - freqtrade.strategy.hyper - INFO - Strategy Parameter: sell_atr_multiplier = 4.99
2021-12-17 18:15:44,728 - freqtrade.strategy.hyper - INFO - Strategy Parameter: sell_atr_timeperiod = 30
2021-12-17 18:15:44,728 - freqtrade.strategy.hyper - INFO - Strategy Parameter: sell_rsi_timeperiod = 12
2021-12-17 18:15:44,728 - freqtrade.strategy.hyper - INFO - Strategy Parameter: sell_stoch_rsi = 0.34
2021-12-17 18:15:44,728 - freqtrade.strategy.hyper - INFO - Strategy Parameter: sell_stoch_rsi_enabled = True
2021-12-17 18:15:44,728 - freqtrade.strategy.hyper - INFO - Strategy Parameter: sell_stoch_rsi_timeperiod = 23
2021-12-17 18:15:44,728 - freqtrade.strategy.hyper - INFO - Strategy Parameter: sell_trix_signal_timeperiod = 22
2021-12-17 18:15:44,728 - freqtrade.strategy.hyper - INFO - Strategy Parameter: sell_trix_signal_type = trailing
2021-12-17 18:15:44,728 - freqtrade.strategy.hyper - INFO - Strategy Parameter: sell_trix_src = low
2021-12-17 18:15:44,728 - freqtrade.strategy.hyper - INFO - Strategy Parameter: sell_trix_timeperiod = 12
2021-12-17 18:15:44,729 - freqtrade.strategy.hyper - INFO - No params for protection found, using default values.
2021-12-17 18:15:44,729 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'timeframe' with value in config file: 1h.
2021-12-17 18:15:44,729 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_currency' with value in config file: USDT.
2021-12-17 18:15:44,729 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'stake_amount' with value in config file: 100.0.
2021-12-17 18:15:44,729 - freqtrade.resolvers.strategy_resolver - INFO - Override strategy 'unfilledtimeout' with value in config file: {'buy': 10, 'sell': 30, 'unit': 'minutes', 'exit_timeout_count': 0}.        
2021-12-17 18:15:44,729 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using minimal_roi: {'0': 0.553, '423': 0.144, '751': 0.059, '1342': 0}
2021-12-17 18:15:44,730 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using timeframe: 1h
2021-12-17 18:15:44,730 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stoploss: -0.31
2021-12-17 18:15:44,730 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop: False
2021-12-17 18:15:44,730 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_stop_positive_offset: 0.0
2021-12-17 18:15:44,730 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using trailing_only_offset_is_reached: False
2021-12-17 18:15:44,730 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_custom_stoploss: True
2021-12-17 18:15:44,730 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using process_only_new_candles: False
2021-12-17 18:15:44,730 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_types: {'buy': 'limit', 'sell': 'limit', 'stoploss': 'market', 'stoploss_on_exchange': False}
2021-12-17 18:15:44,730 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using order_time_in_force: {'buy': 'gtc', 'sell': 'gtc'}
2021-12-17 18:15:44,730 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_currency: USDT
2021-12-17 18:15:44,731 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using stake_amount: 100.0
2021-12-17 18:15:44,731 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using protections: []
2021-12-17 18:15:44,731 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using startup_candle_count: 200
2021-12-17 18:15:44,731 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using unfilledtimeout: {'buy': 10, 'sell': 30, 'unit': 'minutes', 'exit_timeout_count': 0}
2021-12-17 18:15:44,731 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using use_sell_signal: True
2021-12-17 18:15:44,731 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using sell_profit_only: True
2021-12-17 18:15:44,731 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_roi_if_buy_signal: False
2021-12-17 18:15:44,731 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using sell_profit_offset: 0.0
2021-12-17 18:15:44,731 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using disable_dataframe_checks: False
2021-12-17 18:15:44,731 - freqtrade.resolvers.strategy_resolver - INFO - Strategy using ignore_buying_expired_candle_after: 0
2021-12-17 18:15:44,732 - freqtrade.configuration.config_validation - INFO - Validating configuration ...
2021-12-17 18:15:44,740 - freqtrade.resolvers.iresolver - INFO - Using resolved pairlist StaticPairList from '/freqtrade/freqtrade/plugins/pairlist/StaticPairList.py'...
2021-12-17 18:15:45,257 - freqtrade.plugins.pairlistmanager - WARNING - Pair ACM/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,257 - freqtrade.plugins.pairlistmanager - WARNING - Pair ASR/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,257 - freqtrade.plugins.pairlistmanager - WARNING - Pair ATM/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,257 - freqtrade.plugins.pairlistmanager - WARNING - Pair AUD/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,257 - freqtrade.plugins.pairlistmanager - WARNING - Pair BAR/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,257 - freqtrade.plugins.pairlistmanager - WARNING - Pair BTC/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,257 - freqtrade.plugins.pairlistmanager - WARNING - Pair BUSD/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,257 - freqtrade.plugins.pairlistmanager - WARNING - Pair CHZ/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,258 - freqtrade.plugins.pairlistmanager - WARNING - Pair CITY/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,258 - freqtrade.plugins.pairlistmanager - WARNING - Pair CTXC/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,258 - freqtrade.plugins.pairlistmanager - WARNING - Pair EUR/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,258 - freqtrade.plugins.pairlistmanager - WARNING - Pair FOR/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,258 - freqtrade.plugins.pairlistmanager - WARNING - Pair FTT/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,258 - freqtrade.plugins.pairlistmanager - WARNING - Pair GBP/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,258 - freqtrade.plugins.pairlistmanager - WARNING - Pair HBAR/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,259 - freqtrade.plugins.pairlistmanager - WARNING - Pair JUV/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,259 - freqtrade.plugins.pairlistmanager - WARNING - Pair NMR/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,259 - freqtrade.plugins.pairlistmanager - WARNING - Pair OG/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,259 - freqtrade.plugins.pairlistmanager - WARNING - Pair PSG/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,259 - freqtrade.plugins.pairlistmanager - WARNING - Pair SHIB/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,259 - freqtrade.plugins.pairlistmanager - WARNING - Pair SLP/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,260 - freqtrade.plugins.pairlistmanager - WARNING - Pair TUSD/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,260 - freqtrade.plugins.pairlistmanager - WARNING - Pair USDC/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,260 - freqtrade.plugins.pairlistmanager - WARNING - Pair XVS/USDT in your blacklist. Removing it from whitelist...
2021-12-17 18:15:45,262 - freqtrade.data.history.history_utils - INFO - Using indicator startup period: 200 ...
2021-12-17 18:15:45,284 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair 1INCH/USDT, data starts at 2020-12-25 05:00:00
2021-12-17 18:15:45,437 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair ADX/USDT, data starts at 2021-10-29 10:00:00
2021-12-17 18:15:45,457 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair AGLD/USDT, data starts at 2021-10-05 07:00:00
2021-12-17 18:15:45,590 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair ALICE/USDT, data starts at 2021-03-15 06:00:00
2021-12-17 18:15:45,612 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair ALPACA/USDT, data starts at 2021-08-11 08:00:00
2021-12-17 18:15:45,662 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair AMP/USDT, data starts at 2021-11-23 06:00:00
2021-12-17 18:15:45,815 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair AR/USDT, data starts at 2021-05-14 12:00:00
2021-12-17 18:15:45,923 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair ATA/USDT, data starts at 2021-06-07 06:00:00
2021-12-17 18:15:45,983 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair AUCTION/USDT, data starts at 2021-10-29 10:00:00
2021-12-17 18:15:46,039 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair AUTO/USDT, data starts at 2021-04-02 09:00:00
2021-12-17 18:15:46,211 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair BADGER/USDT, data starts at 2021-03-02 08:00:00
2021-12-17 18:15:46,237 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair BAKE/USDT, data starts at 2021-04-30 12:00:00
2021-12-17 18:15:46,534 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair BETA/USDT, data starts at 2021-10-08 12:00:00
2021-12-17 18:15:46,661 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair BNX/USDT, data starts at 2021-11-04 11:00:00
2021-12-17 18:15:46,684 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair BOND/USDT, data starts at 2021-07-05 06:00:00
2021-12-17 18:15:46,711 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair BTCST/USDT, data starts at 2021-01-13 06:00:00
2021-12-17 18:15:46,721 - freqtrade.data.converter - INFO - Missing data fillup for BTCST/USDT: before: 7893 - after: 8002 - 1.38%
2021-12-17 18:15:46,794 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair BTG/USDT, data starts at 2021-04-16 07:00:00
2021-12-17 18:15:46,898 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair BURGER/USDT, data starts at 2021-04-30 12:00:00
2021-12-17 18:15:46,953 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair C98/USDT, data starts at 2021-07-23 12:00:00
2021-12-17 18:15:46,978 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair CAKE/USDT, data starts at 2021-02-19 06:00:00
2021-12-17 18:15:47,007 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair CELO/USDT, data starts at 2021-01-05 08:00:00
2021-12-17 18:15:47,130 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair CFX/USDT, data starts at 2021-03-29 11:00:00
2021-12-17 18:15:47,152 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair CHESS/USDT, data starts at 2021-10-22 06:00:00
2021-12-17 18:15:47,216 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair CKB/USDT, data starts at 2021-01-26 12:00:00
2021-12-17 18:15:47,239 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair CLV/USDT, data starts at 2021-07-29 06:00:00
2021-12-17 18:15:47,563 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair CVP/USDT, data starts at 2021-10-04 10:00:00
2021-12-17 18:15:47,581 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair DAR/USDT, data starts at 2021-11-04 08:00:00
2021-12-17 18:15:47,716 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair DEGO/USDT, data starts at 2021-03-10 11:00:00
2021-12-17 18:15:47,838 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair DEXE/USDT, data starts at 2021-07-23 10:00:00
2021-12-17 18:15:47,858 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair DF/USDT, data starts at 2021-09-24 10:00:00
2021-12-17 18:15:48,018 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair DODO/USDT, data starts at 2021-02-19 10:00:00
2021-12-17 18:15:48,209 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair DYDX/USDT, data starts at 2021-09-09 02:00:00
2021-12-17 18:15:48,261 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair ELF/USDT, data starts at 2021-09-08 08:00:00
2021-12-17 18:15:48,326 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair ENS/USDT, data starts at 2021-11-10 07:00:00
2021-12-17 18:15:48,393 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair EPS/USDT, data starts at 2021-04-02 09:00:00
2021-12-17 18:15:48,421 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair ERN/USDT, data starts at 2021-06-22 06:00:00
2021-12-17 18:15:48,581 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair FARM/USDT, data starts at 2021-08-11 08:00:00
2021-12-17 18:15:48,640 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair FIDA/USDT, data starts at 2021-09-30 12:00:00
2021-12-17 18:15:48,729 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair FIRO/USDT, data starts at 2021-01-29 02:00:00
2021-12-17 18:15:48,757 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair FIS/USDT, data starts at 2021-03-03 08:00:00
2021-12-17 18:15:48,810 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair FLOW/USDT, data starts at 2021-07-30 13:00:00
2021-12-17 18:15:48,834 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair FORTH/USDT, data starts at 2021-04-23 09:00:00
2021-12-17 18:15:48,856 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair FRONT/USDT, data starts at 2021-10-04 10:00:00
2021-12-17 18:15:49,013 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair GALA/USDT, data starts at 2021-09-13 06:00:00
2021-12-17 18:15:49,034 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair GHST/USDT, data starts at 2021-08-20 10:00:00
2021-12-17 18:15:49,055 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair GNO/USDT, data starts at 2021-08-30 06:00:00
2021-12-17 18:15:49,108 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair GTC/USDT, data starts at 2021-06-10 10:00:00
2021-12-17 18:15:49,402 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair ICP/USDT, data starts at 2021-05-11 01:00:00
2021-12-17 18:15:49,464 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair IDEX/USDT, data starts at 2021-09-09 08:00:00
2021-12-17 18:15:49,484 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair ILV/USDT, data starts at 2021-09-22 06:00:00
2021-12-17 18:15:49,743 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair JASMY/USDT, data starts at 2021-11-22 12:00:00
2021-12-17 18:15:49,840 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair KEEP/USDT, data starts at 2021-06-17 06:00:00
2021-12-17 18:15:49,903 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair KLAY/USDT, data starts at 2021-06-24 08:00:00
2021-12-17 18:15:50,045 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair KP3R/USDT, data starts at 2021-11-12 10:00:00
2021-12-17 18:15:50,098 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair LAZIO/USDT, data starts at 2021-10-21 12:00:00
2021-12-17 18:15:50,123 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair LINA/USDT, data starts at 2021-03-18 12:00:00
2021-12-17 18:15:50,193 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair LIT/USDT, data starts at 2021-02-04 06:00:00
2021-12-17 18:15:50,218 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair LPT/USDT, data starts at 2021-05-28 05:00:00
2021-12-17 18:15:50,517 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair MASK/USDT, data starts at 2021-05-25 06:00:00
2021-12-17 18:15:50,676 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair MBOX/USDT, data starts at 2021-08-19 08:00:00
2021-12-17 18:15:50,736 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair MDX/USDT, data starts at 2021-05-24 09:00:00
2021-12-17 18:15:50,799 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair MINA/USDT, data starts at 2021-08-10 06:00:00
2021-12-17 18:15:50,825 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair MIR/USDT, data starts at 2021-04-19 11:00:00
2021-12-17 18:15:50,928 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair MLN/USDT, data starts at 2021-07-05 06:00:00
2021-12-17 18:15:50,947 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair MOVR/USDT, data starts at 2021-11-08 06:00:00
2021-12-17 18:15:51,253 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair NU/USDT, data starts at 2021-06-04 05:00:00
2021-12-17 18:15:51,450 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair OM/USDT, data starts at 2021-03-08 09:00:00
2021-12-17 18:15:51,826 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair PERP/USDT, data starts at 2021-03-19 08:00:00
2021-12-17 18:15:51,850 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair PHA/USDT, data starts at 2021-06-25 10:00:00
2021-12-17 18:15:51,870 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair PLA/USDT, data starts at 2021-11-23 06:00:00
2021-12-17 18:15:51,930 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair POLS/USDT, data starts at 2021-05-19 07:00:00
2021-12-17 18:15:51,951 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair POLY/USDT, data starts at 2021-09-09 08:00:00
2021-12-17 18:15:52,037 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair POND/USDT, data starts at 2021-03-09 08:00:00
2021-12-17 18:15:52,056 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair PORTO/USDT, data starts at 2021-11-16 12:00:00
2021-12-17 18:15:52,074 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair POWR/USDT, data starts at 2021-11-17 06:00:00
2021-12-17 18:15:52,099 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair PUNDIX/USDT, data starts at 2021-04-09 04:00:00
2021-12-17 18:15:52,119 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair PYR/USDT, data starts at 2021-11-26 08:00:00
2021-12-17 18:15:52,139 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair QI/USDT, data starts at 2021-11-15 08:00:00
2021-12-17 18:15:52,160 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair QNT/USDT, data starts at 2021-07-29 06:00:00
2021-12-17 18:15:52,223 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair QUICK/USDT, data starts at 2021-08-13 12:00:00
2021-12-17 18:15:52,243 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair RAD/USDT, data starts at 2021-10-07 07:00:00
2021-12-17 18:15:52,269 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair RAMP/USDT, data starts at 2021-03-22 09:00:00
2021-12-17 18:15:52,290 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair RARE/USDT, data starts at 2021-10-11 06:00:00
2021-12-17 18:15:52,312 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair RAY/USDT, data starts at 2021-08-10 06:00:00
2021-12-17 18:15:52,341 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair REEF/USDT, data starts at 2020-12-29 06:00:00
2021-12-17 18:15:52,438 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair REQ/USDT, data starts at 2021-08-20 10:00:00
2021-12-17 18:15:52,456 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair RGT/USDT, data starts at 2021-11-05 06:00:00
2021-12-17 18:15:52,484 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair RIF/USDT, data starts at 2021-01-07 13:00:00
2021-12-17 18:15:52,604 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair RNDR/USDT, data starts at 2021-11-27 10:00:00
2021-12-17 18:15:52,834 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair SFP/USDT, data starts at 2021-02-08 13:00:00
2021-12-17 18:15:53,290 - freqtrade.data.converter - INFO - Missing data fillup for SUN/USDT: before: 8386 - after: 8496 - 1.31%
2021-12-17 18:15:53,307 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair SUPER/USDT, data starts at 2021-03-25 10:00:00
2021-12-17 18:15:53,422 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair SYS/USDT, data starts at 2021-09-24 10:00:00
2021-12-17 18:15:53,621 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair TKO/USDT, data starts at 2021-04-07 13:00:00
2021-12-17 18:15:53,647 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair TLM/USDT, data starts at 2021-04-13 06:00:00
2021-12-17 18:15:53,710 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair TORN/USDT, data starts at 2021-06-11 06:00:00
2021-12-17 18:15:53,763 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair TRIBE/USDT, data starts at 2021-08-24 06:00:00
2021-12-17 18:15:53,830 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair TRU/USDT, data starts at 2021-01-19 07:00:00
2021-12-17 18:15:53,951 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair TVK/USDT, data starts at 2021-08-06 10:00:00
2021-12-17 18:15:53,979 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair TWT/USDT, data starts at 2021-01-27 08:00:00
2021-12-17 18:15:54,092 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair USDP/USDT, data starts at 2021-09-10 04:00:00
2021-12-17 18:15:54,179 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair VGX/USDT, data starts at 2021-11-22 07:00:00
2021-12-17 18:15:54,199 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair VIDT/USDT, data starts at 2021-09-09 08:00:00
2021-12-17 18:15:54,428 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair WAXP/USDT, data starts at 2021-08-23 06:00:00
2021-12-17 18:15:54,682 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair XEC/USDT, data starts at 2021-09-03 10:00:00
2021-12-17 18:15:54,964 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair XVG/USDT, data starts at 2021-06-06 10:00:00
2021-12-17 18:15:55,056 - freqtrade.data.history.idatahandler - WARNING - Missing data at start for pair YGG/USDT, data starts at 2021-09-24 06:00:00
2021-12-17 18:15:55,292 - freqtrade.optimize.backtesting - INFO - Loading data from 2020-12-23 16:00:00 up to 2021-12-12 15:00:00 (353 days).
2021-12-17 18:15:55,292 - freqtrade.optimize.backtesting - INFO - Dataload complete. Calculating indicators
2021-12-17 18:15:55,292 - freqtrade.optimize.backtesting - INFO - Running backtesting for Strategy TrixV23Strategy
2021-12-17 18:15:58,984 - freqtrade.optimize.backtesting - INFO - Backtesting with data from 2021-01-01 00:00:00 up to 2021-12-12 15:00:00 (345 days).
2021-12-17 18:16:27,893 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/backtest-result-2021-12-17_18-16-27.json"
2021-12-17 18:16:27,942 - freqtrade.misc - INFO - dumping json to "/freqtrade/user_data/backtest_results/.last_result.json"
Result for strategy TrixV23Strategy
============================================================= BACKTESTING REPORT ============================================================
|         Pair |   Buys |   Avg Profit % |   Cum Profit % |   Tot Profit USDT |   Tot Profit % |     Avg Duration |   Win  Draw  Loss  Win% |
|--------------+--------+----------------+----------------+-------------------+----------------+------------------+-------------------------|
|     OXT/USDT |     18 |           6.01 |         108.15 |           108.257 |          10.83 |         23:43:00 |    10     7     1  55.6 |
|    STMX/USDT |     15 |           7.05 |         105.70 |           105.805 |          10.58 |         17:44:00 |    10     2     3  66.7 |
|     NBS/USDT |     11 |           6.76 |          74.36 |            74.434 |           7.44 |         14:44:00 |     8     2     1  72.7 |
|     SUN/USDT |     16 |           4.11 |          65.73 |            65.800 |           6.58 |         16:38:00 |    13     3     0   100 |
|     ONG/USDT |     14 |           4.60 |          64.45 |            64.512 |           6.45 |         12:47:00 |    13     1     0   100 |
|     BTS/USDT |      6 |           9.80 |          58.79 |            58.851 |           5.89 |         10:10:00 |     5     0     1  83.3 |
|     MLN/USDT |     10 |           5.55 |          55.52 |            55.577 |           5.56 |   1 day, 3:30:00 |     6     3     1  60.0 |
|     CVC/USDT |     16 |           3.47 |          55.52 |            55.576 |           5.56 |         20:19:00 |    11     3     2  68.8 |
|    ANKR/USDT |     13 |           3.97 |          51.58 |            51.627 |           5.16 |   1 day, 1:46:00 |    10     1     2  76.9 |
|    TROY/USDT |     16 |           3.04 |          48.66 |            48.707 |           4.87 |         16:08:00 |    13     3     0   100 |
|    WING/USDT |     17 |           2.82 |          47.97 |            48.023 |           4.80 |         18:35:00 |    14     1     2  82.4 |
|    IOST/USDT |     14 |           3.26 |          45.64 |            45.684 |           4.57 |         12:47:00 |    13     1     0   100 |
|    VITE/USDT |     14 |           3.21 |          45.00 |            45.048 |           4.50 |   1 day, 4:34:00 |     7     5     2  50.0 |
|    CTSI/USDT |     14 |           3.03 |          42.48 |            42.522 |           4.25 |         15:04:00 |    11     3     0   100 |
|     CHR/USDT |      8 |           5.09 |          40.70 |            40.739 |           4.07 |         18:15:00 |     7     1     0   100 |
|  BADGER/USDT |      7 |           5.46 |          38.23 |            38.264 |           3.83 |         15:26:00 |     7     0     0   100 |
|    PERL/USDT |     13 |           2.90 |          37.66 |            37.695 |           3.77 |         21:46:00 |    10     3     0   100 |
|     WAN/USDT |     10 |           3.69 |          36.90 |            36.940 |           3.69 |         17:42:00 |     7     3     0   100 |
|     NEO/USDT |     15 |           2.39 |          35.91 |            35.942 |           3.59 |         15:00:00 |    14     0     1  93.3 |
|    RAMP/USDT |      7 |           4.84 |          33.89 |            33.928 |           3.39 |         12:26:00 |     6     0     1  85.7 |
|    BEAM/USDT |     12 |           2.81 |          33.73 |            33.764 |           3.38 |         23:40:00 |     8     3     1  66.7 |
|     REQ/USDT |      6 |           5.58 |          33.47 |            33.502 |           3.35 |   1 day, 6:30:00 |     2     2     2  33.3 |
|     UTK/USDT |     14 |           2.24 |          31.37 |            31.397 |           3.14 |         16:13:00 |     9     4     1  64.3 |
|    FARM/USDT |      5 |           6.20 |          30.98 |            31.010 |           3.10 |         18:00:00 |     2     0     3  40.0 |
|    CELO/USDT |     12 |           2.52 |          30.23 |            30.258 |           3.03 |         23:30:00 |     9     2     1  75.0 |
|     UMA/USDT |      8 |           3.76 |          30.07 |            30.098 |           3.01 |         16:52:00 |     5     2     1  62.5 |
|    UNFI/USDT |     15 |           2.00 |          30.06 |            30.085 |           3.01 |         20:08:00 |    11     2     2  73.3 |
|     KEY/USDT |      9 |           3.17 |          28.56 |            28.593 |           2.86 |         12:53:00 |     7     1     1  77.8 |
|    ARPA/USDT |     12 |           2.36 |          28.35 |            28.377 |           2.84 |         19:55:00 |     7     4     1  58.3 |
|     RLC/USDT |      9 |           3.08 |          27.68 |            27.712 |           2.77 |         18:40:00 |     6     3     0   100 |
|   OCEAN/USDT |      9 |           3.06 |          27.55 |            27.577 |           2.76 |         16:00:00 |     6     2     1  66.7 |
|     ONE/USDT |     10 |           2.71 |          27.11 |            27.137 |           2.71 |         16:18:00 |     7     2     1  70.0 |
|   SUSHI/USDT |     10 |           2.65 |          26.50 |            26.527 |           2.65 |         14:30:00 |     9     0     1  90.0 |
|    STPT/USDT |     15 |           1.76 |          26.41 |            26.434 |           2.64 |   1 day, 2:32:00 |     8     5     2  53.3 |
|     TRX/USDT |     12 |           2.15 |          25.75 |            25.778 |           2.58 |         16:30:00 |     9     2     1  75.0 |
|     MDT/USDT |     12 |           2.09 |          25.08 |            25.106 |           2.51 |  1 day, 13:50:00 |     5     7     0   100 |
|     CFX/USDT |      6 |           4.14 |          24.82 |            24.841 |           2.48 |   1 day, 6:50:00 |     3     3     0   100 |
|     WIN/USDT |     13 |           1.88 |          24.43 |            24.457 |           2.45 |         16:18:00 |     8     3     2  61.5 |
|     OMG/USDT |      7 |           3.46 |          24.22 |            24.241 |           2.42 |         14:09:00 |     5     2     0   100 |
|    ARDR/USDT |     16 |           1.51 |          24.11 |            24.137 |           2.41 |         20:52:00 |    12     2     2  75.0 |
|     TKO/USDT |      6 |           3.97 |          23.81 |            23.832 |           2.38 |         13:00:00 |     5     1     0   100 |
|     LTC/USDT |     13 |           1.79 |          23.31 |            23.333 |           2.33 |         16:28:00 |    10     2     1  76.9 |
|     SFP/USDT |      7 |           3.26 |          22.85 |            22.875 |           2.29 |         10:26:00 |     7     0     0   100 |
|     SNX/USDT |     14 |           1.62 |          22.64 |            22.664 |           2.27 |         16:43:00 |    11     1     2  78.6 |
|    LUNA/USDT |      7 |           3.21 |          22.44 |            22.467 |           2.25 |         20:51:00 |     4     3     0   100 |
|    MANA/USDT |     11 |           2.02 |          22.21 |            22.231 |           2.22 |         16:16:00 |     8     2     1  72.7 |
|     FIO/USDT |     12 |           1.84 |          22.11 |            22.135 |           2.21 |   1 day, 5:20:00 |     6     6     0   100 |
|     AVA/USDT |     13 |           1.63 |          21.21 |            21.227 |           2.12 |         21:46:00 |    10     1     2  76.9 |
|     QNT/USDT |      6 |           3.43 |          20.58 |            20.600 |           2.06 |         14:50:00 |     4     2     0   100 |
|     LSK/USDT |     13 |           1.56 |          20.29 |            20.313 |           2.03 |   1 day, 2:18:00 |     8     3     2  61.5 |
|     RVN/USDT |      6 |           3.15 |          18.91 |            18.932 |           1.89 |         15:40:00 |     5     1     0   100 |
|     HNT/USDT |      6 |           3.11 |          18.67 |            18.689 |           1.87 |         16:20:00 |     4     2     0   100 |
|   STORJ/USDT |      9 |           2.06 |          18.58 |            18.602 |           1.86 |         19:33:00 |     6     2     1  66.7 |
|     ERN/USDT |      6 |           3.07 |          18.44 |            18.455 |           1.85 |         23:00:00 |     4     2     0   100 |
|     XTZ/USDT |      4 |           4.60 |          18.40 |            18.415 |           1.84 |         14:45:00 |     4     0     0   100 |
|     SYS/USDT |      4 |           4.40 |          17.59 |            17.612 |           1.76 |         14:15:00 |     3     1     0   100 |
|   FORTH/USDT |      9 |           1.95 |          17.55 |            17.567 |           1.76 |         20:13:00 |     6     3     0   100 |
|    NULS/USDT |     13 |           1.35 |          17.53 |            17.549 |           1.75 |  1 day, 18:09:00 |     7     5     1  53.8 |
|   ALPHA/USDT |      7 |           2.49 |          17.44 |            17.456 |           1.75 |   1 day, 3:26:00 |     6     1     0   100 |
|    MASK/USDT |      5 |           3.39 |          16.94 |            16.956 |           1.70 |         18:48:00 |     2     3     0   100 |
|     HOT/USDT |     13 |           1.30 |          16.91 |            16.925 |           1.69 |  1 day, 16:32:00 |     8     3     2  61.5 |
|     COS/USDT |     14 |           1.20 |          16.84 |            16.859 |           1.69 |         18:00:00 |    12     0     2  85.7 |
|     RSR/USDT |      7 |           2.35 |          16.42 |            16.438 |           1.64 |         12:51:00 |     5     0     2  71.4 |
|    NANO/USDT |      8 |           2.02 |          16.16 |            16.174 |           1.62 |         16:15:00 |     6     2     0   100 |
|  BURGER/USDT |      9 |           1.79 |          16.11 |            16.125 |           1.61 |         19:13:00 |     7     2     0   100 |
|     BAT/USDT |     11 |           1.42 |          15.64 |            15.651 |           1.57 |         18:05:00 |     9     1     1  81.8 |
|   THETA/USDT |      6 |           2.59 |          15.53 |            15.548 |           1.55 |         19:10:00 |     4     1     1  66.7 |
|    BAND/USDT |      8 |           1.94 |          15.52 |            15.534 |           1.55 |         21:15:00 |     5     3     0   100 |
|   MATIC/USDT |     11 |           1.40 |          15.41 |            15.427 |           1.54 |         21:33:00 |     8     3     0   100 |
|    IRIS/USDT |     10 |           1.50 |          14.99 |            15.004 |           1.50 |         15:18:00 |     8     0     2  80.0 |
|    IOTX/USDT |      3 |           4.99 |          14.97 |            14.984 |           1.50 |          6:00:00 |     3     0     0   100 |
|    FIDA/USDT |      3 |           4.94 |          14.82 |            14.838 |           1.48 |         16:20:00 |     2     1     0   100 |
|     LIT/USDT |      9 |           1.64 |          14.80 |            14.817 |           1.48 |         20:07:00 |     7     1     1  77.8 |
|    PERP/USDT |     11 |           1.33 |          14.64 |            14.655 |           1.47 |         16:33:00 |     7     3     1  63.6 |
|     ADX/USDT |      1 |          14.39 |          14.39 |            14.400 |           1.44 |         10:00:00 |     1     0     0   100 |
|    AION/USDT |     10 |           1.43 |          14.30 |            14.316 |           1.43 |         17:06:00 |     7     1     2  70.0 |
|     LRC/USDT |     11 |           1.28 |          14.07 |            14.083 |           1.41 |         14:22:00 |     8     1     2  72.7 |
|     XLM/USDT |      7 |           2.00 |          14.01 |            14.027 |           1.40 |         11:26:00 |     7     0     0   100 |
|    POND/USDT |     12 |           1.14 |          13.70 |            13.715 |           1.37 |   1 day, 1:50:00 |     6     5     1  50.0 |
|     ETC/USDT |     16 |           0.82 |          13.18 |            13.197 |           1.32 |         19:15:00 |    11     3     2  68.8 |
|     VET/USDT |      7 |           1.88 |          13.18 |            13.196 |           1.32 |         15:43:00 |     4     2     1  57.1 |
|     FTM/USDT |      5 |           2.60 |          13.02 |            13.029 |           1.30 |   1 day, 4:36:00 |     3     2     0   100 |
|     NKN/USDT |      8 |           1.59 |          12.75 |            12.758 |           1.28 |         16:52:00 |     6     0     2  75.0 |
|     XEM/USDT |     11 |           1.13 |          12.39 |            12.402 |           1.24 |         19:55:00 |     8     2     1  72.7 |
|    WAXP/USDT |      5 |           2.47 |          12.34 |            12.348 |           1.23 |         13:24:00 |     3     1     1  60.0 |
|     TWT/USDT |      8 |           1.52 |          12.12 |            12.135 |           1.21 |         20:45:00 |     5     2     1  62.5 |
|    NEAR/USDT |     13 |           0.93 |          12.11 |            12.118 |           1.21 |         13:14:00 |     9     3     1  69.2 |
|     DOT/USDT |      8 |           1.48 |          11.85 |            11.863 |           1.19 |         16:30:00 |     6     1     1  75.0 |
|   STRAX/USDT |     10 |           1.10 |          11.05 |            11.057 |           1.11 |         22:54:00 |     5     4     1  50.0 |
|     ORN/USDT |      9 |           1.22 |          11.00 |            11.008 |           1.10 |         18:27:00 |     6     2     1  66.7 |
|    BZRX/USDT |      5 |           2.02 |          10.11 |            10.123 |           1.01 |         14:48:00 |     4     1     0   100 |
|     BEL/USDT |      6 |           1.48 |           8.87 |             8.879 |           0.89 |         14:10:00 |     5     1     0   100 |
|    VTHO/USDT |     13 |           0.67 |           8.77 |             8.781 |           0.88 |   1 day, 2:37:00 |     7     5     1  53.8 |
|     ICX/USDT |     13 |           0.64 |           8.31 |             8.320 |           0.83 |         13:42:00 |     9     2     2  69.2 |
|     ZEC/USDT |      7 |           1.11 |           7.78 |             7.784 |           0.78 |         15:00:00 |     5     2     0   100 |
|     BTG/USDT |     10 |           0.77 |           7.66 |             7.666 |           0.77 |         21:00:00 |     8     0     2  80.0 |
|   AUDIO/USDT |      8 |           0.92 |           7.37 |             7.375 |           0.74 |         18:52:00 |     5     1     2  62.5 |
|     RIF/USDT |     13 |           0.56 |           7.32 |             7.328 |           0.73 |         16:32:00 |    10     2     1  76.9 |
|    DEGO/USDT |     10 |           0.73 |           7.25 |             7.257 |           0.73 |   1 day, 6:36:00 |     4     5     1  40.0 |
|    DASH/USDT |      6 |           1.19 |           7.13 |             7.137 |           0.71 |          9:40:00 |     5     0     1  83.3 |
|  ALPACA/USDT |      3 |           2.26 |           6.77 |             6.779 |           0.68 |         22:20:00 |     2     1     0   100 |
|     REP/USDT |     17 |           0.38 |           6.49 |             6.492 |           0.65 |         16:11:00 |    15     1     1  88.2 |
|     LPT/USDT |      6 |           1.07 |           6.40 |             6.410 |           0.64 |   1 day, 4:20:00 |     3     3     0   100 |
|    POLY/USDT |      3 |           2.13 |           6.38 |             6.390 |           0.64 |   1 day, 2:00:00 |     2     1     0   100 |
|    LINA/USDT |      5 |           1.26 |           6.32 |             6.325 |           0.63 |         21:12:00 |     4     0     1  80.0 |
|    VIDT/USDT |      2 |           2.96 |           5.93 |             5.932 |           0.59 |         14:00:00 |     2     0     0   100 |
|    AKRO/USDT |     11 |           0.51 |           5.62 |             5.621 |           0.56 |         13:27:00 |     8     1     2  72.7 |
|     ADA/USDT |      9 |           0.62 |           5.57 |             5.572 |           0.56 |   1 day, 1:47:00 |     6     2     1  66.7 |
|    DOGE/USDT |      8 |           0.68 |           5.46 |             5.464 |           0.55 |         23:52:00 |     6     1     1  75.0 |
|   TFUEL/USDT |     10 |           0.53 |           5.28 |             5.287 |           0.53 |         16:12:00 |     8     1     1  80.0 |
|     ELF/USDT |      5 |           0.97 |           4.86 |             4.869 |           0.49 |   1 day, 0:12:00 |     3     1     1  60.0 |
|     ZRX/USDT |      4 |           1.07 |           4.30 |             4.301 |           0.43 |   1 day, 4:00:00 |     3     0     1  75.0 |
|    WNXM/USDT |      9 |           0.45 |           4.09 |             4.095 |           0.41 |         23:00:00 |     7     1     1  77.8 |
|     MBL/USDT |      9 |           0.41 |           3.70 |             3.708 |           0.37 |         18:13:00 |     6     2     1  66.7 |
|     JST/USDT |      9 |           0.39 |           3.52 |             3.526 |           0.35 |         10:00:00 |     7     0     2  77.8 |
|     MFT/USDT |      8 |           0.42 |           3.39 |             3.396 |           0.34 |         16:52:00 |     5     2     1  62.5 |
|     GTC/USDT |      4 |           0.84 |           3.37 |             3.373 |           0.34 |         17:45:00 |     4     0     0   100 |
|      NU/USDT |      8 |           0.39 |           3.15 |             3.153 |           0.32 |         17:15:00 |     6     2     0   100 |
|     AXS/USDT |     14 |           0.22 |           3.10 |             3.104 |           0.31 |         23:56:00 |     8     2     4  57.1 |
|     BNT/USDT |     11 |           0.27 |           2.92 |             2.919 |           0.29 |         10:44:00 |     8     1     2  72.7 |
|     BTT/USDT |     11 |           0.26 |           2.91 |             2.914 |           0.29 |   1 day, 6:33:00 |     6     2     3  54.5 |
|     RAD/USDT |      3 |           0.90 |           2.71 |             2.711 |           0.27 |   1 day, 0:00:00 |     2     0     1  66.7 |
|     CVP/USDT |      3 |           0.88 |           2.64 |             2.641 |           0.26 |         17:20:00 |     2     1     0   100 |
|     C98/USDT |      6 |           0.43 |           2.60 |             2.599 |           0.26 |         21:50:00 |     3     3     0   100 |
|     XEC/USDT |      5 |           0.51 |           2.56 |             2.560 |           0.26 |   1 day, 0:12:00 |     3     1     1  60.0 |
|    DOCK/USDT |     13 |           0.19 |           2.44 |             2.445 |           0.24 |         21:09:00 |     9     2     2  69.2 |
|     ILV/USDT |      5 |           0.47 |           2.36 |             2.362 |           0.24 |         21:36:00 |     3     1     1  60.0 |
|    DEXE/USDT |      8 |           0.25 |           2.01 |             2.016 |           0.20 |  1 day, 14:45:00 |     6     1     1  75.0 |
|    POLS/USDT |      7 |           0.28 |           1.95 |             1.953 |           0.20 |         18:51:00 |     6     0     1  85.7 |
|  PUNDIX/USDT |      6 |           0.31 |           1.87 |             1.874 |           0.19 |         17:10:00 |     3     2     1  50.0 |
|     TRU/USDT |      9 |           0.19 |           1.72 |             1.725 |           0.17 |   1 day, 6:27:00 |     4     2     3  44.4 |
|    KEEP/USDT |      2 |           0.78 |           1.56 |             1.561 |           0.16 |         13:00:00 |     2     0     0   100 |
|     TVK/USDT |      1 |           1.26 |           1.26 |             1.262 |           0.13 |         23:00:00 |     1     0     0   100 |
|   FRONT/USDT |      4 |           0.30 |           1.19 |             1.195 |           0.12 |   1 day, 2:45:00 |     1     3     0   100 |
|     MIR/USDT |      7 |           0.17 |           1.18 |             1.181 |           0.12 |         21:09:00 |     4     2     1  57.1 |
|      SC/USDT |      8 |           0.15 |           1.17 |             1.170 |           0.12 |         20:38:00 |     7     0     1  87.5 |
|     SKL/USDT |     10 |           0.11 |           1.11 |             1.111 |           0.11 |         14:24:00 |     6     1     3  60.0 |
|    HIVE/USDT |     14 |           0.08 |           1.11 |             1.110 |           0.11 |         20:09:00 |     9     2     3  64.3 |
|     PNT/USDT |     10 |           0.08 |           0.84 |             0.836 |           0.08 |         20:18:00 |     7     2     1  70.0 |
|     EOS/USDT |      4 |           0.21 |           0.83 |             0.833 |           0.08 |          9:45:00 |     3     0     1  75.0 |
|     SOL/USDT |      5 |           0.16 |           0.80 |             0.799 |           0.08 |         20:12:00 |     3     1     1  60.0 |
|   QUICK/USDT |      7 |           0.11 |           0.75 |             0.750 |           0.08 |         15:34:00 |     6     0     1  85.7 |
|    IDEX/USDT |      4 |           0.18 |           0.72 |             0.721 |           0.07 |         15:15:00 |     2     1     1  50.0 |
|     GNO/USDT |      2 |           0.22 |           0.44 |             0.439 |           0.04 |         19:00:00 |     1     0     1  50.0 |
|    RARE/USDT |      1 |           0.17 |           0.17 |             0.172 |           0.02 |          4:00:00 |     1     0     0   100 |
|     ICP/USDT |      5 |           0.03 |           0.14 |             0.140 |           0.01 |   1 day, 0:36:00 |     3     0     2  60.0 |
|    KLAY/USDT |      2 |           0.01 |           0.02 |             0.022 |           0.00 |         22:00:00 |     1     1     0   100 |
|    AGLD/USDT |      0 |           0.00 |           0.00 |             0.000 |           0.00 |             0:00 |     0     0     0     0 |
| AUCTION/USDT |      1 |           0.00 |           0.00 |             0.000 |           0.00 | 2 days, 23:00:00 |     0     1     0     0 |
|    BETA/USDT |      0 |           0.00 |           0.00 |             0.000 |           0.00 |             0:00 |     0     0     0     0 |
|     BNX/USDT |      0 |           0.00 |           0.00 |             0.000 |           0.00 |             0:00 |     0     0     0     0 |
|   CHESS/USDT |      1 |           0.00 |           0.00 |             0.000 |           0.00 |   1 day, 0:00:00 |     0     1     0     0 |
|     DAR/USDT |      0 |           0.00 |           0.00 |             0.000 |           0.00 |             0:00 |     0     0     0     0 |
|    DYDX/USDT |      2 |           0.00 |           0.00 |             0.000 |           0.00 |  1 day, 18:30:00 |     0     2     0     0 |
|    KP3R/USDT |      0 |           0.00 |           0.00 |             0.000 |           0.00 |             0:00 |     0     0     0     0 |
|   LAZIO/USDT |      0 |           0.00 |           0.00 |             0.000 |           0.00 |             0:00 |     0     0     0     0 |
|    MOVR/USDT |      0 |           0.00 |           0.00 |             0.000 |           0.00 |             0:00 |     0     0     0     0 |
|     PLA/USDT |      0 |           0.00 |           0.00 |             0.000 |           0.00 |             0:00 |     0     0     0     0 |
|   PORTO/USDT |      0 |           0.00 |           0.00 |             0.000 |           0.00 |             0:00 |     0     0     0     0 |
|    POWR/USDT |      0 |           0.00 |           0.00 |             0.000 |           0.00 |             0:00 |     0     0     0     0 |
|     PYR/USDT |      0 |           0.00 |           0.00 |             0.000 |           0.00 |             0:00 |     0     0     0     0 |
|      QI/USDT |      0 |           0.00 |           0.00 |             0.000 |           0.00 |             0:00 |     0     0     0     0 |
|    RNDR/USDT |      0 |           0.00 |           0.00 |             0.000 |           0.00 |             0:00 |     0     0     0     0 |
|     AMP/USDT |      1 |          -0.05 |          -0.05 |            -0.045 |          -0.00 |          1:00:00 |     0     0     1     0 |
|     ONT/USDT |      5 |          -0.03 |          -0.17 |            -0.170 |          -0.02 |         17:00:00 |     4     0     1  80.0 |
|    COTI/USDT |      8 |          -0.02 |          -0.18 |            -0.184 |          -0.02 |         20:00:00 |     4     3     1  50.0 |
|    DUSK/USDT |     14 |          -0.01 |          -0.20 |            -0.197 |          -0.02 |         16:00:00 |     9     2     3  64.3 |
|     GTO/USDT |     10 |          -0.04 |          -0.36 |            -0.365 |          -0.04 |   1 day, 1:12:00 |     5     4     1  50.0 |
|     FUN/USDT |      5 |          -0.10 |          -0.49 |            -0.494 |          -0.05 |  1 day, 14:00:00 |     3     1     1  60.0 |
|    USDP/USDT |      5 |          -0.11 |          -0.56 |            -0.563 |          -0.06 |  8 days, 1:24:00 |     0     3     2     0 |
|     MTL/USDT |     14 |          -0.04 |          -0.61 |            -0.614 |          -0.06 |         15:47:00 |     9     2     3  64.3 |
|     ZEN/USDT |      6 |          -0.14 |          -0.84 |            -0.837 |          -0.08 |         14:40:00 |     5     0     1  83.3 |
|     DCR/USDT |      8 |          -0.15 |          -1.20 |            -1.199 |          -0.12 |         15:08:00 |     7     0     1  87.5 |
|    CAKE/USDT |      6 |          -0.24 |          -1.44 |            -1.446 |          -0.14 |         18:30:00 |     5     0     1  83.3 |
|     FLM/USDT |      8 |          -0.18 |          -1.46 |            -1.458 |          -0.15 |         12:08:00 |     6     0     2  75.0 |
|   WAVES/USDT |     12 |          -0.13 |          -1.54 |            -1.537 |          -0.15 |         22:20:00 |     8     2     2  66.7 |
|    COMP/USDT |      6 |          -0.26 |          -1.54 |            -1.540 |          -0.15 |   1 day, 7:50:00 |     3     2     1  50.0 |
|    BAKE/USDT |      4 |          -0.41 |          -1.62 |            -1.623 |          -0.16 |   1 day, 1:00:00 |     3     0     1  75.0 |
|    GHST/USDT |      6 |          -0.34 |          -2.03 |            -2.034 |          -0.20 |         15:40:00 |     4     1     1  66.7 |
|    EGLD/USDT |      8 |          -0.27 |          -2.17 |            -2.172 |          -0.22 |         16:52:00 |     6     1     1  75.0 |
|      AR/USDT |      4 |          -0.62 |          -2.47 |            -2.473 |          -0.25 |   1 day, 2:15:00 |     1     2     1  25.0 |
|    SUSD/USDT |     23 |          -0.11 |          -2.57 |            -2.574 |          -0.26 |         23:08:00 |    10    10     3  43.5 |
|     CKB/USDT |      4 |          -0.66 |          -2.63 |            -2.630 |          -0.26 |         14:30:00 |     3     0     1  75.0 |
|    LINK/USDT |      7 |          -0.38 |          -2.68 |            -2.679 |          -0.27 |         19:43:00 |     4     1     2  57.1 |
|    IOTA/USDT |     13 |          -0.22 |          -2.86 |            -2.858 |          -0.29 |   1 day, 4:05:00 |     7     3     3  53.8 |
|     REN/USDT |     11 |          -0.27 |          -3.00 |            -3.002 |          -0.30 |         17:22:00 |     8     1     2  72.7 |
|     XRP/USDT |      9 |          -0.34 |          -3.02 |            -3.021 |          -0.30 |         16:53:00 |     6     1     2  66.7 |
|    AVAX/USDT |      5 |          -0.76 |          -3.82 |            -3.824 |          -0.38 |  1 day, 11:12:00 |     4     0     1  80.0 |
|   TRIBE/USDT |      5 |          -0.79 |          -3.93 |            -3.931 |          -0.39 |         15:12:00 |     2     2     1  40.0 |
|   BTCST/USDT |     14 |          -0.29 |          -3.99 |            -3.995 |          -0.40 |         13:47:00 |     8     2     4  57.1 |
|     KSM/USDT |      5 |          -0.84 |          -4.22 |            -4.226 |          -0.42 |         18:48:00 |     3     1     1  60.0 |
|     SXP/USDT |      9 |          -0.48 |          -4.33 |            -4.331 |          -0.43 |  1 day, 13:20:00 |     4     3     2  44.4 |
|     WTC/USDT |      9 |          -0.50 |          -4.49 |            -4.491 |          -0.45 |         20:40:00 |     5     2     2  55.6 |
|     ETH/USDT |      5 |          -0.96 |          -4.78 |            -4.786 |          -0.48 |         20:36:00 |     2     1     2  40.0 |
|     PHA/USDT |      2 |          -2.47 |          -4.93 |            -4.936 |          -0.49 |         14:00:00 |     1     0     1  50.0 |
|     WRX/USDT |     16 |          -0.31 |          -5.03 |            -5.034 |          -0.50 |         20:56:00 |    10     4     2  62.5 |
|     KMD/USDT |     12 |          -0.44 |          -5.24 |            -5.245 |          -0.52 |         18:55:00 |     7     3     2  58.3 |
|     BAL/USDT |     10 |          -0.59 |          -5.93 |            -5.941 |          -0.59 |         10:18:00 |     8     0     2  80.0 |
|    HARD/USDT |     11 |          -0.55 |          -6.03 |            -6.039 |          -0.60 |         20:55:00 |     5     4     2  45.5 |
|    REEF/USDT |     11 |          -0.57 |          -6.24 |            -6.249 |          -0.62 |         16:22:00 |     8     1     2  72.7 |
|    FLOW/USDT |      7 |          -0.91 |          -6.37 |            -6.381 |          -0.64 |   1 day, 3:00:00 |     3     2     2  42.9 |
|    PAXG/USDT |     19 |          -0.38 |          -7.19 |            -7.200 |          -0.72 |   1 day, 1:16:00 |     6    10     3  31.6 |
|    AUTO/USDT |      6 |          -1.20 |          -7.20 |            -7.211 |          -0.72 |         20:40:00 |     3     2     1  50.0 |
|     STX/USDT |      6 |          -1.21 |          -7.26 |            -7.263 |          -0.73 |         20:50:00 |     3     2     1  50.0 |
|     LTO/USDT |      2 |          -3.69 |          -7.38 |            -7.388 |          -0.74 |  1 day, 11:30:00 |     1     0     1  50.0 |
|     RAY/USDT |      2 |          -3.79 |          -7.58 |            -7.591 |          -0.76 | 2 days, 18:30:00 |     0     1     1     0 |
|     MDX/USDT |      6 |          -1.35 |          -8.08 |            -8.084 |          -0.81 |         17:00:00 |     3     1     2  50.0 |
|    ALGO/USDT |     12 |          -0.68 |          -8.10 |            -8.111 |          -0.81 |         12:15:00 |     8     2     2  66.7 |
|     KNC/USDT |      8 |          -1.10 |          -8.80 |            -8.811 |          -0.88 |         16:00:00 |     6     1     1  75.0 |
|     YGG/USDT |      3 |          -2.93 |          -8.80 |            -8.812 |          -0.88 |  1 day, 12:00:00 |     0     2     1     0 |
|     CLV/USDT |      3 |          -3.07 |          -9.22 |            -9.234 |          -0.92 |   1 day, 0:20:00 |     1     1     1  33.3 |
|     UNI/USDT |      7 |          -1.33 |          -9.32 |            -9.328 |          -0.93 |  1 day, 10:51:00 |     2     3     2  28.6 |
|      DF/USDT |      4 |          -2.33 |          -9.32 |            -9.330 |          -0.93 |   1 day, 2:00:00 |     1     2     1  25.0 |
|   JASMY/USDT |      1 |          -9.40 |          -9.40 |            -9.412 |          -0.94 |   1 day, 1:00:00 |     0     0     1     0 |
|     BCH/USDT |     10 |          -1.04 |         -10.43 |           -10.445 |          -1.04 |         16:24:00 |     5     2     3  50.0 |
|    DENT/USDT |      8 |          -1.31 |         -10.51 |           -10.518 |          -1.05 |   1 day, 2:00:00 |     4     1     3  50.0 |
|    BOND/USDT |     10 |          -1.05 |         -10.52 |           -10.528 |          -1.05 |   1 day, 9:30:00 |     3     4     3  30.0 |
|    ROSE/USDT |     16 |          -0.70 |         -11.21 |           -11.220 |          -1.12 |         13:56:00 |    11     1     4  68.8 |
|    MITH/USDT |     13 |          -0.86 |         -11.21 |           -11.225 |          -1.12 |  1 day, 16:18:00 |     6     4     3  46.2 |
|    KAVA/USDT |     13 |          -0.86 |         -11.24 |           -11.249 |          -1.12 |         13:51:00 |     9     2     2  69.2 |
|     ZIL/USDT |      6 |          -1.98 |         -11.86 |           -11.872 |          -1.19 |         21:30:00 |     2     2     2  33.3 |
|     SRM/USDT |      9 |          -1.35 |         -12.13 |           -12.142 |          -1.21 |         23:20:00 |     4     1     4  44.4 |
|   ALICE/USDT |      4 |          -3.09 |         -12.36 |           -12.368 |          -1.24 | 2 days, 12:15:00 |     1     2     1  25.0 |
|    GALA/USDT |      1 |         -12.56 |         -12.56 |           -12.576 |          -1.26 | 7 days, 18:00:00 |     0     0     1     0 |
|    MBOX/USDT |      1 |         -12.58 |         -12.58 |           -12.592 |          -1.26 | 3 days, 11:00:00 |     0     0     1     0 |
|     BLZ/USDT |      7 |          -1.81 |         -12.67 |           -12.680 |          -1.27 |   1 day, 4:26:00 |     4     1     2  57.1 |
|    DODO/USDT |      2 |          -6.48 |         -12.96 |           -12.974 |          -1.30 |         19:00:00 |     1     0     1  50.0 |
|   1INCH/USDT |      5 |          -2.63 |         -13.16 |           -13.174 |          -1.32 |         17:24:00 |     2     1     2  40.0 |
|     RGT/USDT |      1 |         -13.31 |         -13.31 |           -13.326 |          -1.33 |         17:00:00 |     0     0     1     0 |
|    CELR/USDT |     14 |          -0.96 |         -13.38 |           -13.394 |          -1.34 |         18:04:00 |     9     2     3  64.3 |
|     EPS/USDT |      6 |          -2.31 |         -13.83 |           -13.845 |          -1.38 |   1 day, 0:20:00 |     2     3     1  33.3 |
|    YFII/USDT |     12 |          -1.17 |         -13.99 |           -14.007 |          -1.40 |         23:35:00 |     8     1     3  66.7 |
|     TRB/USDT |      8 |          -1.79 |         -14.32 |           -14.337 |          -1.43 |         14:15:00 |     4     1     3  50.0 |
|     DIA/USDT |     15 |          -0.98 |         -14.65 |           -14.663 |          -1.47 |         16:36:00 |    10     2     3  66.7 |
|    FIRO/USDT |      5 |          -3.00 |         -14.98 |           -14.993 |          -1.50 |   1 day, 7:12:00 |     2     1     2  40.0 |
|     GRT/USDT |     10 |          -1.50 |         -15.00 |           -15.010 |          -1.50 |         21:12:00 |     7     0     3  70.0 |
|    TORN/USDT |      4 |          -3.77 |         -15.08 |           -15.092 |          -1.51 |  2 days, 1:30:00 |     1     1     2  25.0 |
|     VGX/USDT |      1 |         -15.30 |         -15.30 |           -15.312 |          -1.53 |         17:00:00 |     0     0     1     0 |
|     XVG/USDT |      8 |          -1.92 |         -15.34 |           -15.357 |          -1.54 |   1 day, 1:30:00 |     4     1     3  50.0 |
|     BNB/USDT |     12 |          -1.29 |         -15.50 |           -15.514 |          -1.55 |         14:55:00 |     6     2     4  50.0 |
|     DGB/USDT |      9 |          -1.85 |         -16.62 |           -16.638 |          -1.66 |   1 day, 1:27:00 |     5     1     3  55.6 |
|    MINA/USDT |      4 |          -4.25 |         -17.01 |           -17.027 |          -1.70 |   1 day, 0:30:00 |     1     1     2  25.0 |
|     XMR/USDT |     13 |          -1.33 |         -17.32 |           -17.335 |          -1.73 |         17:42:00 |     9     1     3  69.2 |
|    RUNE/USDT |      3 |          -5.79 |         -17.36 |           -17.374 |          -1.74 |         11:20:00 |     1     1     1  33.3 |
|     OGN/USDT |      9 |          -2.01 |         -18.13 |           -18.152 |          -1.82 |         16:20:00 |     4     3     2  44.4 |
|     GXS/USDT |     12 |          -1.52 |         -18.18 |           -18.200 |          -1.82 |         17:30:00 |     7     2     3  58.3 |
|     ENJ/USDT |      8 |          -2.29 |         -18.36 |           -18.377 |          -1.84 |         21:22:00 |     3     2     3  37.5 |
|     FIL/USDT |     12 |          -1.57 |         -18.85 |           -18.873 |          -1.89 |         21:45:00 |     5     3     4  41.7 |
|     ANT/USDT |      9 |          -2.11 |         -18.95 |           -18.967 |          -1.90 |         23:40:00 |     6     0     3  66.7 |
|    TOMO/USDT |      7 |          -2.73 |         -19.14 |           -19.155 |          -1.92 |         16:09:00 |     5     0     2  71.4 |
|     FET/USDT |     12 |          -1.60 |         -19.19 |           -19.210 |          -1.92 |   1 day, 2:25:00 |     4     5     3  33.3 |
|     ENS/USDT |      1 |         -21.16 |         -21.16 |           -21.183 |          -2.12 |  2 days, 3:00:00 |     0     0     1     0 |
|     CRV/USDT |     10 |          -2.21 |         -22.13 |           -22.150 |          -2.22 |         23:06:00 |     5     2     3  50.0 |
|     YFI/USDT |     10 |          -2.21 |         -22.15 |           -22.170 |          -2.22 |   1 day, 0:24:00 |     6     1     3  60.0 |
|     TLM/USDT |      5 |          -4.61 |         -23.07 |           -23.091 |          -2.31 | 2 days, 16:00:00 |     1     2     2  20.0 |
|    DATA/USDT |      6 |          -4.23 |         -25.40 |           -25.427 |          -2.54 |   1 day, 6:30:00 |     3     1     2  50.0 |
|      OM/USDT |      7 |          -3.76 |         -26.31 |           -26.333 |          -2.63 |         23:17:00 |     1     4     2  14.3 |
|     MKR/USDT |      9 |          -3.09 |         -27.82 |           -27.843 |          -2.78 |   1 day, 3:07:00 |     4     1     4  44.4 |
|   SUPER/USDT |     11 |          -2.67 |         -29.33 |           -29.357 |          -2.94 |         21:38:00 |     6     3     2  54.5 |
|    AAVE/USDT |      8 |          -3.76 |         -30.08 |           -30.113 |          -3.01 |         22:52:00 |     5     0     3  62.5 |
|     FIS/USDT |     15 |          -2.38 |         -35.68 |           -35.719 |          -3.57 |   1 day, 7:44:00 |     6     4     5  40.0 |
|     ATA/USDT |      8 |          -4.52 |         -36.13 |           -36.163 |          -3.62 |  2 days, 7:22:00 |     2     4     2  25.0 |
|     INJ/USDT |      9 |          -4.35 |         -39.12 |           -39.156 |          -3.92 |   1 day, 2:20:00 |     3     2     4  33.3 |
|    QTUM/USDT |      8 |          -5.22 |         -41.74 |           -41.779 |          -4.18 |         14:52:00 |     3     1     4  37.5 |
|     TCT/USDT |     12 |          -4.39 |         -52.67 |           -52.719 |          -5.27 |   1 day, 7:55:00 |     4     3     5  33.3 |
|     CTK/USDT |     11 |          -4.86 |         -53.43 |           -53.482 |          -5.35 |         15:49:00 |     6     1     4  54.5 |
|     DNT/USDT |     10 |          -5.39 |         -53.92 |           -53.976 |          -5.40 |   1 day, 4:12:00 |     4     1     5  40.0 |
|    SAND/USDT |     16 |          -3.59 |         -57.38 |           -57.438 |          -5.74 |   1 day, 6:22:00 |     9     2     5  56.2 |
|    ATOM/USDT |     11 |          -5.93 |         -65.26 |           -65.327 |          -6.53 |   1 day, 0:38:00 |     5     0     6  45.5 |
|        TOTAL |   2176 |           0.59 |        1280.64 |          1281.925 |         128.19 |         21:32:00 |  1370   433   373  63.0 |
========================================================== BUY TAG STATS ===========================================================
|   TAG |   Buys |   Avg Profit % |   Cum Profit % |   Tot Profit USDT |   Tot Profit % |   Avg Duration |   Win  Draw  Loss  Win% |
|-------+--------+----------------+----------------+-------------------+----------------+----------------+-------------------------|
| TOTAL |   2176 |           0.59 |        1280.64 |          1281.925 |         128.19 |       21:32:00 |  1370   433   373  63.0 |
======================================================= SELL REASON STATS ========================================================
|        Sell Reason |   Sells |   Win  Draws  Loss  Win% |   Avg Profit % |   Cum Profit % |   Tot Profit USDT |   Tot Profit % |
|--------------------+---------+--------------------------+----------------+----------------+-------------------+----------------|
|                roi |     985 |    552   433     0   100 |           4.49 |        4427.11 |          4431.53  |          16.46 |
|        sell_signal |     818 |    818     0     0   100 |           1.27 |        1039.05 |          1040.09  |           3.86 |
| trailing_stop_loss |     369 |      0     0   369     0 |         -11.09 |       -4092.06 |         -4096.15  |         -15.21 |
|          stop_loss |       3 |      0     0     3     0 |         -31.14 |         -93.41 |           -93.507 |          -0.35 |
|         force_sell |       1 |      0     0     1     0 |          -0.05 |          -0.05 |            -0.045 |          -0    |
======================================================= LEFT OPEN TRADES REPORT =======================================================
|     Pair |   Buys |   Avg Profit % |   Cum Profit % |   Tot Profit USDT |   Tot Profit % |   Avg Duration |   Win  Draw  Loss  Win% |
|----------+--------+----------------+----------------+-------------------+----------------+----------------+-------------------------|
| AMP/USDT |      1 |          -0.05 |          -0.05 |            -0.045 |          -0.00 |        1:00:00 |     0     0     1     0 |
|    TOTAL |      1 |          -0.05 |          -0.05 |            -0.045 |          -0.00 |        1:00:00 |     0     0     1     0 |
=============== SUMMARY METRICS ================
| Metric                 | Value               |
|------------------------+---------------------|
| Backtesting from       | 2021-01-01 00:00:00 |
| Backtesting to         | 2021-12-12 15:00:00 |
| Max open trades        | 269                 |
|                        |                     |
| Total/Daily Avg Trades | 2176 / 6.31         |
| Starting balance       | 1000.000 USDT       |
| Final balance          | 2281.925 USDT       |
| Absolute profit        | 1281.925 USDT       |
| Total profit %         | 128.19%             |
| Trades per day         | 6.31                |
| Avg. daily profit %    | 0.37%               |
| Avg. stake amount      | 100.000 USDT        |
| Total trade volume     | 217600.000 USDT     |
|                        |                     |
| Best Pair              | OXT/USDT 108.15%    |
| Worst Pair             | ATOM/USDT -65.26%   |
| Best trade             | BTS/USDT 55.24%     |
| Worst trade            | DNT/USDT -31.14%    |
| Best day               | 134.056 USDT        |
| Worst day              | -225.890 USDT       |
| Days win/draw/lose     | 158 / 111 / 77      |
| Avg. Duration Winners  | 12:30:00            |
| Avg. Duration Loser    | 1 day, 10:50:00     |
| Rejected Buy signals   | 0                   |
|                        |                     |
| Min balance            | 1006.681 USDT       |
| Max balance            | 2511.253 USDT       |
| Drawdown               | 470.75%             |
| Drawdown               | 471.220 USDT        |
| Drawdown high          | 1153.072 USDT       |
| Drawdown low           | 681.853 USDT        |
| Drawdown Start         | 2021-05-04 00:00:00 |
| Drawdown End           | 2021-07-22 22:00:00 |
| Market change          | 561.59%             |
================================================
```