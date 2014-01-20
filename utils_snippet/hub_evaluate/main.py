
from ghost import Ghost

ghost = Ghost()
page, extra_resources = ghost.open("http://curriculum.hust.edu.cn/student_index.jsp")
print page
print ghost.content
