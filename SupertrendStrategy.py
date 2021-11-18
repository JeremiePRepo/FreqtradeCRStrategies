# pragma pylint: disable=missing-docstring, invalid-name, pointless-string-statement
# flake8: noqa: F401
# isort: skip_file
# --- Do not remove these libs ---
import numpy as np  # noqa
import pandas as pd  # noqa
from pandas import DataFrame

from freqtrade.strategy import (BooleanParameter, CategoricalParameter, DecimalParameter,
                                IStrategy, IntParameter)

# --------------------------------
# Add your lib to import here
import talib.abstract as ta
import freqtrade.vendor.qtpylib.indicators as qtpylib
import pandas_ta as pda


# This class is a sample. Feel free to customize it.
class SupertrendStrategy(IStrategy):
    """
    Sources : 
    Cripto Robot : https://www.youtube.com/watch?v=rl00g3-Iv5A
    Github : https://github.com/CryptoRobotFr/TrueStrategy/tree/main/3SuperTrend

    You can:
        :return: a Dataframe with all mandatory indicators for the strategies
    - Rename the class name (Do not forget to update class_name)
    - Add any methods you want to build your strategy
    - Add any lib you need to build your strategy

    You must keep:
    - the lib in the section "Do not remove these libs"
    - the methods: populate_indicators, populate_buy_trend, populate_sell_trend
    You should keep:
    - timeframe, minimal_roi, stoploss, trailing_*
    """
    # Strategy interface version - allow new iterations of the strategy interface.
    # Check the documentation or the Sample strategy to get the latest version.
    INTERFACE_VERSION = 2

    # Minimal ROI designed for the strategy.
    # This attribute will be overridden if the config file contains "minimal_roi".
    minimal_roi = {
        "0": 100 # inactive
    }

    # Optimal stoploss designed for the strategy.
    # This attribute will be overridden if the config file contains "stoploss".
    stoploss = -1 # inactive

    # Trailing stoploss
    trailing_stop = False
    # trailing_only_offset_is_reached = False
    # trailing_stop_positive = 0.01
    # trailing_stop_positive_offset = 0.0  # Disabled / not configured

    # Hyperoptable parameters
    buy_stoch_rsi = DecimalParameter(0.5, 1, decimals=3, default=0.8, space="buy")
    buy_ema_timeperiod = IntParameter(low=10, high=100, default=50, space='buy')
    sell_stoch_rsi = DecimalParameter(0, 0.5, decimals=3, default=0.2, space="sell")

    # Optimal timeframe for the strategy.
    timeframe = '1h'

    # Run "populate_indicators()" only for new candle.
    process_only_new_candles = False

    # These values can be overridden in the "ask_strategy" section in the config.
    use_sell_signal = True
    sell_profit_only = False
    ignore_roi_if_buy_signal = False

    # Number of candles the strategy requires before producing valid signals
    startup_candle_count: int = 30

    # Optional order type mapping.
    order_types = {
        'buy': 'limit',
        'sell': 'limit',
        'stoploss': 'market',
        'stoploss_on_exchange': False
    }

    # Optional order time in force.
    order_time_in_force = {
        'buy': 'gtc',
        'sell': 'gtc'
    }

    plot_config = {
        'main_plot': {
            'ema90':{},
            'supertrend_1':{},
            'supertrend_2':{},
            'supertrend_3':{},
        },
        'subplots': {
            "SUPERTREND DIRECTION": {
                'supertrend_direction_1': {},
                'supertrend_direction_2': {},
                'supertrend_direction_3': {},
            },
            "STOCH RSI": {
                'fastk_rsi': {},
            }
        }
    }

    def informative_pairs(self):
        """
        Define additional, informative pair/interval combinations to be cached from the exchange.
        These pair/interval combinations are non-tradeable, unless they are part
        of the whitelist as well.
        For more information, please consult the documentation
        :return: List of tuples in the format (pair, interval)
            Sample: return [("ETH/USDT", "5m"),
                            ("BTC/USDT", "15m"),
                            ]
        """
        return []

    def populate_indicators(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Adds several different TA indicators to the given DataFrame

        Performance Note: For the best performance be frugal on the number of indicators
        you are using. Let uncomment only the indicator you are using in your strategies
        or your hyperopt configuration, otherwise you will waste your memory and CPU usage.
        :param dataframe: Dataframe with data from the exchange
        :param metadata: Additional information, like the currently traded pair
        :return: a Dataframe with all mandatory indicators for the strategies
        """

        # Momentum Indicators
        # ------------------------------------

        # # Stochastic RSI
        # Please read https://github.com/freqtrade/freqtrade/issues/2961 before using this.
        # STOCHRSI is NOT aligned with tradingview, which may result in non-expected results.
        # stoch_rsi = ta.STOCHRSI(dataframe)
        # dataframe['fastd_rsi'] = stoch_rsi['fastd']
        # dataframe['fastk_rsi'] = stoch_rsi['fastk']

        # Aligned calculation, from the github issue
        timeperiod = 14
        dataframe['rsi'] = ta.RSI(dataframe, timeperiod)
        dataframe['fastk_rsi'] = (dataframe['rsi'] - dataframe['rsi'].rolling(timeperiod).min()) / (dataframe['rsi'].rolling(timeperiod).max() - dataframe['rsi'].rolling(timeperiod).min())

        # Overlap Studies
        # ------------------------------------

        # # EMA - Exponential Moving Average
        dataframe['ema90'] = ta.EMA(dataframe, timeperiod=90)

        # Supertrend
        ST_length = 20
        ST_multiplier = 3.0
        superTrend = pda.supertrend(dataframe['high'],dataframe['low'],dataframe['close'],length=ST_length,multiplier=ST_multiplier)
        dataframe['supertrend_1'] = superTrend['SUPERT_'+str(ST_length)+"_"+str(ST_multiplier)]
        dataframe['supertrend_direction_1'] = superTrend['SUPERTd_'+str(ST_length)+"_"+str(ST_multiplier)]
        
        ST_length = 20
        ST_multiplier = 4.0
        superTrend = pda.supertrend(dataframe['high'], dataframe['low'], dataframe['close'], length=ST_length, multiplier=ST_multiplier)
        dataframe['supertrend_2'] = superTrend['SUPERT_'+str(ST_length)+"_"+str(ST_multiplier)]
        dataframe['supertrend_direction_2'] = superTrend['SUPERTd_'+str(ST_length)+"_"+str(ST_multiplier)]
        
        ST_length = 40
        ST_multiplier = 8.0
        superTrend = pda.supertrend(dataframe['high'], dataframe['low'], dataframe['close'], length=ST_length, multiplier=ST_multiplier)
        dataframe['supertrend_3'] = superTrend['SUPERT_'+str(ST_length)+"_"+str(ST_multiplier)]
        dataframe['supertrend_direction_3'] = superTrend['SUPERTd_'+str(ST_length)+"_"+str(ST_multiplier)]

        return dataframe

    def populate_buy_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Based on TA indicators, populates the buy signal for the given dataframe
        :param dataframe: DataFrame populated with indicators
        :param metadata: Additional information, like the currently traded pair
        :return: DataFrame with buy column
        """
        dataframe.loc[
            (
                ((dataframe['supertrend_direction_1']+dataframe['supertrend_direction_2']+dataframe['supertrend_direction_3']) >= 1) &
                (dataframe['fastk_rsi'] < self.buy_stoch_rsi.value) &
                (dataframe['close'] > dataframe['ema90']) &
                (dataframe['volume'] > 0)
            ),
            'buy'] = 1

        return dataframe

    def populate_sell_trend(self, dataframe: DataFrame, metadata: dict) -> DataFrame:
        """
        Based on TA indicators, populates the sell signal for the given dataframe
        :param dataframe: DataFrame populated with indicators
        :param metadata: Additional information, like the currently traded pair
        :return: DataFrame with sell column
        """
        dataframe.loc[
            (
                ((dataframe['supertrend_direction_1']+dataframe['supertrend_direction_2']+dataframe['supertrend_direction_3']) < 1) &
                (dataframe['fastk_rsi'] > self.sell_stoch_rsi.value) &
                (dataframe['volume'] > 0)
            ),
            'sell'] = 1
        return dataframe