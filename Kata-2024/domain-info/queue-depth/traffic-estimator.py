from collections import namedtuple

# name is the signal name
# ticks_500ms is how many 500ms ticks go by before the signal fires
Signal = namedtuple('Signal', 'name ticks_500ms')

signals = [
    # 1 per 500ms
    Signal('heart_rate', 1),
    # 1 per hr: 2 per second to minutes to hours
    Signal('blood_pressure', 2 * 60 * 60),
    # 1 per 5s: 2 per second to 5 seconds
    Signal('oxygen_level', 2 * 5),
    # 1 per 5s: 2 per second to 5 seconds
    Signal('blood_sugar', 2 * 5),
    # 1 per 1s: 2 per second
    Signal('respiration', 2),
    # 1 per 1s: 2 per second
    Signal('ecg', 2),
    # 1 per 5min: 2 per second to minutes to 5 minutes
    Signal('body_temp', 2 * 60 * 5),
    # 1 per 2min: 2 per second to minutes to 2 minutes
    Signal('sleep_status', 2 * 60 * 2),
]

# simulate 65 minutes: 2 ticks per second to minutes
ticks = 2 * 60 * 65

# how many sets of signals
num_sets = 500

for tick in range(0, ticks):
    active_signals = [x for x in signals if tick % x.ticks_500ms == 0]
    signal_names = " ".join(x.name for x in active_signals)
    print("%s,%s,%s" % (tick, num_sets * len(active_signals), signal_names))
