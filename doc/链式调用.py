class QueryBuilder:
    """链式调用是一种编程模式，允许我们在单个表达式中通过连续调用同一个对象的多个方法来执行一系列操作。这种模式通过方法在完成自己的操作后返回对象本身
    （通常是通过返回 self）来实现。链式调用的目的是提高代码的可读性和简洁性，使代码更加流畅。"""
    def __init__(self):
        self.query = ""

    def select(self, fields):
        self.query += "SELECT " + fields + " "
        return self

    def from_table(self, table_name):
        self.query += "FROM " + table_name + " "
        return self

    def where(self, condition):
        self.query += "WHERE " + condition + " "
        return self

    def get_query(self):
        return self.query


# 使用链式调用构建查询
query = (QueryBuilder()
         .select("*")
         .from_table("users")
         .where("age > 18")
         .get_query())

print(query)  # 输出：SELECT * FROM users WHERE age > 18