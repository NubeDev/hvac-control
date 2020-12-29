import datetime
import time

from hvac.temp_functions import current_temperature, current_humidity


def setHVACAndSendStatus():
    print('1', current_status)

    cool_switch = current_status['cool_switch']
    cool_temperature = current_status['cool_temperature']
    heat_switch = current_status['heat_switch']
    heat_temperature = current_status['heat_temperature']
    fan_switch = current_status['fan_switch']

    cool_status = 0
    heat_status = 0

    room_temperature = current_temperature()
    humidity = current_humidity()

    min_temp = 22
    max_temp = 23

    temp_buffer = 1

    if not in_temp_range(min_temp, max_temp, cool_temperature):
        cool_temperature = None

    if not in_temp_range(min_temp, max_temp, heat_temperature):
        heat_temperature = None

    if cool_switch == 1:
        if not in_temp_range(min_temp, max_temp, cool_temperature):
            print('Cool temperature out of range')
            cool_switch = 0
            cool_temperature = None
        else:
            if cool_switch == 1 and heat_switch == 1:
                cool_switch = 1
                heat_switch = 0

            if room_temperature > float(cool_temperature) + temp_buffer:
                cool_status = 1
                print('Room temperature too high. Cooling...')
            else:
                cool_status = 0
                print('Room temp cool, turning off cool.')
    else:
        cool_switch = 0
        print('cool switched off')

    if heat_switch == 1:
        if not in_temp_range(min_temp, max_temp, heat_temperature):
            print('Heat temp out of range')
            heat_switch = 0
            heat_temperature = None
        else:
            if cool_switch == 1 and heat_switch == 1:
                cool_switch = 0
                heat_switch = 1

            if room_temperature < float(heat_temperature) - temp_buffer:
                heat_status = 1
                print('Room temp too cold. Heating...')
            else:
                heat_status = 0
                print('Room temp warm. Turning off heat.')
    else:
        heat_switch = 0
        print('heat switched off')
    if fan_switch == 0:
        print('fan switched off')
    elif fan_switch == 1:
        print('fan switched on')

    if cool_switch == 0:
        print('Turn off cool')

    elif cool_switch == 1:
        print('Turn off heat')
        time.sleep(10)
        print('Turn on cool')

    if heat_switch == 0:
        print('Turn off heat')
    elif heat_switch == 1:
        print('Turn off coll')
        time.sleep(10)
        print('Turn on heat')

    current_status['cool_status'] = cool_status
    current_status['heat_status'] = heat_status
    print('2', current_status)  # for debugging
    print('================')


def in_temp_range(min_temp, max_temp, temperature):
    if temperature is None or temperature == '':
        return False

    if int(temperature) < min_temp or int(temperature) > max_temp:
        return False


if __name__ == '__main__':

    startup_status_dictionary = {}

    if not startup_status_dictionary:
        current_status = {
            'room_temperature': current_temperature(),
            'humidity': current_humidity(),
            'cool_switch': 0,
            'cool_status': 0,
            'cool_temperature': None,
            'heat_switch': 0,
            'heat_status': 0,
            'heat_temperature': None,
            'fan_switch': 0
        }
    else:
        current_status = {
            'room_temperature': startup_status_dictionary['room_temperature'],
            'humidity': startup_status_dictionary['humidity'],
            'cool_switch': startup_status_dictionary['cool_switch'],
            'cool_status': startup_status_dictionary['cool_status'],
            'cool_temperature': startup_status_dictionary['cool_temperature'],
            'heat_switch': startup_status_dictionary['heat_switch'],
            'heat_status': startup_status_dictionary['heat_status'],
            'heat_temperature': startup_status_dictionary['heat_temperature'],
            'fan_switch': startup_status_dictionary['fan_switch']
        }

    try:
        while True:
            preConnect = datetime.datetime.now()
            setHVACAndSendStatus()
            lastConnect = datetime.datetime.now()
            time.sleep(10)
    except (Exception, KeyboardInterrupt) as e:
        print("error")
        raise
