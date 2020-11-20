# string formatting
'hello' + 'world'
# 'hello world'

name = 'Alice'
place = 'Main Street'
time = '6 pm'
food = 'turnips'
'Hello ' + name + ', you are invited to a party at ' +
place + ' at ' + time + '. Please bring ' + food + '.'
# but this is too hard to read

'''Hello %s, you are invited to a party at %s at %s. Please
bring %s.''' % (name, place, time, food)
