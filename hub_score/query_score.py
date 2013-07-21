import json


id_set = set()

def score_grade(ID):
  with open('./score_grade.json', 'r') as fi:
    score = json.loads("["  +  fi.read().strip().strip(',').strip('\n').strip(',')  +  "]" )
    for s in score:
      for ss in s:
        if str(ss) == str(ID):
          print s[ss]
          return

def score_all(ID):
  with open('./score.json', 'r') as fi:
    score = json.loads("["  +  fi.read().strip().strip(',').strip('\n').strip(',')  +  "]" )
    for s in score:
      for ss in s:
        if str(ss) == str(ID):
          print s[ss]
          return

def update_id():
  with open('./score_grade.json', 'r') as fi:
    score = json.loads("["  +  fi.read().strip().strip(',').strip('\n').strip(',')  +  "]" )
    for s in score:
      for ss in s:
        id_set.add(str(ss))

    print 'crawler count: %d' % len(id_set)

if __name__ == "__main__":
  #score_all(201117460)
  update_id()
  import sys
  score_grade(sys.argv[1])
  #score_grade(201015958)
