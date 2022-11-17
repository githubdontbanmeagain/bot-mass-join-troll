import subprocess

def get_tokens():
    with open("tokens.txt", "r") as f:
        return f.read().splitlines()

if __name__ == "__main__":
    tokens = get_tokens()
    for token in tokens:
        subprocess.Popen(r"python %s%s" % ("", f"sub.py -t {token}"), shell=True)