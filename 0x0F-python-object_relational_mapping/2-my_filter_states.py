#!/usr/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8"
                            )
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}'".format(sys.argv[4]))
    query_rows = cur.fetchall()
    [print(state) for state in query_rows]
    cur.close()
    conn.close()
