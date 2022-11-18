# tkinter-3.py
from tkinter import *

window = Tk()

basic_data_dict = {
  "title_name" : "HTML maker",
  "window_width" : 300,
  "window_height" : 300,
  "resizable_x" : True,
  "resizable_y" : True,
}

# * 기본 조건인데 리터럴인 것이 영 내키지 않아, 객체에 담아 관리하기로 결정
# * 객체에 담으면 객체만 제어하면 되므로 편함
# * 파이썬에서의 객체는 무엇이지?
# * 검색어: "파이썬 객체" o >>>>>>>>>>>>>>>>>> "tkinter 편하게 작성하는 법" x

window.title(basic_data_dict["title_name"])
geometry_value = str(basic_data_dict["window_width"]) + "x" + str(basic_data_dict["window_height"])
# * geometry_value 라는 변수로 만들어 넣기로 했는데 작성해보니 자바스크립트 메서드 방식으로 넣으면 더 편하겠다는 생각이 듦 -> 찾아보니 파이썬은 직접 딕셔너리에 추가하긴 어렵지만 class의 getter 개념이 존재하는 것을 확인
window.geometry(geometry_value)
window.resizable(basic_data_dict['resizable_x'], basic_data_dict["resizable_y"])
# ? 공통점 발견 : title, geometry, resizable 이 세 가지는 항상 사용해야 하는 것 아닌가??
# * 주안점 : 함수로 처리하면 편하겠다.

label = Label(window, text="이게 무엇이지?")
# ? text 매개변수는 디폴트 파라미터 방식으로 데이터를 받는 모양인데, 다르게 바꿀수도 있다는 뜻인가?
# * 주안점 : 앱 화면에서 작성해서 쌓인 데이터를 저 text 매개변수로 넣으면 되는 방법이 있을 것 같음

label.pack(side = "bottom")
# ? 마치 CSS top, bottom, left, right 같은 형태인 것으로 보이니까, 정밀하게 제어하는 방법도 존재할 것으로 예상

window.mainloop()