
func HTMLEscapse(w io.Writer, b []byte) // 把b进行转义之后写到w
func HTMLEScapseString(s string) string // 转义s之后返回结果字符串
template.HTMLEscapse(w, []byte(r.Form.Get("username"))) // 输出到客户端
/*  
  import "text/template"
  ...
  t, err := template.New("foo").Parse(`{{define "T"}}Hello, {{.}}!{{end}}`)
  err = t.ExecuteTemplate(out, "T", "<script>alert("you have been pwned")</script>")
*/

