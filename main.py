import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt6 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)

        self.btnLogin.clicked.connect(self.check_login)

    def check_login(self):
        # Lấy thông tin email và mật khẩu từ người dùng
        email = self.txtEmail.text()
        password = self.txtPassword.text()
        
        # Kiểm tra email và mật khẩu có được nhập hay không
        if not email: 
            msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Vui lòng nhập mật khẩu!")
            msg_box.exec()
            return
        
        # Kiểm tra email và mật khẩu có khớp với tài khoản admin hay không
        if email == "admin@gmail.com" and password == "admin":
            # Nếu đăng nhập thành công, chuyển sang giao diện chính (Main)
            self.close()
            homePage.show()  
        else:
            # Nếu đăng nhập không thành công, hiển thị thông báo lỗi
            msg_box.setText("Email hoặc mật khẩu không đúng!")
            msg_box.exec()

class Home(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("home.ui", self)

        self.pushButton_3.clicked.connect(self.showMain)
    
    def showMain(self):
        mainPage.show()
        self.close()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

class NotFound(QMainWindow):
    def __init__(self):
        super(NotFound, self).__init__()
        pageName = "notFound.ui"
        uic.loadUi(pageName, self)
        
        self.btn_back.clicked.connect(self.showHome)
        
    def showHome(self):
        homePage.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    homePage = Home()
    mainPage = Main()

    window = MainWindow()
    window.show()

    msg_box = QMessageBox()
    msg_box.setWindowTitle("Lỗi")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")

    app.exec()