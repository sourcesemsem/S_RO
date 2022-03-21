from sqlalchemy import Boolean, Column, String

from userbot.plugins.sql_helper import BASE, SESSION


class Locks(BASE):
    __tablename__ = "locks"
    chat_id = Column(String(14), primary_key=True)
    # Booleans are for "is this locked", _NOT_ "is this allowed"
    bots = Column(Boolean, default=False)
    farsi = Column(Boolean, default=False)
    fosha = Column(Boolean, default=False)
    forward = Column(Boolean, default=False)
    fumed = Column(Boolean, default=False)
    username = Column(Boolean, default=False)
    url = Column(Boolean, default=False)

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)  # ensure string
        self.bots = False
        self.farsi = False
        self.fosha = False
        self.forward = False
        self.fumed = False
        self.username = False
        self.url = False


Locks.__table__.create(checkfirst=True)


def init_locks(chat_id, reset=False):
    curr_restr = SESSION.query(Locks).get(str(chat_id))
    if reset:
        SESSION.delete(curr_restr)
        SESSION.flush()
    restr = Locks(str(chat_id))
    SESSION.add(restr)
    SESSION.commit()
    return restr


def update_lock(chat_id, lock_type, locked):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    if not curr_perm:
        curr_perm = init_locks(chat_id)
    if lock_type == "bots":
        curr_perm.bots = locked
    elif lock_type == "farsi":
        curr_perm.farsi = locked
    elif lock_type == "fosha":
        curr_perm.fosha = locked
    elif lock_type == "forward":
        curr_perm.forward = locked
    elif lock_type == "fumed":
        curr_perm.fumed = locked
    elif lock_type == "username":
        curr_perm.username = locked
    elif lock_type == "url":
        curr_perm.url = locked
    SESSION.add(curr_perm)
    SESSION.commit()


def is_locked(chat_id, lock_type):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    SESSION.close()
    if not curr_perm:
        return False
    if lock_type == "bots":
        return curr_perm.bots
    if lock_type == "farsi":
        return curr_perm.farsi
    if lock_type == "fosha":
        return curr_perm.fosha
    if lock_type == "forward":
        return curr_perm.forward
    if lock_type == "fumed":
        return curr_perm.fumed
    if lock_type == "username":
        return curr_perm.username
    if lock_type == "url":
        return curr_perm.url


def get_locks(chat_id):
    try:
        return SESSION.query(Locks).get(str(chat_id))
    finally:
        SESSION.close()
