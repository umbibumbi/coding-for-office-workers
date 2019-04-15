#Article class with __init__

class Article:
    author = "은비"
    view_count = 0

#***클래스에서 만드는 함수에는 self 변수가 필수
    def __init__(self, title, content):
        self.title = title #클래스의 변수에 접근하기 위해 꼭 self. 을 적어야한다.
        self.content = content

    def read(self):
        self.view_count = self.view_count + 1

article1 = Article("개발", "개발은 쉬워요")
article2 = Article("코딩", "코딩은 쉬워요")


print(article1.view_count)
article1.read()  #불러와서 읽음
print(article1.view_count)
