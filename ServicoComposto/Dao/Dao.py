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
        return cur.fetchall()

    def insert(self):
        con = self.get_connection
        cur = con.cursor()
        con.commit()
        cur.execute('insert into autor * FROM autor')
        autores = cur.fetchall()

    def update(self):
        pass

    def delete(self):
        pass


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
        con.commit()
        print('INSERT INTO publicacao(titulo) VALUES(\'' + titulo + ' \' )')
        cur.execute('INSERT INTO public.publicacao(titulo) VALUES(\'' + titulo + '\');')
        cur.close()
        con.close()

    def update(self):
        pass

    def delete(self):
        pass


class EdicaoDAO(DAO):
    def get(self):
        con = self.get_connection
        cur = con.cursor()
        con.commit()
        cur.execute('SELECT * FROM edicao')
        return cur.fetchall()

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class ForumDAO(DAO):
    def get(self):
        con = self.get_connection
        cur = con.cursor()
        con.commit()
        cur.execute('SELECT * FROM forum')
        return cur.fetchall()

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class LocalDAO(DAO):
    def get(self):
        con = self.get_connection
        cur = con.cursor()
        con.commit()
        cur.execute('SELECT * FROM local')
        return cur.fetchall()

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass