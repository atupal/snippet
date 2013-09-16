<%!
  import mylib
  import re

  def filter(text):
    return re.sub(r"^@", '', text)
%>
