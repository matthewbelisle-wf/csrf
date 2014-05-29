CSRF demo for team learning

Setup
=====

* `sudo pip install -Ur requirements.txt`
* Run `./bank.py` and keep it running.
* Open http://127.0.0.1:5000/
* Login.  The password is `donuts`.
* Run `./hacker.py` and keep it running.
* Open http://127.0.0.1:5001/

Notice how the [hacker site](./templates/hacker.html) is able to execute a cross site request forgery and trick the bank's
legitimate user into sending $1000 to the hacker.

Task
====

Use the CSRF helpers in [bank.py](./bank.py) to stop the hacker.  It's ~3 lines of code with hints in the comments.

https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF)