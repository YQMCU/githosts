import urllib.request

git_hosts_url = 'http://git.yoqi.me/lyq/github-host/raw/master/hosts'
hosts_pathname = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
copyname = 'hosts_copy.txt'
tmpname = 'tmp.txt'

def overwrite(text):
    # copy origin hosts
    with open(hosts_pathname, 'r') as f:
        content = f.read()
        # rows = f.readlines()
        with open(copyname, 'w') as fw:
            fw.write(content)

    rows = content.split('\n')
    #tmp_name = []
    #with open(hosts_pathname, 'r')
    for line in rows:
        if 'github' in line or 'blog.yoqi.me' in line:
            # print(line)
            break
    # print(rows)

    with open(hosts_pathname, 'w', encoding='ansi') as f:
        for line in rows:
            if 'github' in line or 'blog.yoqi.me' in line:
                continue
            f.write(line+'\n')
        f.write(text)
    # print(text)


def main():
    res = urllib.request.urlopen(git_hosts_url)
    # print(res.reason)
    # print(res.status)
    # print(res.url)
    # print(res.headers)
    if res.status == 200 :
        text = res.read().decode('utf-8')
        if text != '':
            overwrite(text)

    print(res.read().decode('utf-8'))

if __name__ == '__main__':
    main()