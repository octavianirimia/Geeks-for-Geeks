"""
Given a string s represents time in 24-hour format ("HH:MM"), determine the minimum angle between the hour and minute hands of an analog clock.

The minute hand moves 6° per minute, while the hour hand moves 0.5° per minute.
Thus, the hour hand's angle is calculated as hrAngle = 30 x H + 0.5 x M, and the minute hand's angle as minAngle = 6 x M.
The difference between the two angles is diff = |hrAngle - minAngle|.
"""

def get_angle(hour_string: str) -> float:
    hour = int(hour_string[:2])
    minute = int(hour_string[3:])

    # The analog clock is in 12h format so we can calculate the angle until 12
    hour %= 12

    hour_angle = 30 * hour + 0.5 * minute
    minute_angle = 6 * minute

    angle = abs(hour_angle - minute_angle)

    return min(360 - angle, angle)


if __name__ == "__main__":
    print(f"{get_angle("03:15"):.3f}")
