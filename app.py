import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from selenium import webdriver

# Classe da thread que executa a automação
class AutomationThread(QThread):
    progress_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._stop_flag = False

    def run(self):
        self._stop_flag = False
        # Iniciando o WebDriver do Selenium (exemplo com Chrome)
        self.driver = webdriver.Chrome()

        try:
            while not self._stop_flag:
                # Exemplo de automação: abrir o Google e pesquisar algo
                self.progress_signal.emit("Abrindo o Google...")
                self.driver.get("https://www.google.com")
                time.sleep(2)  # Simulação de tempo de carregamento

                search_box = self.driver.find_element("name", "q")
                search_box.send_keys("PyQt5 Selenium")
                search_box.submit()

                self.progress_signal.emit("Pesquisa realizada.")
                time.sleep(5)  # Simula espera para visualização

        except Exception as e:
            self.progress_signal.emit(f"Erro: {str(e)}")

        finally:
            self.driver.quit()

    def stop(self):
        self._stop_flag = True
        self.progress_signal.emit("Automação interrompida.")

# Classe da interface gráfica
class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configuração da janela
        self.setWindowTitle('Automação com Selenium e PyQt5')
        self.setGeometry(100, 100, 300, 200)

        # Layout
        self.layout = QVBoxLayout()

        # Botão para iniciar a automação
        self.start_button = QPushButton('Iniciar Automação', self)
        self.start_button.clicked.connect(self.start_automation)
        self.layout.addWidget(self.start_button)

        # Botão para parar a automação
        self.stop_button = QPushButton('Parar Automação', self)
        self.stop_button.clicked.connect(self.stop_automation)
        self.layout.addWidget(self.stop_button)

        # Label para mostrar o status da automação
        self.status_label = QLabel('Status: Pronto', self)
        self.layout.addWidget(self.status_label)

        self.setLayout(self.layout)

        # Instancia a thread da automação
        self.thread = AutomationThread()
        self.thread.progress_signal.connect(self.update_status)

    # Método para iniciar a automação
    @pyqtSlot()
    def start_automation(self):
        if not self.thread.isRunning():
            self.status_label.setText("Status: Iniciando automação...")
            self.thread.start()

    # Método para parar a automação
    @pyqtSlot()
    def stop_automation(self):
        if self.thread.isRunning():
            self.thread.stop()

    # Método para atualizar o status na interface
    @pyqtSlot(str)
    def update_status(self, message):
        self.status_label.setText(f"Status: {message}")

# Executa a aplicação
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())
