
#fake data that comes out of the database and netowork
import pytest
import smtplib

def ehlo(smtpi):
    return (250, b'smtp.gmail.com BLA BLA')
def noop(smtpi):
    return (250, b'BLA BLA gsmtp')

@pytest.fixture(autouse=True)
# so here we have got rid of the calls to google, then create an instance of it 
def smtp(monkeypatch):
    #smtp_instance = smtplib.SMTP()
    monkeypatch.setattr(smtplib.SMTP, "ehlo", ehlo)
    monkeypatch.setattr(smtplib.SMTP, "noop", noop)
    return smtplib.SMTP()