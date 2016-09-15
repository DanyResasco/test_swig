#define WRAP_PYTHON 1
#if WRAP_PYTHON
#include <Python.h>
#include <boost/python.hpp>
#include <numpy/arrayobject.h>
#endif 

#include <iostream>
using namespace std;

#include <eigen3/Eigen/Dense>
#include <eigen3/Eigen/Core>
// #include <Eigen/Array>
using namespace Eigen;

class FooClass
{
public:
	FooClass( int new_m );
	~FooClass();
	
	template<typename Derived>
	int foo(const MatrixBase<Derived>& barIn, MatrixBase<Derived>& barOut);
#if WRAP_PYTHON
	int foo_python(PyObject* barIn, PyObject* barOut);
#endif
private:
	int m;
};
#endif