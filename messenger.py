from datetime import datetime
import requests

from PyQt6 import QtWidgets, QtCore

import ui


class ExampleApp(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, host='http://178.250.157.243:5000'):
        super().__init__()
        self.setupUi(self)
        
        self.host = host

        self.pushButton.pressed.connect(self.send_message)

        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.timer.start(1000)

    def show_messages(self, messages):
        for message in messages:
            dt = datetime.fromtimestamp(message['time']).strftime('%H:%M')
            self.textBroswer.append(dt + ' ' + message['name'])
            self.textBrowser.append(message['text'])
            self.textBrowser.append('')

    def get_messages(self):
        try:
            response = requests.get(self.host + '/messages', params={'after': self.after})
        except:
            return

        messages = response.json()['messages']
        if len(messages) > 0:
            self.show_messages(messages)
            self.after = messages[-1]['time']

    def send_message(self):
        name = self.lineEdit.text()
        text = self.textEdit.toPlainText()

        try:
            response = requests.post(self.host + '/send', json={'name': name, 'text': text})
        except:
            self.textBrowser.append('Serever is not avalible')
            self.textBrowser.append('')
            return
        
        if response.status_code != 200:
            self.textBrowser.append('message not send')
            self.textBrowser.append('')

        self.textEdit.clear()


app = QtWidgets.QApplication([])
window = ExampleApp()
window.show()
app.exec()