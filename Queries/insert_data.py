import sqlite3
import pandas as pd
from connection import Connection
from query import Queries

conn_obj = sqlite3.connect('../safe-haven-detection.db')

conn = Connection(conn_obj).connect()

query = Queries(conn)
query.insert_data()
