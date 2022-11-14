TIERS = (
    "Unrated",
    "Bronze 5", "Bronze 4", "Bronze 3", "Bronze 2", "Bronze 1",
    "Silver 5", "Silver 4", "Silver 3", "Silver 2", "Silver 1",
    "Gold 5", "Gold 4", "Gold 3", "Gold 2", "Gold 1",
    "Platinum 5", "Platinum 4", "Platinum 3", "Platinum 2", "Platinum 1",
    "Diamond 5", "Diamond 4", "Diamond 3", "Diamond 2", "Diamond 1",
    "Ruby 5", "Ruby 4", "Ruby 3", "Ruby 2", "Ruby 1",
    "Master"
)

THEMES = {
  # THEME: {TIER: [background-color, color1, color2, color3, color4, text-color], ...}
  'WARM': {
    'border': '#bfbfbf',
    'background': '#fdfdfd',
    'Unknown': ['#AAAAAA', '#666666', '#000000', '#000000', '#000000', '#000000'],
    'Unrated': ['#666666', '#2D2D2D', '#040202', '#040202', '#040202', '#040202'],
    'Bronze': ['#E8D3C6', '#D0BCB0', '#BE937A', '#88511E', '#522F15', '#A25B36'],
    'Silver': ['#F1F0F5', '#DAD3DE', '#ABA9AD', '#817B89', '#5F5865', '#7B7574'],
    'Gold': ['#F5F3F0', '#FFEF93', '#FDD876', '#FDB859', '#FA8B5A', '#FEBE70'],
    'Platinum': ['#F0F5F3', '#D9FDCE', '#A5FCB6', '#60EFB2', '#00D6A5', '#34E678'],
    'Diamond': ['#F1F0F5', '#D5E3FE', '#8EB9FF','#5F83FC', '#384EC7', '#3F8EEA'],
    'Ruby': ['#F5F3F0', '#FCE6E0', '#FFC8C6', '#FD88A0', '#EB4A52', '#E15C64'],
    'Master': ['#F3F0F5', '#D6F7FD', '#E1C3FF', '#F28FDF', '#FC6297', '#CB7CEF'],
  },
  'COLD': {
    'border': '#bfbfbf',
    'background': '#fdfdfd',
    'Unknown': ['#AAAAAA', '#666666', '#000000', '#000000', '#000000', '#000000'],
    'Unrated': ['#666666', '#2D2D2D', '#040202', '#040202', '#040202', '#040202'],
    'Bronze': ['#F1F0F5', '#C6B7AE', '#B5987B', '#8E6C51', '#5D432F', '#A25B36'],
    'Silver': ['#F1F0F5', '#D3D3DE', '#A1A5B2', '#7B7B9A', '#585865', '#5F606A'],
    'Gold': ['#F5F3F0', '#FFFC98', '#FFE765', '#FFC455', '#FF961D', '#FDC456'],
    'Platinum': ['#F0F5F3', '#C6FDD9', '#8CF8BF', '#39EACF', '#06CBE5', '#39E09D'],
    'Diamond': ['#F1F0F5', '#D5FFFF', '#A5F7F7', '#32DDF4', '#157DE5', '#1AC0F2'],
    'Ruby': ['#F5F3F0', '#FCDAE4', '#FDB8DE', '#F27399', '#E51062', '#DB306B'],
    'Master': ['#F3F0F5', '#CCFFFD', '#D5CBFF', '#E882F5', '#FC62B5', '#CB7CEF'],
  },
  'DARK': {
    'border': '#5c5c5c',
    'background': '#3f3f3f',
    'Unknown': ['#2f2f2f', '#2f2f2f', '#2f2f2f', '#2f2f2f', '#2f2f2f', '#afafaf'],
    'Unrated': ['#3a3a3a', '#2f2f2f', '#1f1f1f', '#0f0f0f', '#0f0f0f', '#dddddd'],
    'Bronze': ['#48423c', '#5e4d3c', '#a16b36', '#B18151', '#E6AD73', '#bb7027'],
    'Silver': ['#494b4c', '#6e6f72', '#969899', '#ccd1d3', '#F8FDFF', '#94989b'],
    'Gold': ['#584c3d', '#6E4F0F', '#896512', '#E69A42', '#FCCB6F', '#FDC456'],
    'Platinum': ['#475C55', '#387762', '#2FA57E', '#39E09D', '#00FFE2', '#39E09D'],
    'Diamond': ['#515055', '#4d6683', '#5489a3', '#57bcec', '#98DEFF', '#1AC0F2'],
    'Ruby': ['#64464e', '#863A4F', '#A22B4E', '#E06087', '#FFA7C2', '#f5457b'],
    'Master': ['#504E58', '#546C71', '#926D9D', '#C970BB', '#FF7CA8', '#CB7CEF'],
  }
}

TIER_RATES = (
    0, # unranked
    30, 60, 90, 120, 150, # bronze
    200, 300, 400, 500, 650, # silver
    800, 950, 1100, 1250, 1400, # gold
    1600, 1750, 1900, 2000, 2100, # platinum
    2200, 2300, 2400, 2500, 2600, # diamond
    2700, 2800, 2850, 2900, 2950, # ruby
    3000 # master
)
