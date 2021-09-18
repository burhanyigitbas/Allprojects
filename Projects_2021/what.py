import pywhatkit as py

import optparse

parse = optparse.OptionParser()

parse.add_option("--number",dest="number",help="--number")
parse.add_option("--message",dest="message",help="--message")
parse.add_option("--hour",dest="hour",help="--hour")
parse.add_option("--minute",dest="minute",help="--minute")

(user_inputs,arguments) = parse.parse_args()

user_number = user_inputs.number

user_message = user_inputs.message

user_hour = user_inputs.hour

user_minute = user_inputs.minute

user_hour = int(user_hour)
user_minute = int(user_minute)


py.sendwhatmsg(user_number,user_message,user_hour,user_minute)