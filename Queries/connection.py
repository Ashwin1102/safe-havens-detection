import sqlite3
import pandas as pd

class Connection:
    def __init__(self, conn):
        self.conn = conn
    
    def connect(self):
        return self.conn
    
    