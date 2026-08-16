class User:
    def __init__(self, id="", level=0):
        self.id = id
        self.level = level

user1 = User("codetree", 10)
user2 = User()
id2, level2 = tuple(input().split())
user2.id = id2
user2.level = level2

print(f"user {user1.id} lv {user1.level}")
print(f"user {user2.id} lv {user2.level}")
