
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "nonassocIFXnonassocELSEleft+-left*/leftDOTADDDOTSUBleftDOTMULDOTDIVrightUMINUSleft'ADDASSIGN BREAK CONTINUE DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQ EYE FLOATNUM FOR GE ID IF INTNUM LE MULASSIGN NEQ ONES PRINT RETURN STR SUBASSIGN WHILE ZEROSprogram : stmts_optstmts_opt : stmts\n                 | stmts : stmts stmt\n             | stmtstmt : ';'stmt : '{' stmts '}'id : IDlvalue : id\n              | id liststmt : lvalue '=' expr ';'\n            | lvalue ADDASSIGN expr ';'\n            | lvalue SUBASSIGN expr ';'\n            | lvalue MULASSIGN expr ';'\n            | lvalue DIVASSIGN expr ';'expr : expr '+' expr\n            | expr '-' expr\n            | expr '*' expr\n            | expr '/' expr\n            | expr DOTADD expr\n            | expr DOTSUB expr\n            | expr DOTMUL expr\n            | expr DOTDIV exprexpr : FLOATNUM\n            | INTNUMexpr : idexpr : STRexpr : '(' expr ')'expr : '-' expr %prec UMINUSexpr : expr '\\''cond : expr '<' expr\n            | expr '>' expr\n            | expr LE expr\n            | expr GE expr\n            | expr EQ expr\n            | expr NEQ exprexpr : '[' lists ']'lists : list\n             | lists ',' listlist : '[' seq ']'seq : expr\n           | seq ',' exprfun : ZEROS \n           | EYE\n           | ONESexpr : fun '(' expr ')'stmt : WHILE '(' cond ')' stmtstmt : FOR id '=' expr ':' expr stmtstmt : IF '(' cond ')' stmt %prec IFX\n            | IF '(' cond ')' stmt ELSE stmtstmt : BREAK ';'\n            | CONTINUE ';'\n            | RETURN expr ';'stmt : PRINT seq ';'"
    
