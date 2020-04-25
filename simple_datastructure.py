storage = {}
storage['first'] = {}
storage['middle'] = {}
storage['last'] = {}

me = 'Magnus Lie Hetland'
storage['first']['Magnus'] = [me]
storage['middle']['Lie'] = [me]
storage['last']['Hetland'] = [me]


my_sister = 'Anne Lie Hetland'
storage['first'].setdefault('Anne', []).append(my_sister)
storage['middle'].setdefault('Lie', []).append(my_sister)
storage['last'].setdefault('Hetland', []).append(my_sister)


def lookup(data,label,name):
    return data[label].get(name)


def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def store(data, full_name):
    names = full_name.split()
    if len(names) ==2: names.insert(1,'')
    labels = 'first', 'middle', 'last'
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


MyNames = {}
init(MyNames)
store(MyNames, 'Hung Lie Hetland')
print (lookup(MyNames, 'middle', 'Lie'))

store(MyNames, 'Robin Hood')
store(MyNames, 'Robin Locksley')
store(MyNames, 'Mr. Gumby')

print(lookup(MyNames, 'first', 'Robin'))
print(lookup(MyNames, 'middle', ''))
