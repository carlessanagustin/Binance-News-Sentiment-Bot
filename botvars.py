############################################
#     USER INPUT VARIABLES LIVE BELOW      #
# You may edit those to configure your bot #
############################################

# select what coins to look for as keywords in articles headlines
# The key of each dict MUST be the symbol used for that coin on Binance
# Use each list to define keywords separated by commas: 'XRP': ['ripple', 'xrp']
# keywords are case sensitive
keywords = {
    'XRP': ['ripple', 'xrp', 'XRP', 'Ripple', 'RIPPLE'],
    'BTC': ['BTC', 'bitcoin', 'Bitcoin', 'BITCOIN'],
    'XLM': ['Stellar Lumens', 'XLM'],
    #'BCH': ['Bitcoin Cash', 'BCH'],
    'ETH': ['ETH', 'Ethereum'],
    'BNB' : ['BNB', 'Binance Coin'],
    'LTC': ['LTC', 'Litecoin']
    }

# The Buy amount in the PAIRING symbol, by default USDT
# 100 will for example buy the equivalent of 100 USDT in Bitcoin.
QUANTITY = 100

# define what to pair each coin to
# AVOID PAIRING WITH ONE OF THE COINS USED IN KEYWORDS
PAIRING = 'USDT'

# define how positive the news should be in order to place a trade
# the number is a compound of neg, neu and pos values from the nltk analysis
# input a number between -1 and 1
SENTIMENT_THRESHOLD = 0
NEGATIVE_SENTIMENT_THRESHOLD = 0

# define the minimum number of articles that need to be analysed in order
# for the sentiment analysis to qualify for a trade signal
# avoid using 1 as that's not representative of the overall sentiment
MINUMUM_ARTICLES = 1

# define how often to run the code (check for new + try to place trades)
# in minutes
REPEAT_EVERY = 60

############################################
#        END OF USER INPUT VARIABLES       #
#             Edit with care               #
############################################
