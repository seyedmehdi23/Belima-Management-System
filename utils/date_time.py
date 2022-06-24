from persiantools.jdatetime import JalaliDateTime
import datetime

def get_now_jalali():
    res = JalaliDateTime.now()
    return res