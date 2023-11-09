import kiosk_backend

s = kiosk_backend.start()
if s != '!P':
    q = 'k'
    while q != '':
        print(s)
        q = input()
        s = kiosk_backend.get_input(q)
    out = kiosk_backend.output()
    print(out)