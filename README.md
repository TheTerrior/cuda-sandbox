# CUDA Sandbox
Experimentation with CUDA and various languages

## Compile and Run (Python)
cc -fPIC -shared -o functions.so functions.c
py main.py

## Compile and Run (Go)
nvcc --ptxas-options=-v --compiler-options '-fPIC' -o libmaxmul.so --shared maxmul.cu
LD_LIBRARY_PATH=. go run maxmul.go



