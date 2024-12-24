import sys
import UI
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QTimer
from random import randint

class Game(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = UI.Ui_Dialog()
        self.ui.setupUi(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTimer)
        self.current_answers = []

    def startTimer(self):
        self.time = 0
        self.ui.Timer.setText("000.000")
        self.timer.start(1)

    def updateTimer(self):
        self.time += 0.001
        self.ui.Timer.setText('{:03.3f}'.format(self.time))

    def getProblem(self):
        fdict = {
            0: '+',
            1: '-',
            2: '*',
            3: '/'
        }
        problem = ''
        answer = []
        for _ in range(10):
            c = randint(0, 3)
            a, b, ans = 0, 0, 0
            if c == 3:  # 确保除法的结果为整数
                b = randint(1, 100)
                ans = randint(1, b)
                a = b * ans
            else:
                a = randint(1, 100)
                b = randint(1, 100)
                if c == 0:
                    ans = a + b
                elif c == 1:
                    ans = a - b
                elif c == 2:
                    ans = a * b
            answer.append(ans)
            problem += '{} {} {} = ???\n'.format(a, fdict[c], b)
        return answer, problem

    def layProblem(self):
        self.current_answers, problem = self.getProblem()  # 获取问题和答案
        self.ui.Question.setText(problem)
        self.startTimer()

    def checkAnswers(self):
        self.timer.stop()
        answer_text = self.ui.Answer.toPlainText()
        answers = answer_text.splitlines()
        answers += ['?'] * (10 - len(answers))
        out = ''
        for i, a in enumerate(answers):
            if a == str(self.current_answers[i]):
                out += '对了，牢弟！\n'
            else:
                out += '错了QAQ，正确答案是: {} \n'.format(self.current_answers[i])
        self.ui.Answer.clear()
        self.ui.Answer.append(out)

    def clear(self):
        self.ui.Question.clear()
        self.ui.Answer.clear()
        self.ui.Timer.setText("")
        self.timer.stop()

    def showName(self):
        message = "谢谢赏光，如果深夜一个人睡不着请发邮件给24yhhuang2@stu.edu.cn 我是个负责任的男人[玫瑰][玫瑰]"
        self.clear()
        self.ui.Timer.setText(message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Dlg = Game()
    Dlg.show()
    sys.exit(app.exec_())