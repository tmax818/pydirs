from ..config.mysqlconnection import connectToMySQL


DATABASE = "schema_name"

class table_name:
    def __init__(self, data):
        self.id = data["id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM table_name;"
        results = connectToMySQL("first_flask").query_db(query)
        # items = []
        # for item in results:
        #     items.append(cls(item))
        # return items
        return [cls(result) for result in results]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO table_name (param1, param2) values (%(param1)s, %(param2)s);"
        table_name_id = connectToMySQL(DATABASE).query_db(query, data)
        return table_name_id

    @classmethod
    def get_one(cls, data:dict) -> object:
        query = "SELECT * FROM table_name WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE table_name SET col_one=%()s,col_two=%()s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM table_name WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
