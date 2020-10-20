base_dir=$(dirname "$(readlink -f "$0")")
config_file=${base_dir}/.pylintrc

cd ${base_dir}


pytest --cov=. --covconfig=../.coveragerc


TEST_EXIT=$?

if [[ TEST_EXIT -ne 0 ]]; then
    echo "Unit tests failed"
    exit 1
fi

echo "Unit tests passed"