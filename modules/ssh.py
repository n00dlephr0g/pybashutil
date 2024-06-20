import os

def ssh(username: str, ip: str, authkey: str):
    os.system(f"ssh {username}@{ip}")
