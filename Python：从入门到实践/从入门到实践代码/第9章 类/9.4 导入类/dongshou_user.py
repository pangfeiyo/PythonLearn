'''用于建模用户的类集合'''
class User():
    """表示简单的用户配置文件"""

    def __init__(self, first_name, last_name, username, email, location):
        """初始化用户"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """显示用户信息的摘要"""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """向用户显示个性化的问候语"""
        print("\nWelcome back, " + self.username + "!")

    def increment_login_attempts(self):
        """login_attempts 增量值"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """login_attempts 归0"""
        self.login_attempts = 0

