
//必填字段
if len(r.Form["username"][0]) == 0 {

}


// 数字

getint ,err := strconv.Atoi(r.Form.Get("age"))
if err != nil {

}

if m, _ := regexp.MatchString("^[0-9]+$", r.Form.Get("age")); !m {
  return false
}

// 中文

if m, _ := regexp.MatchString("^[\\x{4e00}-\\x{9fa5}]+$", r.Form.Get("realname")); !m {
  return false
}
