import sys
from verify_cpf import verify_cpf
from generate_cpf import generate_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow
import design


class GenerateVerifyCPF(QMainWindow, design.Ui_MainWindow):
    """Representa um gerador e um validador de CPFs"""
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGenerateCPF.clicked.connect(self.generate_cpf)
        self.btnVerifyCPF.clicked.connect(self.verify_cpf)

    def generate_cpf(self):
        """Gera um CPF"""
        self.labelReturn.setText(
            str(generate_cpf())
        )

    def verify_cpf(self):
        """Valida um CPF"""
        cpf = self.inputVerifyCPF.text()

        self.labelReturn.setText(
            str(verify_cpf(cpf))
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gv_cpf = GenerateVerifyCPF()
    gv_cpf.show()
    qt.exec_()