_lr_action_items = {'$end':([0,1,2,3,4,5,17,29,30,45,56,71,73,74,75,76,77,101,109,114,115,],[-3,0,-1,-2,-5,-6,-4,-51,-52,-7,-53,-54,-11,-12,-13,-14,-15,-47,-49,-48,-50,]),';':([0,3,4,5,6,12,13,16,17,18,29,30,31,33,34,35,36,43,44,45,46,47,48,49,50,56,65,66,71,73,74,75,76,77,78,87,88,89,90,91,92,93,94,95,96,97,100,101,109,111,112,113,114,115,],[5,5,-5,-6,5,29,30,-8,-4,5,-51,-52,56,-24,-25,-26,-27,71,-41,-7,73,74,75,76,77,-53,-30,-29,-54,-11,-12,-13,-14,-15,5,5,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-42,-47,-49,-46,5,5,-48,-50,]),'{':([0,3,4,5,6,16,17,18,29,30,33,34,35,36,45,56,65,66,71,73,74,75,76,77,78,87,88,89,90,91,92,93,94,95,96,97,101,109,111,112,113,114,115,],[6,6,-5,-6,6,-8,-4,6,-51,-52,-24,-25,-26,-27,-7,-53,-30,-29,-54,-11,-12,-13,-14,-15,6,6,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-47,-49,-46,6,6,-48,-50,]),'WHILE':([0,3,4,5,6,16,17,18,29,30,33,34,35,36,45,56,65,66,71,73,74,75,76,77,78,87,88,89,90,91,92,93,94,95,96,97,101,109,111,112,113,114,115,],[8,8,-5,-6,8,-8,-4,8,-51,-52,-24,-25,-26,-27,-7,-53,-30,-29,-54,-11,-12,-13,-14,-15,8,8,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-47,-49,-46,8,8,-48,-50,]),'FOR':([0,3,4,5,6,16,17,18,29,30,33,34,35,36,45,56,65,66,71,73,74,75,76,77,78,87,88,89,90,91,92,93,94,95,96,97,101,109,111,112,113,114,115,],[9,9,-5,-6,9,-8,-4,9,-51,-52,-24,-25,-26,-27,-7,-53,-30,-29,-54,-11,-12,-13,-14,-15,9,9,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-47,-49,-46,9,9,-48,-50,]),'IF':([0,3,4,5,6,16,17,18,29,30,33,34,35,36,45,56,65,66,71,73,74,75,76,77,78,87,88,89,90,91,92,93,94,95,96,97,101,109,111,112,113,114,115,],[11,11,-5,-6,11,-8,-4,11,-51,-52,-24,-25,-26,-27,-7,-53,-30,-29,-54,-11,-12,-13,-14,-15,11,11,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-47,-49,-46,11,11,-48,-50,]),'BREAK':([0,3,4,5,6,16,17,18,29,30,33,34,35,36,45,56,65,66,71,73,74,75,76,77,78,87,88,89,90,91,92,93,94,95,96,97,101,109,111,112,113,114,115,],[12,12,-5,-6,12,-8,-4,12,-51,-52,-24,-25,-26,-27,-7,-53,-30,-29,-54,-11,-12,-13,-14,-15,12,12,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-47,-49,-46,12,12,-48,-50,]),'CONTINUE':([0,3,4,5,6,16,17,18,29,30,33,34,35,36,45,56,65,66,71,73,74,75,76,77,78,87,88,89,90,91,92,93,94,95,96,97,101,109,111,112,113,114,115,],[13,13,-5,-6,13,-8,-4,13,-51,-52,-24,-25,-26,-27,-7,-53,-30,-29,-54,-11,-12,-13,-14,-15,13,13,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-47,-49,-46,13,13,-48,-50,]),'RETURN':([0,3,4,5,6,16,17,18,29,30,33,34,35,36,45,56,65,66,71,73,74,75,76,77,78,87,88,89,90,91,92,93,94,95,96,97,101,109,111,112,113,114,115,],[14,14,-5,-6,14,-8,-4,14,-51,-52,-24,-25,-26,-27,-7,-53,-30,-29,-54,-11,-12,-13,-14,-15,14,14,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-47,-49,-46,14,14,-48,-50,]),'PRINT':([0,3,4,5,6,16,17,18,29,30,33,34,35,36,45,56,65,66,71,73,74,75,76,77,78,87,88,89,90,91,92,93,94,95,96,97,101,109,111,112,113,114,115,],[15,15,-5,-6,15,-8,-4,15,-51,-52,-24,-25,-26,-27,-7,-53,-30,-29,-54,-11,-12,-13,-14,-15,15,15,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-47,-49,-46,15,15,-48,-50,]),'ID':([0,3,4,5,6,9,14,15,16,17,18,19,20,21,22,23,24,27,28,29,30,32,33,34,35,36,37,45,53,56,57,58,59,60,61,62,63,64,65,66,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,87,88,89,90,91,92,93,94,95,96,97,101,108,109,111,112,113,114,115,],[16,16,-5,-6,16,16,16,16,-8,-4,16,16,16,16,16,16,16,16,16,-51,-52,16,-24,-25,-26,-27,16,-7,16,-53,16,16,16,16,16,16,16,16,-30,-29,16,-54,16,-11,-12,-13,-14,-15,16,16,16,16,16,16,16,16,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-47,16,-49,-46,16,16,-48,-50,]),'}':([4,5,17,18,29,30,45,56,71,73,74,75,76,77,101,109,114,115,],[-5,-6,-4,45,-51,-52,-7,-53,-54,-11,-12,-13,-14,-15,-47,-49,-48,-50,]),'ELSE':([5,29,30,45,56,71,73,74,75,76,77,101,109,114,115,],[-6,-51,-52,-7,-53,-54,-11,-12,-13,-14,-15,-47,113,-48,-50,]),'=':([7,10,16,25,26,86,],[19,-9,-8,53,-10,-40,]),'ADDASSIGN':([7,10,16,26,86,],[20,-9,-8,-10,-40,]),'SUBASSIGN':([7,10,16,26,86,],[21,-9,-8,-10,-40,]),'MULASSIGN':([7,10,16,26,86,],[22,-9,-8,-10,-40,]),'DIVASSIGN':([7,10,16,26,86,],[23,-9,-8,-10,-40,]),'(':([8,11,14,15,19,20,21,22,23,24,27,28,32,37,39,40,41,42,53,57,58,59,60,61,62,63,64,70,72,79,80,81,82,83,84,108,],[24,28,37,37,37,37,37,37,37,37,37,37,37,37,70,-43,-44,-45,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'[':([10,14,15,16,19,20,21,22,23,24,27,28,32,37,38,53,57,58,59,60,61,62,63,64,70,72,79,80,81,82,83,84,98,108,],[27,38,38,-8,38,38,38,38,38,38,38,38,38,38,27,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,27,38,]),'FLOATNUM':([14,15,19,20,21,22,23,24,27,28,32,37,53,57,58,59,60,61,62,63,64,70,72,79,80,81,82,83,84,108,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'INTNUM':([14,15,19,20,21,22,23,24,27,28,32,37,53,57,58,59,60,61,62,63,64,70,72,79,80,81,82,83,84,108,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'STR':([14,15,19,20,21,22,23,24,27,28,32,37,53,57,58,59,60,61,62,63,64,70,72,79,80,81,82,83,84,108,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'-':([14,15,16,19,20,21,22,23,24,27,28,31,32,33,34,35,36,37,44,46,47,48,49,50,52,53,57,58,59,60,61,62,63,64,65,66,67,70,72,79,80,81,82,83,84,85,88,89,90,91,92,93,94,95,96,97,99,100,102,103,104,105,106,107,108,111,112,],[32,32,-8,32,32,32,32,32,32,32,32,58,32,-24,-25,-26,-27,32,58,58,58,58,58,58,58,32,32,32,32,32,32,32,32,32,-30,-29,58,32,32,32,32,32,32,32,32,58,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,58,58,58,58,58,58,58,58,32,-46,58,]),'ZEROS':([14,15,19,20,21,22,23,24,27,28,32,37,53,57,58,59,60,61,62,63,64,70,72,79,80,81,82,83,84,108,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'EYE':([14,15,19,20,21,22,23,24,27,28,32,37,53,57,58,59,60,61,62,63,64,70,72,79,80,81,82,83,84,108,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'ONES':([14,15,19,20,21,22,23,24,27,28,32,37,53,57,58,59,60,61,62,63,64,70,72,79,80,81,82,83,84,108,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'+':([16,31,33,34,35,36,44,46,47,48,49,50,52,65,66,67,85,88,89,90,91,92,93,94,95,96,97,99,100,102,103,104,105,106,107,111,112,],[-8,57,-24,-25,-26,-27,57,57,57,57,57,57,57,-30,-29,57,57,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,57,57,57,57,57,57,57,57,-46,57,]),'*':([16,31,33,34,35,36,44,46,47,48,49,50,52,65,66,67,85,88,89,90,91,92,93,94,95,96,97,99,100,102,103,104,105,106,107,111,112,],[-8,59,-24,-25,-26,-27,59,59,59,59,59,59,59,-30,-29,59,59,59,59,-18,-19,-20,-21,-22,-23,-28,-37,59,59,59,59,59,59,59,59,-46,59,]),'/':([16,31,33,34,35,36,44,46,47,48,49,50,52,65,66,67,85,88,89,90,91,92,93,94,95,96,97,99,100,102,103,104,105,106,107,111,112,],[-8,60,-24,-25,-26,-27,60,60,60,60,60,60,60,-30,-29,60,60,60,60,-18,-19,-20,-21,-22,-23,-28,-37,60,60,60,60,60,60,60,60,-46,60,]),'DOTADD':([16,31,33,34,35,36,44,46,47,48,49,50,52,65,66,67,85,88,89,90,91,92,93,94,95,96,97,99,100,102,103,104,105,106,107,111,112,],[-8,61,-24,-25,-26,-27,61,61,61,61,61,61,61,-30,-29,61,61,61,61,61,61,-20,-21,-22,-23,-28,-37,61,61,61,61,61,61,61,61,-46,61,]),'DOTSUB':([16,31,33,34,35,36,44,46,47,48,49,50,52,65,66,67,85,88,89,90,91,92,93,94,95,96,97,99,100,102,103,104,105,106,107,111,112,],[-8,62,-24,-25,-26,-27,62,62,62,62,62,62,62,-30,-29,62,62,62,62,62,62,-20,-21,-22,-23,-28,-37,62,62,62,62,62,62,62,62,-46,62,]),'DOTMUL':([16,31,33,34,35,36,44,46,47,48,49,50,52,65,66,67,85,88,89,90,91,92,93,94,95,96,97,99,100,102,103,104,105,106,107,111,112,],[-8,63,-24,-25,-26,-27,63,63,63,63,63,63,63,-30,-29,63,63,63,63,63,63,63,63,-22,-23,-28,-37,63,63,63,63,63,63,63,63,-46,63,]),'DOTDIV':([16,31,33,34,35,36,44,46,47,48,49,50,52,65,66,67,85,88,89,90,91,92,93,94,95,96,97,99,100,102,103,104,105,106,107,111,112,],[-8,64,-24,-25,-26,-27,64,64,64,64,64,64,64,-30,-29,64,64,64,64,64,64,64,64,-22,-23,-28,-37,64,64,64,64,64,64,64,64,-46,64,]),"'":([16,31,33,34,35,36,44,46,47,48,49,50,52,65,66,67,85,88,89,90,91,92,93,94,95,96,97,99,100,102,103,104,105,106,107,111,112,],[-8,65,-24,-25,-26,-27,65,65,65,65,65,65,65,-30,65,65,65,65,65,65,65,65,65,65,65,-28,-37,65,65,65,65,65,65,65,65,-46,65,]),',':([16,33,34,35,36,43,44,54,65,66,68,69,86,88,89,90,91,92,93,94,95,96,97,100,110,111,],[-8,-24,-25,-26,-27,72,-41,72,-30,-29,98,-38,-40,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-42,-39,-46,]),'<':([16,33,34,35,36,52,65,66,88,89,90,91,92,93,94,95,96,97,111,],[-8,-24,-25,-26,-27,79,-30,-29,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-46,]),'>':([16,33,34,35,36,52,65,66,88,89,90,91,92,93,94,95,96,97,111,],[-8,-24,-25,-26,-27,80,-30,-29,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-46,]),'LE':([16,33,34,35,36,52,65,66,88,89,90,91,92,93,94,95,96,97,111,],[-8,-24,-25,-26,-27,81,-30,-29,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-46,]),'GE':([16,33,34,35,36,52,65,66,88,89,90,91,92,93,94,95,96,97,111,],[-8,-24,-25,-26,-27,82,-30,-29,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-46,]),'EQ':([16,33,34,35,36,52,65,66,88,89,90,91,92,93,94,95,96,97,111,],[-8,-24,-25,-26,-27,83,-30,-29,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-46,]),'NEQ':([16,33,34,35,36,52,65,66,88,89,90,91,92,93,94,95,96,97,111,],[-8,-24,-25,-26,-27,84,-30,-29,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-46,]),']':([16,33,34,35,36,44,54,65,66,68,69,86,88,89,90,91,92,93,94,95,96,97,100,110,111,],[-8,-24,-25,-26,-27,-41,86,-30,-29,97,-38,-40,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-42,-39,-46,]),')':([16,33,34,35,36,51,55,65,66,67,88,89,90,91,92,93,94,95,96,97,99,102,103,104,105,106,107,111,],[-8,-24,-25,-26,-27,78,87,-30,-29,96,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,111,-31,-32,-33,-34,-35,-36,-46,]),':':([16,33,34,35,36,65,66,85,88,89,90,91,92,93,94,95,96,97,111,],[-8,-24,-25,-26,-27,-30,-29,108,-16,-17,-18,-19,-20,-21,-22,-23,-28,-37,-46,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'stmts_opt':([0,],[2,]),'stmts':([0,6,],[3,18,]),'stmt':([0,3,6,18,78,87,112,113,],[4,17,4,17,101,109,114,115,]),'lvalue':([0,3,6,18,78,87,112,113,],[7,7,7,7,7,7,7,7,]),'id':([0,3,6,9,14,15,18,19,20,21,22,23,24,27,28,32,37,53,57,58,59,60,61,62,63,64,70,72,78,79,80,81,82,83,84,87,108,112,113,],[10,10,10,25,35,35,10,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,10,35,35,35,35,35,35,10,35,10,10,]),'list':([10,38,98,],[26,69,110,]),'expr':([14,15,19,20,21,22,23,24,27,28,32,37,53,57,58,59,60,61,62,63,64,70,72,79,80,81,82,83,84,108,],[31,44,46,47,48,49,50,52,44,52,66,67,85,88,89,90,91,92,93,94,95,99,100,102,103,104,105,106,107,112,]),'fun':([14,15,19,20,21,22,23,24,27,28,32,37,53,57,58,59,60,61,62,63,64,70,72,79,80,81,82,83,84,108,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'seq':([15,27,],[43,54,]),'cond':([24,28,],[51,55,]),'lists':([38,],[68,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> stmts_opt','program',1,'p_program','Mparser.py',30),
  ('stmts_opt -> stmts','stmts_opt',1,'p_stmts_opt','Mparser.py',34),
  ('stmts_opt -> <empty>','stmts_opt',0,'p_stmts_opt','Mparser.py',35),
  ('stmts -> stmts stmt','stmts',2,'p_stmts','Mparser.py',39),
  ('stmts -> stmt','stmts',1,'p_stmts','Mparser.py',40),
  ('stmt -> ;','stmt',1,'p_stmt_empty','Mparser.py',44),
  ('stmt -> { stmts }','stmt',3,'p_stmts_grp','Mparser.py',47),
  ('id -> ID','id',1,'p_id','Mparser.py',51),
  ('lvalue -> id','lvalue',1,'p_lvalue','Mparser.py',55),
  ('lvalue -> id list','lvalue',2,'p_lvalue','Mparser.py',56),
  ('stmt -> lvalue = expr ;','stmt',4,'p_assignment','Mparser.py',60),
  ('stmt -> lvalue ADDASSIGN expr ;','stmt',4,'p_assignment','Mparser.py',61),
  ('stmt -> lvalue SUBASSIGN expr ;','stmt',4,'p_assignment','Mparser.py',62),
  ('stmt -> lvalue MULASSIGN expr ;','stmt',4,'p_assignment','Mparser.py',63),
  ('stmt -> lvalue DIVASSIGN expr ;','stmt',4,'p_assignment','Mparser.py',64),
  ('expr -> expr + expr','expr',3,'p_expr_binop','Mparser.py',68),
  ('expr -> expr - expr','expr',3,'p_expr_binop','Mparser.py',69),
  ('expr -> expr * expr','expr',3,'p_expr_binop','Mparser.py',70),
  ('expr -> expr / expr','expr',3,'p_expr_binop','Mparser.py',71),
  ('expr -> expr DOTADD expr','expr',3,'p_expr_binop','Mparser.py',72),
  ('expr -> expr DOTSUB expr','expr',3,'p_expr_binop','Mparser.py',73),
  ('expr -> expr DOTMUL expr','expr',3,'p_expr_binop','Mparser.py',74),
  ('expr -> expr DOTDIV expr','expr',3,'p_expr_binop','Mparser.py',75),
  ('expr -> FLOATNUM','expr',1,'p_expr_lit','Mparser.py',79),
  ('expr -> INTNUM','expr',1,'p_expr_lit','Mparser.py',80),
  ('expr -> id','expr',1,'p_expr_id','Mparser.py',84),
  ('expr -> STR','expr',1,'p_expr_str','Mparser.py',88),
  ('expr -> ( expr )','expr',3,'p_expr_grp','Mparser.py',92),
  ('expr -> - expr','expr',2,'p_uminus','Mparser.py',96),
  ("expr -> expr '",'expr',2,'p_transpose','Mparser.py',100),
  ('cond -> expr < expr','cond',3,'p_cond','Mparser.py',104),
  ('cond -> expr > expr','cond',3,'p_cond','Mparser.py',105),
  ('cond -> expr LE expr','cond',3,'p_cond','Mparser.py',106),
  ('cond -> expr GE expr','cond',3,'p_cond','Mparser.py',107),
  ('cond -> expr EQ expr','cond',3,'p_cond','Mparser.py',108),
  ('cond -> expr NEQ expr','cond',3,'p_cond','Mparser.py',109),
  ('expr -> [ lists ]','expr',3,'p_literal_matrix','Mparser.py',113),
  ('lists -> list','lists',1,'p_lists','Mparser.py',117),
  ('lists -> lists , list','lists',3,'p_lists','Mparser.py',118),
  ('list -> [ seq ]','list',3,'p_list','Mparser.py',122),
  ('seq -> expr','seq',1,'p_seq','Mparser.py',126),
  ('seq -> seq , expr','seq',3,'p_seq','Mparser.py',127),
  ('fun -> ZEROS','fun',1,'p_fun','Mparser.py',131),
  ('fun -> EYE','fun',1,'p_fun','Mparser.py',132),
  ('fun -> ONES','fun',1,'p_fun','Mparser.py',133),
  ('expr -> fun ( expr )','expr',4,'p_funcall','Mparser.py',137),
  ('stmt -> WHILE ( cond ) stmt','stmt',5,'p_while','Mparser.py',141),
  ('stmt -> FOR id = expr : expr stmt','stmt',7,'p_for','Mparser.py',145),
  ('stmt -> IF ( cond ) stmt','stmt',5,'p_if','Mparser.py',149),
  ('stmt -> IF ( cond ) stmt ELSE stmt','stmt',7,'p_if','Mparser.py',150),
  ('stmt -> BREAK ;','stmt',2,'p_control','Mparser.py',154),
  ('stmt -> CONTINUE ;','stmt',2,'p_control','Mparser.py',155),
  ('stmt -> RETURN expr ;','stmt',3,'p_control','Mparser.py',156),
  ('stmt -> PRINT seq ;','stmt',3,'p_print','Mparser.py',165),
]
