from ..config.mysqlconnection import connectToMySQL

DATABASE = "users"

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.student = data['student']
        self.start_date = data['start_date']
        self.belt = data['belt']
        self.vag = data['vag']
        self.pen = data['pen']
        self.story = data['story']
        self.over = data['over']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojo;'
        results = connectToMySQL(DATABASE).query_db(query)
        return [cls(result) for result in results]

    @classmethod
    def save(cls):
        query = "INSERT INTO dojo (student, start_date, belt, vag, pen, story, over) values (%(student)s, %(start_date)s, %(belt)s, %(vag)s, %(pen)s, %(story)s, %(over)s);"
    @classmethod
    def get_one(cls, data:dict) -> object:
        query = 'SELECT * FROM dojo WHERE id = %(id)s;'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])
