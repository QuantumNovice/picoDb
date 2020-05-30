import pickle, hashlib, os

class record:
    def __init__(self):
        self.data = {}
        self.filename = ''
        
    def upload(self, **kwargs):
        self.data = kwargs

    def uploadDict(self, dictionary):
        self.data = dictionary
        
    def dataHash(self):
        obj = ''
        for i in self.data:
            obj += self.data[i]
        self.filename = str(hashlib.sha512(obj.encode()).hexdigest())

    def save(self):
        self.dataHash()
        if self.filename != '':
            fd = open('records/'+self.filename+'.pkl', 'wb')
            pickle.dump(self.data, fd)
            fd.close()
            
    def load(self, filename):
        fd = open('records/'+filename, 'rb')
        self.data = pickle.load(fd)
        fd.close()
        os.remove('records/'+filename)

    def update(self, **kwargs):
        for key in kwargs:
            self.data[key] = kwargs[key]

class database:
    def list(self, parameter):
        parameters = {}
        for i in os.listdir('records'):
            fd = open('records/'+i, 'rb')
            data = pickle.load(fd)
            fd.close()
            parameters[ data[parameter] ] = i
        return parameters

    def search(self, parameter, value):
        result = []
        for i in os.listdir('records'):
            fd = open('records/'+i, 'rb')
            data = pickle.load(fd)
            fd.close()
            value = value.lower()
            if data[parameter].lower() == value:
                result.append(i)
        return result

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

