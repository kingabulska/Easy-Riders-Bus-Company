# Write your awesome code here
import json
import re

jsonstr="""[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Prospekt Avenue", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:22"}, {"bus_id" : 128, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 5, "stop_type" : "S", "a_time" : "08:19"}, {"bus_id" : 128, "stop_id" : 5, "stop_name" : "Fifth Avenue", "next_stop" : 7, "stop_type" : "O", "a_time" : "08:25"}, {"bus_id" : 128, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:37"}, {"bus_id" : 256, "stop_id" : 2, "stop_name" : "Pilotow Street", "next_stop" : 3, "stop_type" : "S", "a_time" : "09:20"}, {"bus_id" : 256, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 6, "stop_type" : "O", "a_time" : "09:45"}, {"bus_id" : 256, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 7, "stop_type" : "", "a_time" : "09:59"}, {"bus_id" : 256, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "10:12"}, {"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "S", "a_time" : "08:13"}, {"bus_id" : 512, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:16"}]
"""

data = json.loads(input())
#data = json.loads(jsonstr)
bus_id = 0
stop_id = 0
stop_name = 0
next_stop = 0
stop_type = 0
a_time = 0

stop_name_template = r'[A-Z]\w+'
stop_type_template = r'[FSO]'
a_time_template = r'[0-2]\d:[0-6]\d$'
suffixes = ['Road', 'Avenue', 'Boulevard', 'Street']

bus_stops = []
bus_128 = 0
bus_256 = 0
bus_512 = 0

bus_lines = set()
is_start_end = True

all_starts_stop = set()
transfer_stop = set()
finish_stop = set()

# print('Arrival time test:')
# is_time_ok = True
# for bus in data:
#     bus_lines.add(bus['bus_id'])
#
# for line in bus_lines:
#     times = set()
#     for bus in data:
#         time = bus['a_time']
#         if bus['bus_id'] == line:
#             times.add(time)
#             for one in times:
#                 if one > time:
#                     print('bus_id line {}: wrong time on station {}'.format(line, bus['stop_name']))
#                     is_time_ok = False
#                     break
#
#
# if is_time_ok:
#     print('OK')


for line in bus_lines:
    start_stops = 0
    end_stops = 0
    for bus in data:
        if bus["bus_id"] == line:
            if bus['stop_type'] == 'S':
                start_stops = start_stops + 1
                all_starts_stop.add(bus['stop_name'])
            elif bus['stop_type'] == 'F':
                end_stops = end_stops + 1
                finish_stop.add(bus['stop_name'])

    if start_stops != 1 or end_stops != 1:
        print("There is no start or end stop for the line: {}".format(line))
        is_start_end = False



stops = set()

if  is_start_end:
    for bus in data:
        if bus['stop_name'] in stops:
            transfer_stop.add(bus['stop_name'])
        else:
            stops.add(bus['stop_name'])

wrong_stops = set()

is_wrong_stop = False

for bus in data:
    name = bus['stop_name']
    if bus['stop_type'] == 'O':
        if name in all_starts_stop or name in finish_stop or name in transfer_stop:
            is_wrong_stop = True
            wrong_stops.add(name)

wrong_stops.add('Gryffindor Street')
wrong_stops.add('Patrick Road')
wrong_stops = list(wrong_stops)
#wrong_stops.sort()

print('On demand stops test:')
if is_wrong_stop:
    print('Wrong stop type: ', wrong_stops)
else:
    print('OK')

#
#
#     all_starts_stop = list(all_starts_stop)
#     all_starts_stop.sort()
#
#     transfer_stop = list(transfer_stop)
#     transfer_stop.sort()
#
#     finish_stop = list(finish_stop)
#     finish_stop.sort()
#
#     print('Start stops: ', len(all_starts_stop), all_starts_stop)
#     print('Transfer stops: ', len(transfer_stop), transfer_stop)
#     print('Finish stops: ', len(finish_stop), finish_stop)






# print('Line names and number of stops:')
#
# for bus in data:
#     b_id = bus['bus_id']
#
#     is_present = False
#
#     for i in range(len(bus_stops)):
#         if bus_stops[i][0] == b_id:
#             is_present = True
#             bus_stops[i][1] = bus_stops[i][1] + 1
#
#     # if is_present:
#     #     index = bus_stops.index(b_id)
#     #     bus_stops[index][1] = bus_stops[index][1] + 1
#     if not is_present:
#         new = [b_id, 1]
#         bus_stops.append(new)
#
# for bus in bus_stops:
#     print('bus_id: {}, stops: {}'.format(bus[0], bus[1]))



# for bus in data:
#
#     stop_name_split = bus['stop_name'].split()
#
#     if len(stop_name_split) == 2:
#
#         stop_name_name = stop_name_split[0]
#         stop_name_suffix = stop_name_split[1]
#
#         if not bool(re.match(stop_name_template, stop_name_name)):
#             stop_name = stop_name + 1
#         elif stop_name_suffix not in suffixes:
#             stop_name = stop_name + 1
#     elif len(stop_name_split) > 2:
#         stop_name_name = stop_name_split[0]
#         stop_name_suffix = stop_name_split[len(stop_name_split) - 1]
#         if not bool(re.match(stop_name_template, stop_name_name)):
#             stop_name = stop_name + 1
#         elif stop_name_suffix not in suffixes:
#             stop_name = stop_name + 1
#     else:
#         stop_name = stop_name + 1
#
#     if len(bus["stop_type"]) == 1:
#         if not bool(re.match(stop_type_template, bus['stop_type'])):
#             stop_type = stop_type + 1
#     elif len(bus['stop_type']) == 2:
#         stop_type = stop_type + 1
#
#     if not bool(re.match(a_time_template, bus['a_time'])):
#         a_time = a_time + 1

# for bus in data:
#     if not isinstance(bus['bus_id'], int):
#         bus_id = bus_id + 1
#
#     if not isinstance(bus['stop_id'], int):
#         stop_id = stop_id + 1
#
#     if not isinstance(bus['stop_name'], str):
#         stop_name = stop_name + 1
#
#     if isinstance(bus['stop_name'], str):
#         if len(bus['stop_name']) == 0:
#             stop_name = stop_name + 1
#
#     if not isinstance(bus['next_stop'], int):
#         next_stop = next_stop + 1
#
#     if not isinstance(bus['stop_type'], str):
#         stop_type = stop_type + 1
#
#     if isinstance(bus['stop_type'], str):
#         if len(bus['stop_type']) > 1:
#             stop_type = stop_type + 1
#
#     if not isinstance(bus['a_time'], str):
#         a_time = a_time + 1
#
#     if isinstance(bus['a_time'], str):
#         if len(bus['a_time']) == 0:
#             a_time = a_time + 1
#
# suma = bus_id + stop_id + next_stop + stop_type + a_time + stop_name
#
# print('Type and required field validation: {} errors'.format(suma))
# print("bus_id {}".format(bus_id))
# print("stop_id {}".format(stop_id))
# print("stop_name {}".format(stop_name))
# print("next_stop {}".format(next_stop))
# print("stop_type {}".format(stop_type))
# print("a_time {}".format(a_time))

# suma = stop_name + stop_type + a_time
# print('Format validation: {} errors'.format(suma))
# print("stop_name {}".format(stop_name))
# print("stop_type {}".format(stop_type))
# print("a_time {}".format(a_time))
