# Class inheritance 상속
class Article:
    author = "은비"
    view_count = 0

#클래스에서 만드는 함수에는 self 변수가 필수
    def __init__(self, title, content):
        self.title = title #클래스의 변수에 접근하기 위해 꼭 self. 을 적어야한다.
        self.content = content

    def read(self):
        self.view_count = self.view_count + 1

article1 = Article("개발", "개발은 쉬워요")
article2 = Article("코딩", "코딩은 쉬워요")

class BrunchArticle(Article): #Article 클래스를 상속
    source = "브런치"

    def read(self):
        self.view_count = self.view_count + 2 #기존 함수 Override

brunch_article = BrunchArticle("개발", "개발은 쉬워요") #instance 를 만든다
print(brunch_article.content)
print(brunch_article.source)
print(brunch_article.view_count)
brunch_article.read()
print(brunch_article.view_count)
