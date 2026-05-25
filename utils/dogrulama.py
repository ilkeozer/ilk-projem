def bos_mu(veri):

    return veri.strip() == ""


def email_kontrol(email):

    return "@" in email and "." in email
