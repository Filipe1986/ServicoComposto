import psycopg2
from abc import ABC, abstractmethod


class DAO(ABC):
    @property
    def get_connection(self):
        con = psycopg2.connect(host='localhost', database='Restful',
                               user='postgres', password='admin')
        return con

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass


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
