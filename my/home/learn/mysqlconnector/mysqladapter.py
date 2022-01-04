import configparser
from mysql import connector

from my.home.learn.mysqlconnector.setProperties import Properties


class ConnectMySql:
    @staticmethod
    def create_connection():
        parser = configparser.ConfigParser()
        parser.read("C:\\Users\\vhs_s\\PycharmProjects\\py_learn\\properties.properties")
        env_name = parser.get("parameters", "db.name")
        env_pass = parser.get("parameters", "db.pass")
        env_username = parser.get("parameters", "db.user")
        env_addr = parser.get("parameters", "db.address")
        connection = connector.connect(user=env_username, password=env_pass,
                                       host=env_addr,
                                       database=env_name)
        return connection


ConnectMySql.create_connection()
