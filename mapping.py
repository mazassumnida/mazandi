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

COLOR_WARM = {
    'Unknown': ['#AAAAAA', '#666666', '#000000', '#000000', '#000000'],
    'Unrated': ['#666666', '#2D2D2D', '#040202', '#040202', '#040202'],
    'Bronze': ['#F1F0F5', '#D0BCB0', '#B47F4E', '#522F15', '#A25B36'],
    'Silver': ['#F1F0F5', '#DAD3DE', '#ABA9AD', '#5F5865', '#7B7574'],
    'Gold': ['#F5F3F0', '#FDE7B4', '#FEBE70', '#F48554', '#FEBE70'],
    'Platinum': ['#F0F5F3', '#C4FAC6', '#5AF5AD', '#00C9C9', '#34E678'],
    'Diamond': ['#F1F0F5', '#D5E3FE', '#8EB9FF', '#384EC7', '#3F8EEA'],
    'Ruby': ['#F5F3F0', '#FCC6B8', '#FC849C', '#D93841', '#E15C64'],
    'Master': ['#F3F0F5', '#D6F7FD', '#E1C3FF', '#FC6297', '#CB7CEF'],
}

COLOR_COLD = {
    'Unknown': ['#AAAAAA', '#666666', '#000000', '#000000', '#000000'],
    'Unrated': ['#666666', '#2D2D2D', '#040202', '#040202', '#040202'],
    'Bronze': ['#F1F0F5', '#C6B7AE', '#A3805E', '#5D432F', '#A25B36'],
    'Silver': ['#F1F0F5', '#D3D3DE', '#A1A5B2', '#585865', '#5F606A'],
    'Gold': ['#F5F3F0', '#FFF2AC', '#FFD972', '#F5A03C', '#FDC456'],
    'Platinum': ['#F0F5F3', '#C6FDD9', '#5EF5C1', '#06CBE5', '#39E09D'],
    'Diamond': ['#F1F0F5', '#B4F8F8', '#4AC0F5', '#0065CB', '#1AC0F2'],
    'Ruby': ['#F5F3F0', '#FCDAE4', '#F793B2', '#E51062', '#DB306B'],
    'Master': ['#F3F0F5', '#CCFFFD', '#D5CBFF', '#FC62B5', '#CB7CEF'],
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