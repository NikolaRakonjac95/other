import os

with open('IP.txt', "r") as output, open('IP_reachable.txt', "w") as output_1:
    keep = True
    output_text = output.readlines()
    for ip in output_text:
        response = os.system('ping {}'.format(ip))
        if keep and response == 0:
            output_1.write(ip)
        else:
            print('ip {} not available'.format(ip))
