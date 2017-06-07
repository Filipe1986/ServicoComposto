from Dao.Dao import DAO


class PublicacaoDAO(DAO):
    def get(self):
        con = self.get_connection
        cur = con.cursor()
        con.commit()
        cur.execute('SELECT * FROM publicacao')
        return cur.fetchall()

    def insert(self, titulo):
        con = self.get_connection
        cur = con.cursor()
        print("""INSERT INTO publicacao(titulo) VALUES (%s);""",titulo)
        cur.execute("""INSERT INTO publicacao(titulo) VALUES (%s);""", (titulo,))
        con.commit()
        cur.close()
        con.close()

    def update(self):
        pass

    def delete(self):
        pass
