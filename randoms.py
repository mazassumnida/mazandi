import random
from datetime import datetime, timedelta
from string import ascii_lowercase
from typing import Optional

from utils import get_tier_id

# tier: None=random, 0=unknown, 1~5: bronze, 6~10: silver, ...
def random_user(tier: Optional[str] = None):
  if not tier:
    tier = '{tier} {lv}'.format(
      tier=random.choice(['bronze', 'silver', 'gold', 'platinum', 'diamond', 'ruby', 'master']),
      lv=random.randint(1, 5)
    )
  elif len(tier.split(' ')) == 1:
    tier = '{tier} {lv}'.format(tier=tier, lv=random.randint(1, 5))
  print('tier', tier)
  hash = ''.join(random.choice(ascii_lowercase) for i in range(5))
  handle = 'random-{}'.format(hash)
  result = {
    'handle': handle,
    'bio': '',
    'organizations': [],
    'badge': None,
    'background': {
      'backgroundId': 'abstract_001_light',
      'backgroundImageUrl': 'https://static.solved.ac/profile_bg/abstract_001/abstract_001_light.png',
      'unlockedUserCount': 0,
      'displayName': '아이콘',
      'displayDescription': 'solved.ac 아이콘'
    },
    'profileImageUrl': None,
    'solvedCount': 69,
    'voteCount': 0,
    'class': 1,
    'classDecoration': 'none',
    'tier': get_tier_id(tier),
    'rating': 198,
    'ratingByProblemsSum': 122,
    'ratingByClass': 25,
    'ratingBySolvedCount': 51,
    'ratingByVoteCount': 0,
    'exp': 47544,
    'rivalCount': 0,
    'reverseRivalCount': 0,
    'maxStreak': 3,
    'rank': 29946
  }
  return result


# generate random timestamp
def random_timestamp():
  current = datetime.now()
  result = []
  count = 7 * 18   # 18 weeks
  for i in range(count):
    result.append({
      'timestamp': current.isoformat(),
      'value': count - i
    })
    current -= timedelta(hours=random.randint(0, 48))
  return result
