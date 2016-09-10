/* File : example.i */
%module Exampletest_dany
%{
extern int do_op(int,int, int (*op)(int,int));
extern int add(int,int);
extern int sub(int,int);
extern int mul(int,int);

extern int (*funcvar)(int,int);
%}

/* Wrap a function taking a pointer to a function */
extern int  do_op(int a, int b, int (*op)(int, int));

/* Now install a bunch of "ops" as constants */
%constant int (*ADD)(int,int) = add;
%constant int (*SUB)(int,int) = sub;
%constant int (*MUL)(int,int) = mul;

extern int (*funcvar)(int,int);

