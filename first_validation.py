""" First validation
"""

from pathlib import Path

from hashlib import sha1

data_pth = Path() / 'data'
example_pth =  data_pth / '24719.f3_beh_CHYM.csv'

if not example_pth.is_file():
    raise RuntimeError('Have you run the "get_data.py" script?')

contents = example_pth.read_bytes()
hash_value = sha1(contents).hexdigest()

print(f'Hash value for {example_pth} is {hash_value}')

hashes_pth = data_pth / 'data_hashes.txt'

print(f'Contents of {hashes_pth}')
hashes_text = hashes_pth.read_text()
print(hashes_text)


def hash_for_fname(fname):
    """ Return SHA1 hash string for file in `fname`

    `fname` can be a string or a Path.
    """
    # Convert a string filename to a Path object.
    fpath = Path(fname)
    
    file_contents = fpath.read_bytes()
    file_hash_value = sha1(file_contents).hexdigest()
    return file_hash_value


# Fill in the function above to make the test below pass.
# The test passes when there is no error.
calc_hash = hash_for_fname(example_pth)
exp_hash = '7fa09f0f0dc11836094b8d360dc63943704796a1'
assert calc_hash == exp_hash, f'{calc_hash} does not match {exp_hash}'


def check_hashes(hash_fname):
    """ Check hashes and filenames in given in file `hash_fname`
    """
    hash_pth = Path(hash_fname)
    # Directory containing hash filenames file.
    data_dir = hash_pth.parent
        
    with open(hash_fname) as file:
        for line in file.readlines():
            expected_hash, file_name = line.split()
            file_name = data_dir / file_name
            calculated_hash = hash_for_fname(file_name)
            if calculated_hash != expected_hash :
                return False
    
    return True


assert check_hashes(hashes_pth), 'Check hash list does not return True'
