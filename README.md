# password-checker
RUN FIRST!

python -m pip install -r requirements.txt


THEN
RUN FROM THE COMMAND LINE

python checkmypass.py "PASSWORD TO CHECK"

EXAMPLES

-- checking 1 password
python checkmypass.py helloworld 

-- 2 passwords
python checkmypass.py helloworld test

-- can check as many as you want at a time, listed one after another
