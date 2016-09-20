nella cartella test_eigen ho trovato un ragazzo che fa la conversione in questo modo ma non riesco a compilarlo continua a darmi errore su import foo.

  File "wrapper_example.py", line 6, in <module>
    from FooClass import FooClass
ImportError: No module named FooClass


Nella cartella test_bb stavo cercando di far comunicare i due codici importando per prima cosa la classe box e poi le funzioni che avevo creato, ma mi da quel errore swig_import_helper() sul file pyc
lo compilo con  
cmake . -DBUILD_SHARED_LIBS=ON
perchè senno mi da errore 

/usr/bin/ld: libtest_dany_bb.a(pacman_bb_test.cpp.o): relocation R_X86_64_32S against `_ZTVN5boost16exception_detail10clone_baseE' can not be used when making a shared object; recompile with -fPIC
libtest_dany_bb.a: error adding symbols: Bad value

compilo poi con sudo make install e mi esce sempre questo

  File "main.py", line 1, in <module>
    import Exampletest_dany_bb	#importo funzione delle bb
  File "/home/daniela/Projects/Tutorial_python/Test_import_c++/Test_bb/Exampletest_dany_bb.py", line 28, in <module>
    _Exampletest_dany_bb = swig_import_helper()
  File "/home/daniela/Projects/Tutorial_python/Test_import_c++/Test_bb/Exampletest_dany_bb.py", line 20, in swig_import_helper
    import _Exampletest_dany_bb
ImportError: libtest_dany_bb.so: cannot open shared object file: No such file or directory

