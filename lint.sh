base_dir=$(dirname "$(readlink -f "$0")")
config_file=${base_dir}/.pylintrc

cd ${base_dir}

python_files=$(find . -name '*.py')

echo "Found the following files:"
printf "%s\n" ${python_files}

echo "Running Pylint"
echo ${python_files} | xargs python -u -m pylint --rcfile=${config_file}