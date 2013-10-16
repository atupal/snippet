
import requests

import sys

url = 'http://bksjw.hust.edu.cn:80/reportServlet?action=18&file=student_personal_score_grade.raq&srcType=file&separator=%09&reportParamsId=103997&saveAsName=%7Cu534E%7Cu4E2D%7Cu79D1%7Cu6280%7Cu5927%7Cu5B66%7Cu62A5%7Cu8868&cachedId=A_14870&t_i_m_e=1374721017793'
print requests.get(url).content
