
import messagebird
client = messagebird.Client('<>')
try:
    msg =  client.voice_message_create('+917775980613','Hey Love',{'voice':'male'})
    print(msg.__dict__)
except messagebird.client.ErrorException as e:
    for error in e.errors:
        print(error)