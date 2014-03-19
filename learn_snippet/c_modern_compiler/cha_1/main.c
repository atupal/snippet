#include "main.h"

Table_ t1, t2;
IntAndTable_ it1, it2;

Table_ interpStm(A_stm s, Table_ t) {
  switch (s->kind) {
    case A_compoundStm:
      if (DEBUG) printf("A_compoundStm\n");
      t1 = interpStm(s->u.compound.stm1, t);
      t2 = interpStm(s->u.compound.stm2, t1);
      return t2;
      break;
    case A_assignStm:
      if (DEBUG) printf("A_assignStm\n");
      it1 = interpExp(s->u.assign.exp, t);
      t2 = Table(s->u.assign.id, it1.i, it1.t);
      return t2;
      break;
    case A_printStm:
      if (DEBUG) printf("A_printStm\n");
      return printStm(s->u.print.exps, t);
      break;
    default:
      printf("no match in interpStm!\n");
      exit(1);
  }
}

IntAndTable_ interpExp(A_exp e, Table_ t) {
  switch (e->kind) {
    case A_idExp:
      t1 = t;
      while (t1) {
        if (strcmp(t1->id, e->u.id) == 0) {
          return IntAndTable(t1->value, t);
        }
        t1 = t1->tail;
      }
      printf("not find the id!\n");
      exit(1);
      break;
    case A_numExp:
      return IntAndTable(e->u.num, t);
      break;
    case A_opExp:
      return opExp(e->u.op.left, e->u.op.oper, e->u.op.right, t);
      break;
    case A_eseqExp:
      t1 = interpStm(e->u.eseq.stm, t);
      it1 = interpExp(e->u.eseq.exp, t1);
      return it1;
      break;
    default:
      printf("no match in interpExp!\n");
      exit(1);
  }
}

Table_ printStm(A_expList exps, Table_ t) {
  switch (exps->kind) {
    case A_pairExpList:
      it1 = interpExp(exps->u.pair.head, t);
      printf("%d ", it1.i);
      return printStm(exps->u.pair.tail, it1.t);
      break;
    case A_lastExpList:
      it1 = interpExp(exps->u.last, t);
      printf("%d\n", it1.i);
      return it1.t;
      break;
    default:
      printf("no match in printStm!\n");
      exit(1);
  }
}

IntAndTable_ opExp(A_exp left, A_binop oper, A_exp right, Table_ t) {
  it1 = interpExp(left, t);
  it2 = interpExp(right, it1.t);
  switch (oper) {
    case A_plus:
      return IntAndTable(it1.i + it2.i, it2.t);
      break;
    case A_minus:
      return IntAndTable(it1.i - it2.i, it2.t);
      break;
    case A_times:
      return IntAndTable(it1.i * it2.i, it2.t);
      break;
    case A_div:
      return IntAndTable(it1.i / it2.i, it2.t);
      break;
    default:
      printf("no match in opExp!\n");
      exit(1);
  }
}

int main() {
  A_stm s = prog();
  Table_ t = interpStm(s, NULL);
  /*
  while (t) {
    printf("%s:%d -> ", t->id, t->value);
    t = t->tail;
  }
  */
  return 0;
}
