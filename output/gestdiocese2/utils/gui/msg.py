from PyQt5.QtWidgets import QMessageBox

class msg:
    @staticmethod
    def show(txt="votre operation à été prise en compte", type="info"):
        dialog = QMessageBox()
        dialog.setText(txt)
        dialog.setWindowTitle("Message de confirmation")
        if type == "info":
            dialog.setIcon(QMessageBox.Information)
        elif type == "warn":
            dialog.setIcon(QMessageBox.Warning)
        elif type == "err":
            dialog.setIcon(QMessageBox.Critical)
        dialog.exec_()
