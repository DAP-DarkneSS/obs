# distro.py for openSUSE

if not sysconf.getReadOnly():
    # https://bugzilla.novell.com/show_bug.cgi?id=199127
    sysconf.set(("channels", "rpm-sys"),
                {"alias": "rpm-sys",
                 "type": "rpm-sys",
                 "name": "RPM System"})

    sysconf.set("rpm-check-signatures", True, weak=True)
    sysconf.set("keyserver", "subkeys.pgp.net", weak=True)

    pkgconf.setFlag("multi-version", "java")
