#!/usr/bin/env python3

import hashlib
import random
import string

allchar = string.ascii_letters + string.digits
password = "".join(random.choice(allchar) for x in range(random.randint(12, 12)))
print("Token: " + password)
tokenhash = hashlib.sha256(password.encode("utf-8")).hexdigest()

with open("/root/token.sha256", "w") as f:
    f.write(tokenhash)
