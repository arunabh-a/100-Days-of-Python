class user:
    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user1 = user("001", "James")
user2 = user("002", "Brad")
print(user1.followers)
print(user2.followers)

user1.follow(user2)
print(user1.follow)
print(user2.followers)