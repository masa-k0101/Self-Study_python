# -*- coding: utf-8 -*-

#! python3
# phoneAndEmail.py - クリップボードから電話番号とメアドを検索する

import pyperclip, re

phone_regex = re.compile(r'''(
    (\d{3}|\(d{3}\))?           # 市外局番
    (\s|-|\.)?                  # 区切り
    (\d{3})                     # 3桁の番号
    (\s|-|\.)?                  # 区切り
    (\d{4})                     # 4桁の番号
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # 内線番号
    )''', re.VERBOSE)

# 電子メールの正規表現を作る
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           # ユーザー名
    @                           # @ 記号
    [a-zA-Z0-9.-]+              # ドメイン名
    (\.[a-zA-Z]{2,4})           # ドット
    )''', re.VERBOSE)

# TODO:

# TODO: