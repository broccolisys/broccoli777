import sqlite3

# 메모리에 SQLite3 데이터베이스를 만든다
# 네 가지 속성을 지닌 Sales 테이블을 만든다

con = sqlite3.connect(':memory:')

"""" ": memory :"를 사용하여 디스크 대신 RAM에있는 데이터베이
스에 대한 데이터베이스 연결을 열 수 있습니다. 데이터베이스가 성
공적으로 열리면 연결 개체가 반환됩니다."""

query = """CREATE TABLE sales
            (customer VARCHAR(20),
            product VARCHAR(40),
            amount FLOAT,
            date DATE);"""
con.execute(query)
# execute() SQL문 실행
con.commit()
# 트랜직션을 실행(db에 저장되는 것)

# sales 테이블에 데이터를 삽입한다
data = [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
        ('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
        ('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
        ('Stephen Randolph', 'Computer', 679.40, '2014-02-20')]

statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
con.executemany(statement, data)
# 안에 내용이 다양하게 있을 경우 execuemany 를 씀
con.commit()

# sales 테이블에 질의한다.
cursor = con.execute("SELECT *FROM sales")
rows = cursor.fetchall()
# 레코드 조회 : fetchall()

# 출력된 데이터의 수를 센다
row_counter = 0
for row in rows:
    print(row)
    row_counter += 1
print('Number of rows: {}'.format(row_counter))