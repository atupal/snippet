#include "util.h"
#include "slp.h"
#include "prog1.h"

#define DEBUG 0

typedef struct table *Table_;
struct table {
  string id;
  int value;
  Table_ tail;
};

Table_ Table(string id, int value, struct table *tail) {
  Table_ t = (Table_)malloc (sizeof(*t));
  t->id = id;
  t->value = value;
  t->tail = tail;
  return t;
}

Table_ interpStm(A_stm s, Table_ t);
Table_ update(Table_, string, int);
int lookup(Table_ t, string key);

typedef struct intAndTalbe{
  int i;
  Table_ t;
} IntAndTable_;

IntAndTable_ IntAndTable(int i, Table_ t) {
  IntAndTable_ it;
  it.i = i;
  it.t = t;
  return it;
}

IntAndTable_ interpExp(A_exp e, Table_ t);
Table_ printStm(A_expList, Table_ t);
IntAndTable_ opExp(A_exp, A_binop, A_exp, Table_);
