from json import loads, dumps
DB_FILE = './db.json'


def db(method: str, field: str, value: str | int | None = None):
    if method == 'GET':
        try:
            with open(DB_FILE, 'r') as file:
                content = file.read()
                data = {} if len(content) < 1 else loads(content)

                response = 0

                if data[field] != None:
                    response = data[field]

                file.close()

                return response
        except:
            return 0
    elif method == 'SAVE':
        if value == None:
            return
        data = None
        with open(DB_FILE, 'a') as file:
            content = file.read()
            data = {} if len(content) < 1 else loads(content)

            data[field] = value

            file.close()
        with open(DB_FILE, 'w') as file:
            file.write(dumps(data))
            file.close()
        return
