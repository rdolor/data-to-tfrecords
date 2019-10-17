
import configparser


features_dtype_int  = ['click', 'weekday', 'region', 'city', 'adexchange', 'slotformat', 'hour', 'slotwidth',
                      'slotheight', 'slotvisibility', 'slotprice']
features_dtype_list = ['usertag']
all_features        = features_dtype_int + features_dtype_list

# Read Config file
INI = configparser.RawConfigParser()
INI.optionxform = str
INI.read('./data_to_tf/ini/setting.ini')
