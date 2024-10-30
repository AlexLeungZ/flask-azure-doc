# This script will delete everything in the cython directory and build directory.
# Then create a zip file via deploy.py.
rm -r cython/
rm -r build/
python deploy.py