
callStack = []
callStack.append({'returnAddr':'start', 'number':5})
returnValue = None

while len(callStack) > 0:
	number = callStack[-1]['number']
	returnAddr = callStack[-1]['returnAddr']
	print(callStack)
	
	if returnAddr == 'start':
		if number == 1:
			returnValue = 1
			callStack.pop()
			continue
		else:
			callStack[-1]['returnAddr'] = 'after recursive call'
			callStack.append({'returnAddr':'start', 'number':number-1})
			continue
			
	elif returnAddr == 'after recursive call':
		returnValue = number * returnValue
		callStack.pop()
		continue
		
print(returnValue)

