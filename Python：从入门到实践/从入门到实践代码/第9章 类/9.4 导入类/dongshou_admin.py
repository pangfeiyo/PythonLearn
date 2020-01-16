from dongshou_user import User

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

