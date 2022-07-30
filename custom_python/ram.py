import psutil
def bytes_format(n):
    for x in ['bytes', 'KB', 'MB', 'GB']:
        if n < 1024.0:
            return "%3.1f %s" % (n, x)
        n /= 1024.0
response=list(psutil.virtual_memory())
# Total ram.
print("Total Ram:", bytes_format(int(response[0])))
# Ram used.
print("Ram used :", bytes_format(int(response[3])))
# Ram free.
print("Ram Free :", bytes_format(int(response[1])))
