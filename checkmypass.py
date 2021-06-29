import requests
import hashlib
import sys


"""
make a function to hit the api, accepts the hashed data. small subset of the total hash
"""


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {response.status_code}, check the api and try again')
    return response


"""
function to determine the number of times the password as been hacked, 
accepts the list of hashes from request_api_data as well as the hash for the password we are looking for
"""


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


"""
takes the password and hashes it. splits the hashed password into the query and the tail hash... first 5 chars and then the rest...
sends the first 5 chars to the api request which returns the lists of all the responses, could be hundreds.
then it sends that list of hashes and the tail to the get_password_leaks_count, returning a count
"""


def pwned_api_check(password):
    # check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


"""
main takes the arguments from the cmd, loops through them if more then one given.
It gets the cound for each password given and prints it into the cmd back to the user
"""


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f'{password} was found {count} times... you should think about changing your password')
        else:
            print(f'{password} was not found, its a good password... for now')
    return 'Done checking'


"""
only going to run if this file is run as the main file
"""
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
