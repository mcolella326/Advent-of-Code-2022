# exec(s:='print("%r"%s)')

# exec(s := 'print("exec(s := %r})" % s)')
exec(s := 'print(f"exec(s := {s!r})")')