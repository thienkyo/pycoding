# Unpack a long list
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *not_relevant, homedir, sh = line.split(':')
print(uname, homedir, sh)  # nobody /var/empty /usr/bin/false

