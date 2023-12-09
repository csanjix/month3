CREATE_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS telegram_users
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
USERNAME CHAR(50),
FISRT_NAME CHAR(50),
LAST_NAME CHAR(50),
UNIQUE (TELEGRAM_ID)
)
"""

ALTER_USER_TABLE = """
ALTER TABLE telegram_users
ADD COLUMN REFERENCE_LINK TEXT
"""

ALTER_USER_V2_TABLE = """
ALTER TABLE telegram_users
ADD COLUMN BALANCE INTEGER
"""

CREATE_BAN_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS ban_users
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
COUNT INTEGER,
UNIQUE (TELEGRAM_ID)
)
"""

CREATE_USER_FORM_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS user_form
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
NICKNAME CHAR(50),
BIO TEXT,
GEO TEXT,
GENDER CHAR(50),
AGE INTEGER,
PHOTO TEXT,
UNIQUE (TELEGRAM_ID)
)
"""

CREATE_LIKE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS like_forms
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
LIKER_TELEGRAM_ID INTEGER,
UNIQUE (OWNER_TELEGRAM_ID, LIKER_TELEGRAM_ID)
)
"""

CREATE_REFERRAL_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS referral
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
REFERRAL_TELEGRAM_ID INTEGER,
UNIQUE (OWNER_TELEGRAM_ID, REFERRAL_TELEGRAM_ID)
)
"""

INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?,?,?)
"""

INSERT_BAN_USER_QUERY = """
INSERT INTO ban_users VALUES (?,?,?)
"""

INSERT_LIKE_QUERY = """
INSERT INTO like_forms VALUES (?,?,?)
"""

INSERT_USER_FORM_QUERY = """
INSERT INTO user_form VALUES (?,?,?,?,?,?,?,?)
"""

SELECT_BAN_USER_QUERY = """
SELECT * FROM ban_users WHERE TELEGRAM_ID = ?
"""

SELECT_USER_LINK_QUERY = """
SELECT REFERENCE_LINK FROM telegram_users WHERE TELEGRAM_ID = ?
"""

SELECT_USER_BY_LINK_QUERY = """
SELECT TELEGRAM_ID FROM telegram_users WHERE REFERENCE_LINK = ?
"""

SELECT_USER_FORM_QUERY = """
SELECT * FROM user_form WHERE TELEGRAM_ID = ?
"""

SELECT_ALL_USER_FORM_QUERY = """
SELECT * FROM user_form
"""

UPDATE_BAN_USER_COUNT_QUERY = """
UPDATE ban_users SET COUNT = COUNT + 1 WHERE TELEGRAM_ID = ?
"""

FILTER_LEFT_JOIN_USER_FORM_LIKE_QUERY = """
SELECT * FROM user_form
LEFT JOIN like_forms ON user_form.TELEGRAM_ID = like_forms.OWNER_TELEGRAM_ID
AND like_forms.LIKER_TELEGRAM_ID = ?
WHERE like_forms.ID IS NULL
AND user_form.TELEGRAM_ID != ?
"""

DOUBLE_SELECT_REFERRAL_USER_QUERY = """
SELECT
    COALESCE(telegram_users.BALANCE, 0) AS BALANCE,
    COUNT(referral.ID) AS total_referral
FROM
    telegram_users
LEFT JOIN
    referral ON telegram_users.TELEGRAM_ID = referral.OWNER_TELEGRAM_ID
WHERE
    telegram_users.TELEGRAM_ID = ?
"""

UPDATE_REFERENCE_LINK_QUERY = """
UPDATE telegram_users SET REFERENCE_LINK = ? WHERE TELEGRAM_ID = ?
"""

UPDATE_USER_BALANCE_QUERY = """
UPDATE telegram_users SET BALANCE = COALESCE(BALANCE, 0) + 100 WHERE TELEGRAM_ID = ?
"""

INSERT_REFERRAL_QUERY = """
INSERT INTO referral VALUES (?,?,?)
"""

ALTER_USER_V2_TABLE = """
ALTER TABLE telegram_users
ADD COLUMN BALANCE INTEGER,
ADD COLUMN WALLET INTEGER;
"""

UPDATE_USER_BALANCE_QUERY = """
UPDATE telegram_users SET BALANCE = COALESCE(BALANCE, 0) + 100 WHERE TELEGRAM_ID = ?;
"""

CREATE_WALLET_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS wallet
(
    ID INTEGER PRIMARY KEY,
    USER_TELEGRAM_ID INTEGER,
    AMOUNT INTEGER,
    UNIQUE (USER_TELEGRAM_ID)
);
"""

INSERT_WALLET_QUERY = """
INSERT INTO wallet VALUES (NULL, ?, ?);
"""

SELECT_WALLET_AMOUNT_QUERY = """
SELECT AMOUNT FROM wallet WHERE USER_TELEGRAM_ID = ?;
"""