class query_handler(object):
    def auth(self, username, password):
        query = f" exec dbo.Valid_User '{username}', '{password}' "
        return query

    def insert(self, name, phone_number):
        query = f" exec dbo.Insert_Data '{name}', '{phone_number}' "
        return query

    def get_all(self):
        query = f" exec dbo.Get_All_Data "
        return query

    def get_by_id(self, id):
        query = f" exec Get_Data_By_Id {id} "
        return query

    def update(self, name, phone_number, id):
        query = f" exec Update_Data '{name}', '{phone_number}', {id} "
        return query

    def delete(self, id):
        query = f" exec Delete_Data {id} "
        return query
