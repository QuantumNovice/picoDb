from Database import *

class ui:
    def __init__(self):
        rec = record()
        db = database()
        print('Database')
        choice1 = input('(Quick create, Search, Create, Update, List)<< ')
        if choice1 == '0':
            name = input('Name < ')
            job = input('Job < ')
            employer = input('Employer < ')
            rec.upload(name=name, job=job, employer=employer)
            rec.save()
        elif choice1 == '1':
            choice2 = input('Paramter=Query < ')
            paramter, value = choice2.split('=')
            data = db.search(paramter, value)
            for i in data:
                rec.load(i)
                print('='*10)
                for i in rec.data:
                    print(i.capitalize(),':', rec.data[i])
                rec.save()
        elif choice1 == '2':
            choice2 = ''
            entry = {}
            while True:
                choice2 = input('Parameter=Value < ')
                if choice2 == 'x':
                    break
                parameter, value = choice2.split('=')
                entry[parameter] = value
            rec.uploadDict(entry)
            rec.save()
        elif choice1 == '3':
            pass
        elif choice1 == '4':
            names = db.list('name').keys()
            for i in range(len(names)):
                print(str(i)+')', list(names)[i])

            choice3 = input('<<<')
            if int(choice3) < len(names):
                print(rec.load())

if __name__ == '__main__':
    while True:
        ui()
##print(db().list('name'))
##print(db().search('name', 'john doe'))
##        
##d = record()
##d.upload(name='John Doe', job='S3cret', employer='Amazon')
##print(d.data)
##d.save()
##
##d.upload(name='John Oliver', job='S3cret', employer='Amazon')
##print(d.data)
##d.save()

