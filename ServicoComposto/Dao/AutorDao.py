from Dao.Dao import DAO


class AuthorDAO(DAO):
    def get(self):
        con = self.get_connection
        cur = con.cursor()
        con.commit()
        cur.execute('SELECT * FROM autor')
        autores = cur.fetchall()
        return autores

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
