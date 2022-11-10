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
    # 18주 내 가장 많이 문제를 풀은 날의 solved count가 4 미만일 경우 4으로 설정
    solved_dict['solved_max'] = 4
    
    # solved.ac는 하루의 시작이 오전 6시이므로 UTC+3으로 변경
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
            solved_dict['solved_max'] = max(solved_dict['solved_max'], solved_dict[timestamp])
            
    solved_dict['solved_max'] = min(solved_dict['solved_max'], 50)

    return solved_dict


def get_starting_day():
    # 오늘 날짜와 오늘로부터 17주 전 일요일의 날짜를 반환
    # solved.ac는 하루의 시작이 오전 6시이므로 UTC+3으로 변경
    today = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
    # Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6
    weekday = today.isoweekday() % 7
    
    return today.strftime('%Y-%m-%d'), (today - datetime.timedelta(days=weekday + 119)).strftime('%Y-%m-%d')


def get_tomorrow(timestamp):
    # timestamp로부터 하루 뒤의 날짜를 반환
    timedata = datetime.datetime.strptime(timestamp, '%Y-%m-%d')
    tomorrow = timedata + datetime.timedelta(days=1)

    return tomorrow.strftime('%Y-%m-%d')


# solved.ac에서 사용하는 티어 id (0:Unrated, 1~5:Bronze, ..., 31:Master)
def get_tier_name(id: int):
  if id == 0: return 'Unrated'
  lut = ['Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Ruby', 'Master']
  tier = lut[(id - 1) // 5]
  lv = ((id - 1) % 5) + 1
  if tier == 'Master': return 'Master'
  return '{tier} {lv}'.format(tier=tier, lv=lv)


# 티어명을 solved.ac에서 사용하는 티어 id로 변환 ('Bronze 4' => 2)
def get_tier_id(name: str):
  name = name.lower()
  arr = name.split(' ') + [None] # padding when level is empty
  tier = arr[0]
  lv = int(arr[1]) if arr[1] else 0
  lut = ['bronze', 'silver', 'gold', 'platinum', 'diamond', 'ruby', 'master']
  if tier in lut:
    if tier == 'master': return 31
    return lut.index(tier) * 5 + lv
  return 0 # unrated
