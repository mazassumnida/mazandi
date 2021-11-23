# -*- coding: utf-8 -*-
import datetime
import pytz

def boj_rating_to_lv(rating):
    if rating < 30: return 0
    if rating < 150: return rating // 30
    if rating < 200: return 5
    if rating < 500: return (rating-200) // 100 + 6
    if rating < 1400: return (rating-500) // 150 + 9
    if rating < 1600: return 15
    if rating < 1750: return 16
    if rating < 1900: return 17
    if rating < 2800: return (rating-1900) // 100 + 18
    if rating < 3000: return (rating-2800) // 50 + 27
    return 31


def create_solved_dict(json):
    solved_dict = {}
    # solved.ac는 한국 시간 기준으로 매일 오전 6시에 변경되므로 UTC+3시간으로 변경
    today = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
    # Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6
    weekday = today.isoweekday() % 7

    for i, problem in enumerate(json):
        timedata = problem['timestamp'].split('.')[0].replace('T', ' ')
        trimmed_timedata = datetime.datetime.strptime(timedata, '%Y-%m-%d %H:%M:%S')
        
        KST = pytz.timezone('Europe/Moscow')        
        timestamp = pytz.utc.localize(trimmed_timedata).astimezone(KST)
        
        # 18주 내에 해결한 문제까지만 solved_dict에 저장
        if today - timestamp > datetime.timedelta(120 + weekday):
            return solved_dict
        
        timestamp = timestamp.strftime('%Y-%m-%d')

        if solved_dict.get(timestamp) == None:
            solved_dict[timestamp] = 1
        else:
            solved_dict[timestamp] += 1
            
    return solved_dict
