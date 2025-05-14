def get_cookies():
    cookies_str = "_WEU=lMAnrz9v_MtpDKhjtPicV28ar3C_9rrnSPto06PTYmJGCVCrW7e08XdZpGN7vXePdWRWQUGvw4a2Yml668fwJS*03oeEZLMoUcVxL9Ai_m7lSdce1IdYXiO781udNDb6hEgXyjIruuUHrC938dZbC6cmk80KANG45uHtAtin9WYthQlRb5T2WradV2tphb7Y; EMAP_LANG=zh; THEME=cherry; JSESSIONID=5hrPMzstLEbD-sj6qK2YXF4xPbDg_TiETSuKM04alfmrYNjk3j4B!-656819764; amp.locale=undefined; MOD_AMP_AUTH=MOD_AMP_0e142312-9af3-46d8-8b9f-a96978ad418a; asessionid=c301afc9-20be-4cac-9d3c-f7e8a4d94e89; route=ab22dc972e174017d573ee90262bcc96; CASTGC=plXj2hpTFptwjb0yWXiaOcOFpxYOtGreIrx4mws9xLnpHfr3TlXLNw==; CASTGC=TGT-2613947-EkZDccBzXg1QOzsJ5AqVghrRnJkStJAxfpiQvsXqbtWqnvNaJT-gdscas01"
    cookies = {}
    item = cookies_str.split("; ")
    for i in item:
        print(i)
        key, value = i.split("=", maxsplit=1)
        cookies.update({key: value})
    return cookies

COOKIES = get_cookies()
print(COOKIES)