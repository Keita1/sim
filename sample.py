# sample simulation file.
# loads directly instead of through io.py

config = {
    'pal_len': 12,  # PL
    'num_pallets': 15,  # NP
    'conv_name':  'mainline',
    'conv_len': 70,
    'conv_spd': 60,
    'stations': [
        {
        'sta_num': 1,
        'sta_pos': 12,
        'sta_cycle_time': 5,
        'sta_type': 1
        },
        {
        'sta_num': 2,
        'sta_pos': 24,
        'sta_cycle_time': 5,
        'sta_type': 1
        },
        {
        'sta_num': 3,
        'sta_pos': 36,
        'sta_cycle_time': 5,
        'sta_type': 6
        },
        {
        'sta_num': 4,
        'sta_pos': 48,
        'sta_cycle_time': 5,
        'sta_type': 3
        },
        {
        'sta_num': 5,
        'sta_pos': 60,
        'sta_cycle_time': 5,
        'sta_type': 2
        }
    ]
}
