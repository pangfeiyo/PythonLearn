'''一个代表餐馆的班级'''
class Restaurant():
    '''一个代表餐馆的班级'''
    def __init__(self, name, cuisine_type):
        '''初始化餐厅'''
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def describe_restaurant(self):
        '''显示餐厅的摘要'''
        msg = self.name + " serves wonderful" + self.cuisine_type +"."
        print("\n"+ msg)
    def open_restaurant(self):
        '''显示餐厅开门的信息'''
        msg = self.name + " is open. Come on in!"
        print("\n" + msg)
    def set_number_served(self, number_served):
        '''允许用户设置已送达的客户数'''
        self.number_served = number_served
    def increment_number_served(self, additional_served):
        '''允许用户增加服务的客户数'''
        self.number_served += additional_served



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


class Admin(User):
    """具有管理员特权的用户"""

    def __init__(self, first_name, last_name, username, email, location):
        """初始化管理员"""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        # 初始化一组空的权限   谷歌直翻
        #将一个privileges 实例用作其属性
        self.privileges = Privileges()

class Privileges():
    """存储管理员权限的类"""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("- This user has no privileges.")
