base_dir=$(dirname "$(readlink -f "$0")")
config_file=${base_dir}/.pylintrc

cd ${base_dir}

echo "Running black"
black --check --verbose .

BLACK_EXIT=$?

if [[ BLACK_EXIT -ne 0 ]]; then
    echo "Black failed"
    exit 1
fi

echo "Black passed"

