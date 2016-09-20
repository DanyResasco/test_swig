/* File : example.i */
%module Exampletest_dany
%{
#include "test_dany_code.h"
%}

/* Wrap a function taking a pointer to a function */
%include "test_dany_code.h"
