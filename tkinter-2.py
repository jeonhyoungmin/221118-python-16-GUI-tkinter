# tkinter-2.py
from tkinter import *

window = Tk()
window.title("HTML maker")
# * HTML의 <title> 역할을 하는 함수가 있는 것을 발견, 적용
window.geometry("300x300")
# * 특이하게 브라우저 창 사이즈도 개발자가 직접 지정할 수 있는 것 확인. 적용
window.resizable(True, True)
# * 브라우저는 기본값인 사이즈 조정 여부도 개발자가 직접 허용/불허 할 수 있음을 발견
label = Label(window, text="이게 무엇이지?")
#  * Label() 레이블이라는 클래스는 HTML <p>태그처럼 인터페이스 창에서 글씨를 쓸 때 사용하는 것을 발견
label.pack(side = "bottom")
# * pack()이라는 단어의 의미가 추론이 안되어 찾아보니 <HTML>의 display:block 비스무리한 역할을 하는 속성인 것을 유추 정도까지만 확인됨

window.mainloop()