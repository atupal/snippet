<%
  x = db.get_resource('foo')
  y = [z.element for z in x if x.frobnizzle==5]
%>

% for elem in y:
  element: ${elem}
% endfor
